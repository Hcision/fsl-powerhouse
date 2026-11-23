#!/usr/bin/env python3
"""Compare visible text on curated Salesforce documentation entry points."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.error import URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL_HOSTS = {
    "resources.docs.salesforce.com", "help.salesforce.com", "developer.salesforce.com", "architect.salesforce.com",
    "issues.salesforce.com", "trailhead.salesforce.com",
}


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


def fingerprint(raw):
    parser = VisibleText()
    parser.feed(raw)
    normalized = re.sub(r"\s+", " ", " ".join(parser.parts)).strip()
    if len(normalized) < 300:
        raise ValueError("Too little visible text. Check the rendered page manually.")
    return hashlib.sha256(normalized.encode()).hexdigest()


def probe(url):
    if not official(url):
        raise ValueError("Expected an official HTTPS documentation URL")
    with build_opener(OfficialRedirects()).open(
        Request(url, headers={"User-Agent": "FSLPowerhouseDocsMonitor/0.2"}), timeout=12
    ) as response:
        if response.headers.get_content_type() != "text/html":
            raise ValueError("Unexpected response type")
        maximum = 4_000_000
        content = response.read(maximum + 1)
        if len(content) > maximum:
            raise ValueError("Document exceeds monitor size limit")
        return fingerprint(content.decode(response.headers.get_content_charset() or "utf-8", errors="replace"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=ROOT / ".cache/source-state.json")
    parser.add_argument("--all", action="store_true", help="Check all catalog entries")
    args = parser.parse_args()
    previous = json.loads(args.state.read_text()) if args.state.exists() else {}
    current = previous.copy()
    errors = 0
    for source in json.loads((ROOT / "knowledge/sources.json").read_text()):
        if not args.all and not source.get("monitor"):
            continue
        key = source["id"]
        try:
            digest = probe(source["url"])
        except (OSError, URLError, ValueError) as exc:
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
