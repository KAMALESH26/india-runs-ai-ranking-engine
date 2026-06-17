def generate_reason(candidate):

    title = candidate["profile"]["current_title"]
    exp = candidate["profile"]["years_of_experience"]

    strengths = []

    text = ""

    for job in candidate.get("career_history", []):
        text += " " + job.get("description", "").lower()

    if "recommendation" in text:
        strengths.append("recommendation systems")

    if "ranking" in text:
        strengths.append("ranking models")

    if "search" in text:
        strengths.append("search systems")

    if "retrieval" in text:
        strengths.append("retrieval pipelines")

    if "semantic search" in text:
        strengths.append("semantic search")

    if "faiss" in text:
        strengths.append("vector search")

    return (
        f"{exp} years experience as {title}. "
        f"Strong background in {', '.join(strengths[:4])}."
    )