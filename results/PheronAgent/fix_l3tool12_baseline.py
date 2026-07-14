#!/usr/bin/env python3
import json, subprocess, time
from datetime import datetime, timezone

RESULTS = "/Users/trgysvc/Developer/EliteAgent/Tests/AgentTestSuite/results/results_2026-07-09_v2_backup.jsonl"
LOG = "/Users/trgysvc/Developer/EliteAgent/Tests/AgentTestSuite/results/fix_l3tool12_baseline.log"
HEALTH = "http://localhost:11500/api/health"
AGENT = "http://localhost:11500/api/agent"
AUDIT = "/Users/trgysvc/Library/Logs/PheronAgent/audit.log"

PROMPT = "Blender ile arka planda 3D küp modeli render et"
TARGET_RUNS = [2]  # run 1 already fixed; only run 2 still corrupted

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

def audit_line_count():
    try:
        out = subprocess.run(["wc", "-l", AUDIT], capture_output=True, text=True, timeout=10)
        return int(out.stdout.strip().split()[0])
    except Exception:
        return 0

def audit_slice(start_line):
    try:
        out = subprocess.run(["tail", "-n", f"+{start_line+1}", AUDIT], capture_output=True, text=True, timeout=10)
        return out.stdout
    except Exception:
        return ""

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

def run_one(run_idx):
    for outer in range(3):
        if not wait_until_free(max_wait=1200):
            log(f"[SKIP-BUSY] L3-TOOL-12 fix-run {run_idx} outer={outer} — server never freed")
            continue
        start_line = audit_line_count()
        started_at = datetime.now(timezone.utc).isoformat()
        response = curl_agent(PROMPT)
        if response and response.strip() and "BUSY" not in response:
            audit_excerpt = audit_slice(start_line)
            record = {
                "id": "L3-TOOL-12",
                "run": run_idx,
                "k": 3,
                "started_at": started_at,
                "turns": [{"prompt": PROMPT, "response": response, "audit_excerpt": audit_excerpt}],
            }
            log(f"[DONE] L3-TOOL-12 fix-run {run_idx} (outer={outer})")
            return record
        log(f"[RETRY] L3-TOOL-12 fix-run {run_idx} outer={outer} — empty/BUSY response: {str(response)[:200]}")
        time.sleep(15)
    log(f"[FAIL] L3-TOOL-12 fix-run {run_idx} — exhausted retries")
    return None

def main():
    new_records = {}
    for run_idx in TARGET_RUNS:
        rec = run_one(run_idx)
        if rec:
            new_records[run_idx] = rec

    # Rewrite the results file: replace old L3-TOOL-12 run 1/2 lines with new clean ones, leave everything else untouched
    lines_out = []
    with open(RESULTS) as f:
        for line in f:
            try:
                d = json.loads(line)
            except Exception:
                lines_out.append(line.rstrip("\n"))
                continue
            if d.get("id") == "L3-TOOL-12" and d.get("run") in new_records:
                lines_out.append(json.dumps(new_records[d["run"]], ensure_ascii=False))
                del new_records[d["run"]]  # mark replaced
            else:
                lines_out.append(json.dumps(d, ensure_ascii=False))

    with open(RESULTS, "w") as f:
        for line in lines_out:
            f.write(line + "\n")

    if new_records:
        log(f"[WARN] Could not find original lines to replace for runs: {list(new_records.keys())}")
    log("L3-TOOL-12 BASELINE FIX COMPLETE")

if __name__ == "__main__":
    main()
