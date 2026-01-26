#!/bin/bash
# Fetch web content using lynx (recommended method)
# Usage: ./fetch_content.sh "URL"

URL="${1:-}"

if [ -z "$URL" ]; then
    echo "Usage: $0 \"URL\""
    exit 1
fi

# Check if lynx is installed
if command -v lynx &> /dev/null; then
    lynx -dump -nolist -hiddenlinks=ignore "$URL"
elif command -v curl &> /dev/null && command -v pandoc &> /dev/null; then
    # Fallback to curl + pandoc
    curl -s "$URL" | pandoc -f html -t markdown
else
    echo "Error: Neither lynx nor pandoc is installed"
    echo "Install with: brew install lynx pandoc"
    exit 1
fi
