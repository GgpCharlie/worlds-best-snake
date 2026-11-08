#!/usr/bin/env bash
# Starts a tiny local web server so you can test the games in your browser.
# The 3D games won't open by double-clicking the file — browsers need a real
# web address for them. That's normal, and it works fine on the live site.
#
# Usage:  ./serve.sh
# Then open:  http://localhost:8000
# Stop it with Ctrl+C.
cd "$(dirname "$0")"
PORT="${1:-8000}"
echo ""
echo "  t54w is running! Open this in your browser:"
echo "    http://localhost:$PORT"
echo "  (Ctrl+C to stop)"
echo ""
python3 -m http.server "$PORT"
