#!/usr/bin/env bash
# v47: Snapshot + clear PheronAgent's persistent memory stores before a memory-recall test batch
# (MT-04, L2/L3-BELLEK-*), so those tests get a genuinely clean slate instead of reading real,
# long-lived personal facts (CV data, past sessions, ...) accumulated from actual usage.
# Confirmed root cause: MT-04 asked "what do you know about me?" mid-batch and got told its city
# was "Ankara" — sourced not from test contamination alone but from the REAL user's real CV
# (analyzed weeks earlier) plus the SAME batch's own L3-BELLEK-02 run, both legitimately-tagged
# entries in the persistent ExperienceVault. No code fix can or should suppress genuinely-true
# personal-memory recall — the fix has to be test isolation, not agent behavior.
#
# MUST be paired with restore_memory_after_test.sh at the end of the batch. Never run a memory-
# sensitive test batch with this script without restoring afterward — this deletes the live
# vault/notes/profile files (after backing them up first).
#
# Usage: ./reset_memory_for_test.sh
# Requires: PheronAgent.app must be QUIT before running this (it holds the sqlite file open).

set -euo pipefail

APP_SUPPORT="$HOME/Library/Application Support/PheronAgent"
BACKUP_MARKER="$APP_SUPPORT/.test_memory_backup_current"

if [ -f "$BACKUP_MARKER" ]; then
    echo "ERROR: a backup marker already exists at $BACKUP_MARKER — a previous reset was never" >&2
    echo "restored. Run restore_memory_after_test.sh first, or investigate manually before" >&2
    echo "overwriting it (doing so risks losing the earlier backup)." >&2
    exit 1
fi

if pgrep -f "PheronAgent.app/Contents/MacOS/PheronAgent" > /dev/null 2>&1; then
    echo "ERROR: PheronAgent is currently running — quit it first so the sqlite file isn't" >&2
    echo "open/locked during the copy, and so the app doesn't write to it mid-backup." >&2
    exit 1
fi

BACKUP_DIR="$APP_SUPPORT/.test_memory_backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

ITEMS=(experience_vault.sqlite memory session_summaries.plist KNOWLEDGE_BASE_public.md UserProfile.md)
for item in "${ITEMS[@]}"; do
    if [ -e "$APP_SUPPORT/$item" ]; then
        cp -R "$APP_SUPPORT/$item" "$BACKUP_DIR/"
    fi
done

# Verify every existing source item was actually copied before touching anything live.
for item in "${ITEMS[@]}"; do
    if [ -e "$APP_SUPPORT/$item" ] && [ ! -e "$BACKUP_DIR/$item" ]; then
        echo "ERROR: backup verification failed for '$item' — aborting before any deletion." >&2
        rm -rf "$BACKUP_DIR"
        exit 1
    fi
done

echo "$BACKUP_DIR" > "$BACKUP_MARKER"
echo "Backed up to: $BACKUP_DIR"

for item in "${ITEMS[@]}"; do
    rm -rf "${APP_SUPPORT:?}/$item"
done
mkdir -p "$APP_SUPPORT/memory"

echo "Memory state cleared (vault/daily-notes/session-summaries/KB/profile)."
echo "Restart PheronAgent.app now to run tests against a clean slate."
echo "When the batch is done: quit the app, then run restore_memory_after_test.sh."
