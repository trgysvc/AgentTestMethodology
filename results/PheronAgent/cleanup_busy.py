import json

path = "results_k5upgrade_core.jsonl"
kept = []
removed = 0
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        resp = d["turns"][0]["response"] or ""
        if d["id"] == "L3-TOOL-12" and '"error":"BUSY"' in resp:
            removed += 1
            continue
        kept.append(line)

with open(path, "w") as f:
    for line in kept:
        f.write(line + "\n")

print("removed", removed, "lines; kept", len(kept))
