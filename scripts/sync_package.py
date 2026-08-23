#!/usr/bin/env python3
"""Drop a freshly built .ipk/.deb into the upload repo, replacing the old
version of the same package and updating the addons manifest / listing
files."""
import argparse
import json
import re
import shutil
import sys
from pathlib import Path

# Fallback location when no prior version of a package exists anywhere in
# the repo yet, keyed by package extension (oe2.0 ships .ipk, oe2.5 .deb).
FALLBACK_DIR = {
    "ipk": "oe2.0/lululla",
    "deb": "oe2.5/varius",
}


def fmt_size(n: int) -> str:
    if n < 1024:
        return f"{n:.1f}B"
    if n < 1024 ** 2:
        return f"{n / 1024:.1f}KB"
    return f"{n / 1024 ** 2:.1f}MB"


def find_matches(upload_dir: Path, package: str, arch: str, ext: str):
    pattern = re.compile(rf"^{re.escape(package)}_.+_{re.escape(arch)}\.{re.escape(ext)}$")
    return [p for p in upload_dir.rglob(f"*.{ext}") if pattern.match(p.name)]


def update_addons_xml(upload_dir: Path, old_name: str, new_name: str) -> bool:
    xml_path = upload_dir / "fill" / "addons_2024.xml"
    if not xml_path.exists() or old_name == new_name:
        return False
    text = xml_path.read_text(encoding="utf-8")
    if old_name not in text:
        return False
    xml_path.write_text(text.replace(old_name, new_name), encoding="utf-8")
    return True


def update_listing_txt(upload_dir: Path, rel_dir: Path, old_name: str, new_name: str, new_size: int) -> bool:
    top = rel_dir.parts[0]  # oe2.0 or oe2.5
    txt_path = upload_dir / f"GitHub_upload_{top}.txt"
    if not txt_path.exists() or old_name == new_name:
        return False
    lines = txt_path.read_text(encoding="utf-8").splitlines(keepends=True)
    pattern = re.compile(rf"^{re.escape(old_name)} \(.*\)\s*$")
    for i, line in enumerate(lines):
        if pattern.match(line):
            lines[i] = f"{new_name} ({fmt_size(new_size)})\n"
            txt_path.write_text("".join(lines), encoding="utf-8")
            return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pkg", required=True, help="path to a freshly built .ipk or .deb")
    ap.add_argument("--upload-dir", required=True, help="path to upload repo checkout")
    args = ap.parse_args()

    pkg_path = Path(args.pkg)
    manifest_path = Path(str(pkg_path) + ".manifest.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    package, arch, new_name, ext = (
        manifest["package"], manifest["arch"], manifest["filename"], manifest["ext"]
    )
    upload_dir = Path(args.upload_dir)

    matches = find_matches(upload_dir, package, arch, ext)
    new_size = pkg_path.stat().st_size

    if not matches:
        dest_dir = upload_dir / FALLBACK_DIR[ext]
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / new_name
        shutil.copy2(pkg_path, dest)
        print(f"NEW: {package} -> {dest.relative_to(upload_dir)} (no prior version found, placed in fallback dir)")
        return

    for old_path in matches:
        old_name = old_path.name
        rel_dir = old_path.parent.relative_to(upload_dir)
        dest = old_path.parent / new_name
        if old_name == new_name:
            print(f"SAME: {package} already at {new_name} in {rel_dir}, overwriting bytes")
        old_path.unlink()
        shutil.copy2(pkg_path, dest)

        xml_updated = update_addons_xml(upload_dir, old_name, new_name)
        txt_updated = update_listing_txt(upload_dir, rel_dir, old_name, new_name, new_size)

        print(f"UPDATED: {rel_dir}/{old_name} -> {new_name} "
              f"(addons_2024.xml {'updated' if xml_updated else 'unchanged'}, "
              f"GitHub_upload_{rel_dir.parts[0]}.txt {'updated' if txt_updated else 'unchanged'})")


if __name__ == "__main__":
    sys.exit(main())
