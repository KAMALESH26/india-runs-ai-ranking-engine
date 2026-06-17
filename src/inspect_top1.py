import json

TARGET_ID = "CAND_0079387"

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] == TARGET_ID:

            print("="*80)
            print("TITLE:", candidate["profile"]["current_title"])
            print("EXP:", candidate["profile"]["years_of_experience"])

            print("\nCAREER HISTORY\n")

            for job in candidate["career_history"]:
                print(job["title"])
                print(job["description"])
                print()

            print("\nSKILL ASSESSMENTS\n")
            print(candidate["redrob_signals"]["skill_assessment_scores"])

            break