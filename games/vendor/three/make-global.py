#!/usr/bin/env python3
"""Build three.global.js from three.module.js (Three.js r160, MIT licensed).

Browsers refuse to run ES modules opened straight from disk (file://), so the
3D games load Three.js the old-fashioned way instead: a plain script that
sets window.THREE. This script just re-wraps the official module build — the
code itself is untouched, only the export block at the end changes.

Run from this folder:  python3 make-global.py
"""
import re, pathlib

here = pathlib.Path(__file__).parent
src = (here / "three.module.js").read_text(encoding="utf-8")

# Safety checks: the official build has exactly one export at the very end
# and no import statements anywhere. If that ever changes, this script must change too.
assert src.count("export {") == 1, "unexpected layout in three.module.js — not converting"
assert not re.search(r"import\s*[{*(]", src), "found a real import statement in three.module.js — not converting"

m = re.search(r"export \{([^}]*)\};\s*$", src)
exports = []
for item in m.group(1).split(","):
    item = item.strip()
    if not item:
        continue
    if " as " in item:
        local, public = [p.strip() for p in item.split(" as ")]
    else:
        local = public = item
    exports.append(f"{public}:{local}")
body = src[:m.start()].rstrip()

out = (
    "/**\n"
    " * three.global.js — generated from three.module.js (Three.js r160) by make-global.py.\n"
    " * Same MIT-licensed Three.js, wrapped as a classic script so games also work when\n"
    " * opened straight from disk (file://). Do not edit by hand — regenerate instead.\n"
    " */\n"
    + body
    + "\n\nglobalThis.THREE = {" + ",".join(exports) + "};\n})();\n"
)
# wrap everything (after the license headers) in a strict-mode IIFE,
# so it keeps the same rules ES modules use
head_end = out.index("*/", out.index("@license")) + 2
# insert IIFE open right after the existing top license comment block
iife_open = "\n(function(){\"use strict\";\n"
line_end = out.index("\n", head_end)
out = out[:line_end] + iife_open + out[line_end+1:]

(here / "three.global.js").write_text(out, encoding="utf-8")
print(f"wrote three.global.js — {len(exports)} exports, {len(out)} bytes")
