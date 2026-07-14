#!/usr/bin/env bash
# v47: Restores the real memory state backed up by reset_memory_for_test.sh. See that script's
# header for why this pair exists. Never skip this after a memory-sensitive test batch — the
# live vault/notes/profile stay in the test-cleared state until this runs.
#
# Usage: ./restore_memory_after_test.sh
# Requires: PheronAgent.app must be QUIT before running this.

set -euo pipefail

APP_SUPPORT="$HOME/Library/Application Support/PheronAgent"
BACKUP_MARKER="$APP_SUPPORT/.test_memory_backup_current"

if [ ! -f "$BACKUP_MARKER" ]; then
    echo "ERROR: no backup marker found at $BACKUP_MARKER — nothing to restore. Aborting to" >&2
    echo "avoid accidentally wiping current state with an empty restore." >&2
    exit 1
fi

if pgrep -f "PheronAgent.app/Contents/MacOS/PheronAgent" > /dev/null 2>&1; then
    echo "ERROR: PheronAgent is currently running — quit it first." >&2
    exit 1
fi

BACKUP_DIR=$(cat "$BACKUP_MARKER")
if [ ! -d "$BACKUP_DIR" ]; then
    echo "ERROR: backup dir '$BACKUP_DIR' (from marker) does not exist. Aborting — investigate" >&2
    echo "manually before removing the marker." >&2
    exit 1
fi

ITEMS=(experience_vault.sqlite memory session_summaries.plist KNOWLEDGE_BASE_public.md UserProfile.md)
for item in "${ITEMS[@]}"; do
    rm -rf "${APP_SUPPORT:?}/$item"
done
for item in "${ITEMS[@]}"; do
    if [ -e "$BACKUP_DIR/$item" ]; then
        cp -R "$BACKUP_DIR/$item" "$APP_SUPPORT/"
    fi
done

rm -rf "$BACKUP_DIR"
rm -f "$BACKUP_MARKER"

echo "Memory state restored from backup. Restart PheronAgent.app for normal use."
