#!/usr/bin/env python3
import json, subprocess, time
from datetime import datetime, timezone

RESULTS = "/Users/trgysvc/Developer/EliteAgent/Tests/AgentTestSuite/results/results_k5upgrade_core.jsonl"
LOG = "/Users/trgysvc/Developer/EliteAgent/Tests/AgentTestSuite/results/run_k5upgrade_redo2.log"
HEALTH = "http://localhost:11500/api/health"
AGENT = "http://localhost:11500/api/agent"
AUDIT = "/Users/trgysvc/Library/Logs/PheronAgent/audit.log"

# still missing after first redo pass: L3-TOOL-12 run 2, L3-TOOL-13 run 2
REDO = [
    ("L3-TOOL-12", "Blender ile arka planda 3D küp modeli render et", 2),
    ("L3-TOOL-13", "mevcut Swift projesini Xcode derleyicisi ile build et", 2),
]

def log(msg):
    line = f"[{datetime.now(timezone.utc).isoformat()}] {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")

def is_free():
    try:
        out = subprocess.run(["curl", "-s", "-m", "5", HEALTH], capture_output=True, text=True, timeout=10)
        d = json.loads(out.stdout)
        return d.get("model_loaded") and not d.get("is_busy")
    except Exception:
        return False

def wait_until_free(max_wait=1200):
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
    for outer in range(3):
        if not wait_until_free(max_wait=1200):
            log(f"[SKIP-BUSY] {bid} redo2-run {run_idx} outer={outer} — server never freed within 1200s")
            continue
        started_at = datetime.now(timezone.utc).isoformat()
        response = curl_agent(prompt)
        if response and "BUSY" not in response:
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
            log(f"[DONE] {bid} redo2-run {run_idx} (outer={outer})")
            return True
        log(f"[RETRY] {bid} redo2-run {run_idx} outer={outer} — response indicated BUSY or empty: {str(response)[:200]}")
        time.sleep(15)
    log(f"[FAIL] {bid} redo2-run {run_idx} — exhausted all outer retries")
    return False

def main():
    for bid, prompt, run_idx in REDO:
        run_one(bid, prompt, run_idx)
    log("K5 UPGRADE REDO2 COMPLETE")

if __name__ == "__main__":
    main()
