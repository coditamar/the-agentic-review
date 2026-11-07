"""Assemble the public site from an explicit allowlist."""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_PATHS = ("index.html", ".nojekyll", "articles", "assets")


def build():
    for name in PUBLIC_PATHS:
        source = ROOT / name
        candidates = (source, *source.rglob("*")) if source.is_dir() else (source,)
        if any(path.is_symlink() for path in candidates):
            raise ValueError(f"Public sources must not contain symlinks: {name}")
    target = ROOT / "_site"
    if target.exists():
        shutil.rmtree(target)
    target.mkdir()
    for name in PUBLIC_PATHS:
        source = ROOT / name
        if source.is_dir():
            shutil.copytree(source, target / name)
        else:
            shutil.copy2(source, target / name)
    return target


if __name__ == "__main__":
    print(f"Public site assembled in {build().name}/")
