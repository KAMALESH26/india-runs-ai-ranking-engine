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
    "CAND_0079387",  # AI Engineer
    "CAND_0086022",  # Senior Applied Scientist
    "CAND_0064326",  # Search Engineer
]

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] in TARGET_IDS:

            print("=" * 80)

            print(candidate["candidate_id"])
            print(candidate["profile"]["current_title"])

            print("Career:", career_score(candidate))
            print("Experience:", experience_score(candidate))
            print("Redrob:", redrob_score(candidate))
            print("Skills:", skill_score(candidate))
            print("Certifications:", certification_score(candidate))
            print("Final:", final_score(candidate))