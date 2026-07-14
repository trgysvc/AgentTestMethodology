#!/usr/bin/env python3
import json, subprocess, time, sys
from datetime import datetime, timezone

RESULTS = "/Users/trgysvc/Developer/EliteAgent/Tests/AgentTestSuite/results/results_k5upgrade_core.jsonl"
LOG = "/Users/trgysvc/Developer/EliteAgent/Tests/AgentTestSuite/results/run_k5upgrade_core.log"
HEALTH = "http://localhost:11500/api/health"
AGENT = "http://localhost:11500/api/agent"
AUDIT = "/Users/trgysvc/Library/Logs/PheronAgent/audit.log"

REMAINING = [
    ("L3-TOOL-01", "'/Users/trgysvc/Local Documents/Suno Downloads/Aura di Luce (Aura of Light - Işık Hale)/Aura di Luce (Aura of Light - Işık Hale) (1).mp3' dosyasındaki müziğin DNA analizini yap ve bana müzik türünü söyle"),
    ("L3-TOOL-02", "çalan şarkıyı durdur ve bir sonraki şarkıya geç"),
    ("L3-TOOL-06", "Safari'de yeni bir sekme aç ve google.com adresine git"),
    ("L3-TOOL-07", "Swift 6 dökümantasyon sayfasını tarayıcıda doğrudan aç"),
    ("L3-TOOL-08", "proje performans analizini içeren bir markdown raporu tasarla"),
    ("L3-TOOL-10", "Takvime yarın saat 10:00'da 'Haftalık Değerlendirme' adında bir etkinlik ekle"),
    ("L3-TOOL-12", "Blender ile arka planda 3D küp modeli render et"),
    ("L3-TOOL-13", "mevcut Swift projesini Xcode derleyicisi ile build et"),
    ("L3-TOOL-14", "sistemdeki mevcut kestirmeleri listele"),
    ("L3-TOOL-19", "/Users/trgysvc/Local Documents/Suno Downloads/Aura di Luce (Aura of Light - Işık Hale) dizinindeki MP3 dosyalarının ID3 etiketlerini txt ve jpeg dosyalarını kullanarak otomatik doldur, TPE1 değerini 'Aura Artist' ve TALB değerini 'Aura Album' olarak ez (override et)"),
]

def log(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")
    print(msg, flush=True)

def is_free():
    try:
        out = subprocess.run(["curl", "-s", "-m", "5", HEALTH], capture_output=True, text=True, timeout=10)
        d = json.loads(out.stdout)
        return d.get("model_loaded") and not d.get("is_busy")
    except Exception:
        return False

def wait_until_free(max_wait=600):
    start = time.time()
    while time.time() - start < max_wait:
        if is_free():
            return True
        time.sleep(3)
    return False

def curl_agent(prompt, timeout=180):
    body = json.dumps({"prompt": prompt})
    try:
        out = subprocess.run(
            ["curl", "-s", "-m", str(timeout), "-X", "POST", AGENT,
             "-H", "Content-Type: application/json", "-d", body],
            capture_output=True, text=True, timeout=timeout + 15
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
        log(f"[SKIP-BUSY] {bid} extra-run {run_idx}/2 — server never freed")
        return
    started_at = datetime.now(timezone.utc).isoformat()
    response = None
    for attempt in range(3):
        response = curl_agent(prompt)
        if response and "BUSY" not in response:
            break
        time.sleep(5)
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
    log(f"[DONE] {bid} extra-run {run_idx}/2")

def main():
    for bid, prompt in REMAINING:
        for run_idx in (1, 2):
            run_one(bid, prompt, run_idx)
    log("K5 UPGRADE CORE COMPLETE")

if __name__ == "__main__":
    main()
