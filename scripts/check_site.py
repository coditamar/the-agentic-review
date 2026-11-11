"""Check publication structure and local references without network access."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys
import re
import xml.etree.ElementTree as ET

from build_site import ROOT, build


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.references = []
        self.counts = Counter()
        self.errors = []
        self.canonical = []
        self.lang = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.counts[tag] += 1
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "img" and "alt" not in attrs:
            self.errors.append("image missing alt attribute")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href", ""))
        for key in ("href", "src", "srcset"):
            if key in attrs:
                self.references.append(attrs[key])


def check():
    root = build()
    pages = {path: Page(path.read_text()) for path in root.rglob("*.html")}
    errors = []
    site_url = "https://coditamar.github.io/the-agentic-review/"
    for path, page in pages.items():
        label = str(path.relative_to(root))
        for error in page.errors:
            errors.append(f"{label}: {error}")
        for tag in ("h1", "main", "title"):
            if page.counts[tag] != 1:
                errors.append(f"{label}: expected one {tag}")
        if page.lang != "en":
            errors.append(f"{label}: expected English document language")
        if len(page.ids) != len(set(page.ids)):
            errors.append(f"{label}: duplicate IDs")
        suffix = "" if path.name == "index.html" else label
        if page.canonical != [site_url + suffix]:
            errors.append(f"{label}: missing or incorrect canonical URL")
        for reference in page.references:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                if url.scheme not in ("https", "mailto"):
                    errors.append(f"{label}: unsupported external URL {reference}")
                continue
            if url.path.startswith("/"):
                errors.append(f"{label}: root-relative URL breaks project hosting: {reference}")
                continue
            dest = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not dest.is_relative_to(root):
                errors.append(f"{label}: link escapes public site: {reference}")
                continue
            if dest.is_dir():
                dest /= "index.html"
            if not dest.is_file():
                errors.append(f"{label}: missing local target {reference}")
            elif url.fragment and dest in pages and unquote(url.fragment) not in pages[dest].ids:
                errors.append(f"{label}: missing fragment {reference}")
    for path in root.rglob("*"):
        if path.is_symlink():
            errors.append(f"symlink in public output: {path.name}")
        if path.is_file() and path.suffix not in (".html", ".css", ".svg", ".png", ".jpg", ".webp", ".ico", ".pdf") and path.name != ".nojekyll":
            errors.append(f"unexpected public file: {path.relative_to(root)}")
        if path.suffix == ".svg":
            try:
                ET.parse(path)
            except ET.ParseError as error:
                errors.append(f"invalid SVG: {path.name}: {error}")
    # Inspect both public content and files visible in the repository, not just linked pages.
    # These checks catch common publication mistakes; an editorial review is still required.
    blocked = (
        ("private conversation link", re.compile(r"https?://[^\s\"<>]*slack\.com/(?:archives|files)/", re.I)),
        ("local filesystem path", re.compile(r"(?:/Users/|/home/|file:///)", re.I)),
        ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
        ("service credential", re.compile(r"(?:sk-(?:proj-|svcacct-)[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{30,}|xox[baprs]-[A-Za-z0-9-]{20,})")),
        ("implementation assessment", re.compile(r"implementation[-_ ]status", re.I)),
    )
    for source in ROOT.rglob("*"):
        relative = source.relative_to(ROOT)
        if any(part in {".git", "_site", "__pycache__", ".qodo"} for part in relative.parts):
            continue
        if source.is_symlink():
            errors.append(f"symlink in repository: {relative}")
            continue
        if not source.is_file():
            continue
        if re.search(r"implementation[-_ ]status", source.name, re.I):
            errors.append(f"implementation assessment asset: {relative}")
        if source.suffix in {".html", ".svg", ".css", ".md", ".json", ".txt"}:
            content = source.read_text()
            for label, pattern in blocked:
                if pattern.search(content):
                    errors.append(f"{relative}: {label}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Site checks passed: {len(pages)} pages; local links, fragments, canonical URLs, images, preview allowlist, and publication boundary scan.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
