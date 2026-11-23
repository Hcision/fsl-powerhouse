#!/usr/bin/env python3
"""Discover official pages by following links in sf-docs Markdown output."""
import argparse
from datetime import datetime, timezone
import hashlib
import shutil
from collections import deque
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit

from monitor_sources import ROOT, official

LINK = re.compile(r"\]\(<?([^\s)>]+)>?(?:\s+[\"'][^)]*[\"'])?\)")
TRACKING = {"utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"}


def canonical(base, target):
    if target.startswith("#"):
        return None
    parts = urlsplit(urljoin(base, target))
    query = urlencode(sorted((k, v) for k, v in parse_qsl(parts.query) if k not in TRACKING))
    url = urlunsplit((parts.scheme, parts.netloc, parts.path, query, ""))
    if not official(url):
        return None
    if parts.netloc == "help.salesforce.com":
        return url if parts.path == "/s/articleView" and "id" in dict(parse_qsl(query)) else None
    if parts.netloc == "developer.salesforce.com":
        return url if parts.path.startswith("/docs/") else None
    if parts.netloc == "architect.salesforce.com":
        return url if parts.path.startswith(("/docs/", "/well-architected/", "/diagrams/")) else None
    if parts.netloc == "trailhead.salesforce.com":
        return url if parts.path.startswith("/content/learn/") else None
    return None


def discover(seeds, fetch, limit, depth):
    visited = set(seeds)
    pending = deque((url, 0, None) for url in seeds)
    results = []
    while pending and len(results) < limit:
        url, level, parent = pending.popleft()
        row = {"url": url, "depth": level, "discovered_from": parent}
        try:
            markdown = fetch(url)
            if not markdown.strip():
                raise ValueError("Empty Markdown output")
            row["status"] = "fetched"
            if level < depth:
                for match in LINK.finditer(markdown):
                    target = canonical(url, match[1])
                    if target and target not in visited:
                        visited.add(target)
                        pending.append((target, level + 1, url))
        except (OSError, subprocess.SubprocessError, ValueError) as error:
            row.update(status="failed", error=str(error))
        results.append(row)
    return {"results": results, "queued": len(pending)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", action="append", help="Official page to start from. Repeat as needed.")
    parser.add_argument("--toc", action="append", default=[],
                        help="Developer documentation deliverable or guide ID to enumerate")
    parser.add_argument("--refresh", action="store_true", help="Refetch already imported pages")
    parser.add_argument("--limit", type=int, default=30, help="Maximum fetch attempts per run")
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--output", type=Path, default=ROOT / ".cache/discovery.json")
    args = parser.parse_args()
    if shutil.which("sf-docs") is None:
        parser.error("Install sf-docs and add it to PATH before importing.")
    if args.limit < 1 or args.depth < 0:
        parser.error("Use a positive limit and nonnegative depth")
    catalog = json.loads((ROOT / "knowledge/sources.json").read_text())
    urls = args.seed or [row["url"] for row in catalog if row["topic"].startswith("fsl-")]
    for target in args.toc:
        root = "https://developer.salesforce.com/docs/"
        if "/" not in target:
            root += f"atlas.en-us.{target}.meta/{target}/"
        else:
            root += target.strip("/") + "/"
        try:
            result = subprocess.run(["sf-docs", "--format", "json", "toc", target, "--depth", "3"],
                                    capture_output=True, text=True, check=True, timeout=120)
            urls.extend(url for entry in json.loads(result.stdout)
                        if (url := canonical(root, entry.get("href") or "#")))
        except (OSError, subprocess.SubprocessError, ValueError) as error:
            parser.error(f"Could not enumerate {target}: {error}")
    seeds = list(dict.fromkeys(canonical(url, url) for url in urls))
    if None in seeds:
        parser.error("Every seed must be an official supported Salesforce documentation page")
    corpus = args.output.parent / "corpus"

    def fetch(url):
        key = hashlib.sha256(url.encode()).hexdigest()
        markdown = corpus / (key + ".md")
        metadata = corpus / (key + ".json")
        if not args.refresh and markdown.is_file() and metadata.is_file():
            return markdown.read_text(encoding="utf-8")
        command = ["sf-docs", "--format", "md"]
        if args.refresh:
            command.append("--no-cache")
        result = subprocess.run([*command, "fetch", url], capture_output=True, text=True, timeout=90)
        if result.returncode:
            lines = result.stderr.strip().splitlines()
            raise ValueError(lines[0][:350] if lines else f"sf-docs exited {result.returncode}")
        if result.stdout.strip():
            corpus.mkdir(parents=True, exist_ok=True)
            markdown.write_text(result.stdout, encoding="utf-8")
            metadata.write_text(json.dumps({
                "url": url, "retrieved_at": datetime.now(timezone.utc).isoformat(),
            }), encoding="utf-8")
        return result.stdout

    report = discover(seeds, fetch, args.limit, args.depth)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    count = sum(row["status"] == "fetched" for row in report["results"])
    print(f"Fetched {count}/{len(report['results'])} attempted pages, {report['queued']} unvisited discovered URLs")
    return int(count == 0)


if __name__ == "__main__":
    raise SystemExit(main())
