#!/bin/bash
# Search script using Serper.dev API
# Usage: ./search.sh "search query" [number_of_results]

API_KEY="${SERPER_API_KEY}"
QUERY="${1:-}"
NUM="${2:-10}"

if [ -z "$API_KEY" ]; then
    echo "Error: SERPER_API_KEY environment variable not set"
    echo "Please set it with: export SERPER_API_KEY='your_api_key'"
    exit 1
fi

if [ -z "$QUERY" ]; then
    echo "Usage: $0 \"search query\" [number_of_results]"
    exit 1
fi

curl -s -X POST "https://google.serper.dev/search" \
  -H "X-API-KEY: $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"q\":\"$QUERY\",\"num\":$NUM,\"hl\":\"zh-cn\",\"gl\":\"cn\"}"
