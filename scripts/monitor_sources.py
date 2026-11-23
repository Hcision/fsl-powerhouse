#!/usr/bin/env python3
"""Compare visible text on curated Salesforce documentation entry points.

Pages that only render in a browser, such as Salesforce Help articles, are
read through the optional sf-docs CLI when it is on PATH.
"""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.error import URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL_HOSTS = {
    "resources.docs.salesforce.com", "help.salesforce.com", "developer.salesforce.com", "architect.salesforce.com",
    "issues.salesforce.com", "trailhead.salesforce.com",
}


class ThinPage(ValueError):
    """The response holds too little visible text to compare."""


def official(url):
    parts = urlsplit(url)
    return (parts.scheme == "https" and parts.netloc in OFFICIAL_HOSTS)


class OfficialRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not official(newurl):
            raise ValueError("Redirect outside approved Salesforce documentation hosts")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class VisibleText(HTMLParser):
    ignored = {"head", "script", "style", "svg", "noscript", "nav", "footer"}
    void = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
            "meta", "param", "source", "track", "wbr"}

    def __init__(self):
        super().__init__()
        self.hidden = []
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.void and (self.hidden or tag in self.ignored):
            self.hidden.append(tag)

    def handle_endtag(self, tag):
        if tag in self.hidden:
            index = len(self.hidden) - 1 - self.hidden[::-1].index(tag)
            del self.hidden[index:]

    def handle_data(self, data):
        if not self.hidden and data.strip():
            self.parts.append(data.strip())


def text_fingerprint(text):
    normalized = re.sub(r"\s+", " ", text).strip()
    if len(normalized) < 300:
        raise ThinPage("Too little visible text. Check the rendered page manually.")
    return hashlib.sha256(normalized.encode()).hexdigest()


def fingerprint(raw):
    parser = VisibleText()
    parser.feed(raw)
    return text_fingerprint(" ".join(parser.parts))


def render(url, executable):
    """Return the page as Markdown from sf-docs, which renders JavaScript pages."""
    result = subprocess.run([executable, "--format", "md", "--no-cache", "fetch", url],
                            shell=False, capture_output=True, text=True, timeout=90)
    if result.returncode:
        lines = result.stderr.strip().splitlines()
        raise ValueError(lines[0][:350] if lines else f"sf-docs exited {result.returncode}")
    return result.stdout


def download(url):
    with build_opener(OfficialRedirects()).open(
        Request(url, headers={"User-Agent": "FSLPowerhouseDocsMonitor/0.2"}), timeout=12
    ) as response:
        if response.headers.get_content_type() != "text/html":
            raise ValueError("Unexpected response type")
        maximum = 4_000_000
        content = response.read(maximum + 1)
        if len(content) > maximum:
            raise ValueError("Document exceeds monitor size limit")
        return content.decode(response.headers.get_content_charset() or "utf-8", errors="replace")


def probe(url, renderer=None, download=download):
    """Fingerprint a page, using the renderer when the static response is a shell."""
    if not official(url):
        raise ValueError("Expected an official HTTPS documentation URL")
    try:
        return fingerprint(download(url))
    except ThinPage:
        if renderer is None:
            raise ThinPage("Page renders in the browser only. Install sf-docs to monitor it.") from None
    # The prefix keeps a rendered digest from matching a static one for the same page.
    return "rendered:" + text_fingerprint(renderer(url))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=ROOT / ".cache/source-state.json")
    parser.add_argument("--all", action="store_true", help="Check all catalog entries")
    args = parser.parse_args()
    previous = json.loads(args.state.read_text()) if args.state.exists() else {}
    executable = shutil.which("sf-docs")
    renderer = None
    if executable:
        executable = str(Path(executable).absolute())
        renderer = lambda url: render(url, executable)  # noqa: E731
    current = previous.copy()
    errors = 0
    for source in json.loads((ROOT / "knowledge/sources.json").read_text()):
        if not args.all and not source.get("monitor"):
            continue
        key = source["id"]
        try:
            digest = probe(source["url"], renderer)
        except (OSError, URLError, ValueError, subprocess.SubprocessError) as exc:
            errors += 1
            print(f"REVIEW MANUALLY | {key} | {exc} | {source['url']}")
            continue
        old = previous.get(key)
        status = "BASELINE" if old is None else "UNCHANGED" if old == digest else "CHANGED"
        print(f"{status} | {key} | {source['url']}")
        current[key] = digest
    args.state.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.state.with_suffix(".tmp")
    temporary.write_text(json.dumps(current, sort_keys=True, indent=2) + "\n")
    temporary.replace(args.state)
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
