import json

FILE_PATH = "data/candidates.jsonl"

KEYWORDS = [
    "recommendation",
    "ranking",
    "retrieval",
    "search",
    "relevance",
    "embedding",
    "llm",
    "machine learning",
    "artificial intelligence",
    "personalization"
]

matches = []

with open(FILE_PATH, "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        text = ""

        for exp in candidate.get("career_history", []):
            text += " " + str(exp.get("title", ""))
            text += " " + str(exp.get("description", ""))

        text = text.lower()

        score = 0

        for keyword in KEYWORDS:
            if keyword in text:
                score += 1

        if score > 0:
            matches.append(
                {
                    "id": candidate.get("candidate_id"),
                    "score": score,
                    "title": candidate.get("profile", {}).get(
                        "current_title", "Unknown"
                    )
                }
            )

matches.sort(key=lambda x: x["score"], reverse=True)

print("\nTop 20 Matching Candidates\n")

for item in matches[:20]:
    print(item)