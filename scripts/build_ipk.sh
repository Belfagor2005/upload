#!/usr/bin/env bash
# Build an Enigma2 .ipk (opkg/ar package) from a plugin repo checkout.
# Expected repo layout: CONTROL/{control,preinst,postinst,postrm} + usr/...
set -euo pipefail

SRC_DIR="${1:?usage: build_ipk.sh <repo_dir> <out_dir>}"
OUT_DIR="${2:?usage: build_ipk.sh <repo_dir> <out_dir>}"

CONTROL_FILE="$SRC_DIR/CONTROL/control"
[ -f "$CONTROL_FILE" ] || { echo "no CONTROL/control in $SRC_DIR" >&2; exit 1; }
[ -d "$SRC_DIR/usr" ] || { echo "no usr/ tree in $SRC_DIR" >&2; exit 1; }

PKG=$(awk -F': ' '/^Package:/{print $2; exit}' "$CONTROL_FILE" | tr -d '\r')
VER=$(awk -F': ' '/^Version:/{print $2; exit}' "$CONTROL_FILE" | tr -d '\r')
ARCH=$(awk -F': ' '/^Architecture:/{print $2; exit}' "$CONTROL_FILE" | tr -d '\r')

[ -n "$PKG" ] && [ -n "$VER" ] && [ -n "$ARCH" ] || { echo "control file missing Package/Version/Architecture" >&2; exit 1; }

WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

echo "2.0" > "$WORK/debian-binary"
tar --numeric-owner --owner=0 --group=0 -C "$SRC_DIR/CONTROL" -czf "$WORK/control.tar.gz" .
tar --numeric-owner --owner=0 --group=0 -C "$SRC_DIR" -czf "$WORK/data.tar.gz" usr

FILENAME="${PKG}_${VER}_${ARCH}.ipk"
OUT_FILE="$OUT_DIR/$FILENAME"
mkdir -p "$OUT_DIR"
rm -f "$OUT_FILE"
ar rc "$OUT_FILE" "$WORK/debian-binary" "$WORK/control.tar.gz" "$WORK/data.tar.gz"

cat > "$OUT_DIR/$FILENAME.manifest.json" <<JSON
{
  "package": "$PKG",
  "version": "$VER",
  "arch": "$ARCH",
  "filename": "$FILENAME"
}
JSON

echo "built: $OUT_FILE"
