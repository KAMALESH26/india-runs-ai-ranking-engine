import re

HIGH_VALUE_KEYWORDS = [
    "ranking",
    "recommendation",
    "retrieval",
    "search",
    "relevance",
    "learning-to-rank",
    "semantic search",
    "faiss",
    "bm25",
    "personalization",
]

TITLE_BOOSTS = {
    "Search Engineer": 20,
    "Recommendation Systems Engineer": 20,
    "Applied ML Engineer": 15,
    "Machine Learning Engineer": 10,
    "NLP Engineer": 5,
    "AI Engineer": 5,
}

TARGET_SKILLS = [
    "Recommendation Systems",
    "Information Retrieval",
    "Learning to Rank",
    "Embeddings",
    "NLP",
    "Machine Learning",
    "Search",
]

MEDIUM_VALUE_KEYWORDS = [
    "llm",
    "rag",
    "langchain",
    "embeddings",
    "gpt",
]


def career_score(candidate):

    score = 0

    for job in candidate.get("career_history", []):

        text = (
            job.get("title", "") + " " +
            job.get("description", "")
        ).lower()

        for keyword in HIGH_VALUE_KEYWORDS:
            if keyword in text:
                score += 10

        for keyword in MEDIUM_VALUE_KEYWORDS:
            if keyword in text:
                score += 5

    return min(score, 100)


def experience_score(candidate):

    exp = candidate["profile"]["years_of_experience"]

    if 6 <= exp <= 8:
        return 100

    if 5 <= exp < 6:
        return 85

    if 8 < exp <= 10:
        return 80

    if 3 <= exp < 5:
        return 60

    return 30


def redrob_score(candidate):

    signals = candidate.get("redrob_signals", {})

    score = 0

    if signals.get("open_to_work_flag"):
        score += 20

    score += min(
        signals.get("github_activity_score", 0) * 2,
        20
    )

    score += min(
        signals.get("saved_by_recruiters_30d", 0) * 2,
        20
    )

    score += min(
        signals.get("interview_completion_rate", 0) * 20,
        20
    )

    score += min(
        signals.get("recruiter_response_rate", 0) * 20,
        20
    )

    return min(score, 100)

def title_score(candidate):

    title = candidate["profile"]["current_title"]

    return TITLE_BOOSTS.get(title, 0)

def skill_score(candidate):

    signals = candidate.get("redrob_signals", {})
    assessments = signals.get("skill_assessment_scores", {})

    score = 0

    HIGH_VALUE = [
        "recommendation",
        "retrieval",
        "ranking",
        "search",
        "learning to rank",
        "information retrieval"
    ]

    for skill, value in assessments.items():

        skill_lower = skill.lower()

        for keyword in HIGH_VALUE:
            if keyword in skill_lower:
                score += value
                break

    return min(score, 100)

    return min(score, 100)

def certification_score(candidate):

    certs = candidate.get("certifications", [])

    score = len(certs) * 10

    return min(score, 100)


def final_score(candidate):

    career = career_score(candidate)
    experience = experience_score(candidate)
    redrob = redrob_score(candidate)
    skills = skill_score(candidate)
    certs = certification_score(candidate)
    title = title_score(candidate)

    score = (
        career * 0.55 +
        experience * 0.20 +
        redrob * 0.10 +
        skills * 0.05 +
        certs * 0.02 +
        title * 0.08
    )

    return round(score, 2)