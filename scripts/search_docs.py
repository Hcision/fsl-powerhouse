#!/usr/bin/env python3
"""Index imported documentation sections and return bounded cited search excerpts."""
import argparse
import json
from pathlib import Path
import re
import sqlite3

from monitor_sources import ROOT

TOKEN = re.compile(r"[A-Za-z0-9_]+")


def sections(markdown):
    heading = "Overview"
    lines = []
    fenced = False
    for line in markdown.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
        if not fenced and re.match(r"^#{1,6} ", line):
            if lines:
                yield heading, "\n".join(lines).strip()
            heading, lines = line.lstrip("# ").strip(), []
        else:
            lines.append(line)
    if lines:
        yield heading, "\n".join(lines).strip()


def index(connection, directory):
    connection.execute("CREATE VIRTUAL TABLE IF NOT EXISTS docs USING fts5(heading, body, url UNINDEXED)")
    count = 0
    with connection:
        connection.execute("DELETE FROM docs")
        for sidecar in sorted(directory.glob("*.json")):
            data = json.loads(sidecar.read_text(encoding="utf-8"))
            path = sidecar.with_suffix(".md")
            if not path.is_file():
                continue
            for heading, body in sections(path.read_text(encoding="utf-8")):
                for offset in range(0, len(body), 1800):
                    connection.execute("INSERT INTO docs VALUES (?, ?, ?)",
                                       (heading, body[offset:offset + 1950], data["url"]))
                    count += 1
    return count


def search(connection, query, limit):
    words = list(dict.fromkeys(TOKEN.findall(query)))[:24]
    if not words:
        return []
    match = " OR ".join(f'"{word}"' for word in words)
    return connection.execute(
        """SELECT heading, url, snippet(docs, 1, '', '', ' … ', 45)
           FROM docs WHERE docs MATCH ? ORDER BY bm25(docs, 3, 1, 0) LIMIT ?""",
        (match, limit)).fetchall()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=ROOT / ".cache")
    parser.add_argument("--index", action="store_true")
    parser.add_argument("--limit", type=int, choices=range(1, 9), default=4)
    parser.add_argument("query", nargs="?")
    args = parser.parse_args()
    db = args.cache / "search.sqlite"
    if args.index:
        args.cache.mkdir(parents=True, exist_ok=True)
    elif not db.exists():
        parser.error("Run the importer and then search_docs.py --index first.")
    with sqlite3.connect(db) as connection:
        if args.index:
            print(f"Indexed {index(connection, args.cache / 'corpus')} sections")
        if args.query:
            matches = search(connection, args.query, args.limit)
            if not matches:
                print("No matching imported documents. Check the official live sources.")
            for heading, url, snippet in matches:
                excerpt = " ".join(snippet.split())[:750]
                print(f"{heading[:140]}\n{url}\n{excerpt}\n")
        if not args.index and not args.query:
            parser.error("Pass a query, --index, or both.")


if __name__ == "__main__":
    main()
