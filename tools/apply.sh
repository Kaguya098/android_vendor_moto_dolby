#!/bin/bash
# usage: tools/apply.sh <device_tree_dir>   (folder yang berisi audio_effects.xml & media_codecs.xml)
set -e
D="${1:?device tree dir}"; T="$(dirname "$0")"
for f in $(find "$D" -name 'audio_effects*.xml'); do python3 "$T/patch_audio_effects.py" "$f"; done
for f in $(find "$D" -name 'media_codecs.xml' -o -name 'media_codecs_*.xml' | grep -v dolby | head -1); do
  grep -q media_codecs_dolby_audio "$f" || sed -i 's#</MediaCodecs>#    <Include href="media_codecs_dolby_audio.xml" />\n</MediaCodecs>#' "$f"
  echo "include ditambah ke $f"
done
