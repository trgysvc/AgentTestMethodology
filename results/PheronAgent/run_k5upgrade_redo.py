#!/usr/bin/env python3
import json, subprocess, time
from datetime import datetime, timezone

RESULTS = "/Users/trgysvc/Developer/EliteAgent/Tests/AgentTestSuite/results/results_k5upgrade_core.jsonl"
LOG = "/Users/trgysvc/Developer/EliteAgent/Tests/AgentTestSuite/results/run_k5upgrade_redo.log"
HEALTH = "http://localhost:11500/api/health"
AGENT = "http://localhost:11500/api/agent"
AUDIT = "/Users/trgysvc/Library/Logs/PheronAgent/audit.log"

# (id, prompt, run_idx) — the 5 runs that were contaminated (BUSY) or skipped last time
REDO = [
    ("L3-TOOL-12", "Blender ile arka planda 3D küp modeli render et", 1),
    ("L3-TOOL-12", "Blender ile arka planda 3D küp modeli render et", 2),
    ("L3-TOOL-13", "mevcut Swift projesini Xcode derleyicisi ile build et", 1),
    ("L3-TOOL-13", "mevcut Swift projesini Xcode derleyicisi ile build et", 2),
    ("L3-TOOL-14", "sistemdeki mevcut kestirmeleri listele", 1),
]

def log(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")

def is_free():
    try:
        out = subprocess.run(["curl", "-s", "-m", "5", HEALTH], capture_output=True, text=True, timeout=10)
        d = json.loads(out.stdout)
        return d.get("model_loaded") and not d.get("is_busy")
    except Exception:
        return False

def wait_until_free(max_wait=900):
    start = time.time()
    while time.time() - start < max_wait:
        if is_free():
            return True
        time.sleep(5)
    return False

def curl_agent(prompt, timeout=280):
    body = json.dumps({"prompt": prompt})
    try:
        out = subprocess.run(
            ["curl", "-s", "-m", str(timeout), "-X", "POST", AGENT,
             "-H", "Content-Type: application/json", "-d", body],
            capture_output=True, text=True, timeout=timeout + 20
        )
        return out.stdout
    except subprocess.TimeoutExpired:
        return json.dumps({"error": "CLIENT_TIMEOUT"})

def get_audit_excerpt(nlines=15):
    try:
        out = subprocess.run(["tail", "-n", str(nlines), AUDIT], capture_output=True, text=True, timeout=10)
        return out.stdout
    except Exception:
        return ""

def run_one(bid, prompt, run_idx):
    if not wait_until_free():
        log(f"[SKIP-BUSY] {bid} redo-run {run_idx} — server never freed")
        return False
    started_at = datetime.now(timezone.utc).isoformat()
    response = None
    for attempt in range(4):
        response = curl_agent(prompt)
        if response and "BUSY" not in response:
            break
        time.sleep(10)
    if response is None or "BUSY" in response:
        log(f"[SKIP-STILL-BUSY] {bid} redo-run {run_idx} — all retries returned BUSY")
        return False
    audit_excerpt = get_audit_excerpt()
    record = {
        "id": bid,
        "run": run_idx,
        "k_added": 2,
        "started_at": started_at,
        "turns": [{"prompt": prompt, "response": response, "audit_excerpt": audit_excerpt}],
    }
    with open(RESULTS, "a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    log(f"[DONE] {bid} redo-run {run_idx}")
    return True

def main():
    for bid, prompt, run_idx in REDO:
        run_one(bid, prompt, run_idx)
    log("K5 UPGRADE REDO COMPLETE")

if __name__ == "__main__":
    main()
