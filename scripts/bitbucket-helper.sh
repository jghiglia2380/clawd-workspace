#!/bin/bash
# Bitbucket API Helper for Thomas
# Usage: ./bitbucket-helper.sh <action> [path]
# Actions: ls, cat, search, tree

BB_USER="justin@pflacademy.co"
BB_TOKEN="ATATT3xFfGF05DKULGmvFpyjGks8n5NtyTHFrkfN7squDVGO2J-uosi4rBvH4Rqz9tEOBkItM7HBfq96dd0GD0bDIP2ZsiWp70lNx-7MUKNAp875F-lJ31knuikKvYk8RPMeu772cVydAtwldFGkrGeEsnwZz7CpG-odwsexLJgPl84O68igDrI=9F057656"
BB_AUTH="$BB_USER:$BB_TOKEN"
REPO="sebastian_lucaciu/pfl-academy"
BRANCH="master"

ACTION=$1
shift

case $ACTION in
    ls)
        # List directory contents
        PATH_ARG=${1:-""}
        curl -s --max-time 15 -u "$BB_AUTH" "https://api.bitbucket.org/2.0/repositories/$REPO/src/$BRANCH/$PATH_ARG" | jq '.values[] | {path: .path, type: .type, size: .size}'
        ;;
    cat)
        # Get file contents
        FILE_PATH=$1
        curl -s --max-time 15 -u "$BB_AUTH" "https://api.bitbucket.org/2.0/repositories/$REPO/src/$BRANCH/$FILE_PATH"
        ;;
    search)
        # Search for files by name pattern
        PATTERN=$1
        curl -s --max-time 30 -u "$BB_AUTH" "https://api.bitbucket.org/2.0/repositories/$REPO/src/$BRANCH/?max_depth=10" | jq -r '.values[].path' | grep -i "$PATTERN"
        ;;
    commits)
        # Recent commits
        COUNT=${1:-10}
        curl -s --max-time 15 -u "$BB_AUTH" "https://api.bitbucket.org/2.0/repositories/$REPO/commits?pagelen=$COUNT" | jq '.values[] | {date: .date[0:10], author: .author.raw, message: .message[0:80]}'
        ;;
    *)
        echo "Usage: ./bitbucket-helper.sh <action> [args]"
        echo "Actions:"
        echo "  ls [path]       - List directory contents"
        echo "  cat <file>      - Get file contents"
        echo "  search <pattern> - Search for files"
        echo "  commits [count] - Recent commits"
        ;;
esac
