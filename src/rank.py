import json
import pandas as pd

from feature_engineering import final_score

FILE_PATH = "data/candidates.jsonl"

results = []

count = 0

with open(FILE_PATH, "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        score = final_score(candidate)

        from reasoning import generate_reason

        results.append({
            "candidate_id": candidate["candidate_id"],
            "title": candidate["profile"]["current_title"],
            "score": score,
            "reason": generate_reason(candidate)
        })

        count += 1

        if count % 10000 == 0:
            print(f"Processed {count}")

df = pd.DataFrame(results)

df = df.sort_values(
    by="score",
    ascending=False
)

top100 = df.head(100)

# Detailed file for demo/PPT
top100.to_csv(
    "outputs/top100_detailed.csv",
    index=False
)

# Submission file
submission = top100[["candidate_id"]]

submission.to_csv(
    "outputs/submission.csv",
    index=False
)

print("Saved outputs/submission.csv")
print("Saved outputs/top100_detailed.csv")
print("Saved final_submission.csv")

df.to_csv(
    "outputs/top_candidates.csv",
    index=False
)

print("\nSaved outputs/top_candidates.csv")