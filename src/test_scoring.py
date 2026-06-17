import json

from feature_engineering import (
    career_score,
    experience_score,
    redrob_score,
    skill_score,
    certification_score,
    final_score
)

TARGET_IDS = [
    "CAND_0030953",
    "CAND_0018549",
    "CAND_0055992"
]

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] in TARGET_IDS:

            print("=" * 60)

            print("ID:", candidate["candidate_id"])
            print("TITLE:", candidate["profile"]["current_title"])

            print("Career Score:", career_score(candidate))
            print("Experience Score:", experience_score(candidate))
            print("Redrob Score:", redrob_score(candidate))
            print("Final Score:", final_score(candidate))