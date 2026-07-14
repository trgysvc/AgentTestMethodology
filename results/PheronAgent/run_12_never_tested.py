#!/usr/bin/env python3
import json, subprocess, time
from datetime import datetime, timezone

RESULTS = "/Users/trgysvc/Developer/EliteAgent/Tests/AgentTestSuite/results/results_12_never_tested.jsonl"
LOG = "/Users/trgysvc/Developer/EliteAgent/Tests/AgentTestSuite/results/run_12_never_tested.log"
HEALTH = "http://localhost:11500/api/health"
AGENT = "http://localhost:11500/api/agent"
AUDIT = "/Users/trgysvc/Library/Logs/PheronAgent/audit.log"

TESTS = [
    ("L3-TOOL-17", "Notion'da yeni bir toplantı notu sayfası oluştur", 103),
    ("L3-TOOL-18", "Higgsfield kullanarak 'dalgalı denizde giden gemi' videosu üret", 87),
    ("EK-TOOL-20", "Bu haftaki takvim etkinliklerimi ve toplantılarımı listele", 21),
    ("EK-TOOL-21", "Eski e-posta arşivimdeki 'Rapor' konulu mailleri kontrol et", 22),
    ("EK-TOOL-22", "Messenger üzerinden Can'a '10 dakika içinde oradayım' yaz", 37),
    ("EK-TOOL-23", "Masaüstünü Temizle kestirmesini (shortcut) çalıştır", 49),
    ("EK-TOOL-24", "MCP git aracını kullanarak bu projedeki aktif değişiklikleri listele", 96),
    ("EK-TOOL-25", "MCP bellek aracını kullanarak 'Turgay Swift geliştiricisidir' bilgisini kalıcı hafızaya ekle", 97),
    ("EK-TOOL-26", "MCP tarayıcı aracı ile apple.com/newsroom adresine git ve son başlığı getir", 98),
    ("EK-TOOL-27", "Perplexity aracıyla Apple M4 Ultra çipinin çıkış tarihi hakkındaki son haberleri araştır", 99),
    ("EK-TOOL-28", "Zapier entegrasyonuyla gelen son mailleri Slack kanalına ilet", 102),
    ("EK-TOOL-29", "Unreal Engine aracını kullanarak sahneyi build et ve hata loglarını getir", 104),
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

def run_one(bid, prompt, expected_ubid):
    for outer in range(3):
        if not wait_until_free(max_wait=1200):
            log(f"[SKIP-BUSY] {bid} outer={outer} — server never freed")
            continue
        start_line = audit_line_count()
        started_at = datetime.now(timezone.utc).isoformat()
        response = curl_agent(prompt)
        if response and response.strip() and "BUSY" not in response:
            audit_excerpt = audit_slice(start_line)
            record = {
                "id": bid, "run": 1, "k": 1, "expected_ubid": expected_ubid,
                "started_at": started_at,
                "turns": [{"prompt": prompt, "response": response, "audit_excerpt": audit_excerpt}],
            }
            with open(RESULTS, "a") as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
            log(f"[DONE] {bid} (outer={outer})")
            return True
        log(f"[RETRY] {bid} outer={outer} — empty/BUSY: {str(response)[:150]}")
        time.sleep(15)
    log(f"[FAIL] {bid} — exhausted retries")
    return False

def main():
    for bid, prompt, ubid in TESTS:
        run_one(bid, prompt, ubid)
    log("RUN_12_NEVER_TESTED COMPLETE")

if __name__ == "__main__":
    main()
