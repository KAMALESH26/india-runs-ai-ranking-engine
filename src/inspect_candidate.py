import json

TARGET_IDS = [
    "CAND_0030953",  # Search Engineer
    "CAND_0018549",  # Recommendation Systems Engineer
    "CAND_0055992",  # AI Engineer
]

FILE_PATH = "data/candidates.jsonl"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        if candidate["candidate_id"] in TARGET_IDS:

            print("=" * 80)
            print("ID:", candidate["candidate_id"])

            profile = candidate.get("profile", {})
            print("TITLE:", profile.get("current_title"))
            print("EXP:", profile.get("years_of_experience"))

            print("\nSKILLS:")
            for skill in candidate.get("skills", [])[:20]:
                print("-", skill["name"])

            print("\nCAREER HISTORY:")
            for job in candidate.get("career_history", []):
                print("\nTITLE:", job.get("title"))
                print("DESCRIPTION:")
                print(job.get("description", ""))

            print("\nBEHAVIOR SIGNALS:")
            for k, v in candidate.get("behavioral_signals", {}).items():
                print(k, "=", v)

            print("\n")