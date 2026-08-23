#!/usr/bin/env bash
# Build both an Enigma2 .ipk (opkg, gzip) and a .deb (dpkg, xz) from a
# plugin repo checkout. Both packages are built from the same
# CONTROL/{control,preinst,postinst,postrm} + usr/... tree — they only
# differ in compression, matching what opkg (oe2.0) and dpkg (oe2.5)
# actually expect.
set -euo pipefail

SRC_DIR="${1:?usage: build_ipk.sh <repo_dir> <out_dir>}"
OUT_DIR="${2:?usage: build_ipk.sh <repo_dir> <out_dir>}"

CONTROL_FILE="$SRC_DIR/CONTROL/control"
[ -f "$CONTROL_FILE" ] || { echo "no CONTROL/control in $SRC_DIR" >&2; exit 1; }

# usr/ normally sits at the repo root alongside CONTROL/, but a few repos
# nest it one level down (e.g. XStreamity/usr/). Tolerate that instead of
# failing the build.
if [ -d "$SRC_DIR/usr" ]; then
  DATA_ROOT="$SRC_DIR"
else
  DATA_ROOT=$(find "$SRC_DIR" -mindepth 2 -maxdepth 2 -type d -name usr -printf '%h\n' 2>/dev/null | head -1)
  [ -n "$DATA_ROOT" ] || { echo "no usr/ tree in $SRC_DIR (checked root and one level down)" >&2; exit 1; }
fi

PKG=$(awk -F': ' '/^Package:/{print $2; exit}' "$CONTROL_FILE" | tr -d '\r')
VER=$(awk -F': ' '/^Version:/{print $2; exit}' "$CONTROL_FILE" | tr -d '\r')
ARCH=$(awk -F': ' '/^Architecture:/{print $2; exit}' "$CONTROL_FILE" | tr -d '\r')

[ -n "$PKG" ] && [ -n "$VER" ] && [ -n "$ARCH" ] || { echo "control file missing Package/Version/Architecture" >&2; exit 1; }

WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

mkdir -p "$OUT_DIR"
echo "2.0" > "$WORK/debian-binary"

build_one() {
  local ext="$1" compress="$2" tar_flag="$3"
  local filename="${PKG}_${VER}_${ARCH}.${ext}"
  local out_file="$OUT_DIR/$filename"

  tar --numeric-owner --owner=0 --group=0 "$tar_flag" -C "$SRC_DIR/CONTROL" -cf "$WORK/control.tar.$compress" .
  tar --numeric-owner --owner=0 --group=0 "$tar_flag" -C "$DATA_ROOT" -cf "$WORK/data.tar.$compress" usr

  rm -f "$out_file"
  ar rc "$out_file" "$WORK/debian-binary" "$WORK/control.tar.$compress" "$WORK/data.tar.$compress"
  rm -f "$WORK/control.tar.$compress" "$WORK/data.tar.$compress"

  cat > "$OUT_DIR/$filename.manifest.json" <<JSON
{
  "package": "$PKG",
  "version": "$VER",
  "arch": "$ARCH",
  "filename": "$filename",
  "ext": "$ext"
}
JSON
  echo "built: $out_file"
}

build_one ipk gz -z
build_one deb xz -J
