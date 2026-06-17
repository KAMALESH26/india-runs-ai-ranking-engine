# src/show_signals.py

import json

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    candidate = json.loads(next(f))

print(candidate["redrob_signals"])