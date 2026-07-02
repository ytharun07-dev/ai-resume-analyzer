import re
from .constants import TECH_SKILLS
from .weights import SKILL_WEIGHTS


def calculate_ats_score(resume_text, job_description):
    """
    Compare resume with job description and calculate
    weighted ATS score.
    """

    resume = resume_text.lower()
    job = job_description.lower()

    matched = []
    missing = []

    # Match skills using whole-word/phrase matching
    for skill in TECH_SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, job):

            if re.search(pattern, resume):
                matched.append(skill)
            else:
                missing.append(skill)

    # Weighted scoring
    matched_weight = sum(
        SKILL_WEIGHTS.get(skill, 1)
        for skill in matched
    )

    missing_weight = sum(
        SKILL_WEIGHTS.get(skill, 1)
        for skill in missing
    )

    total_weight = matched_weight + missing_weight

    if total_weight == 0:
        score = 0
    else:
        score = round((matched_weight / total_weight) * 100)

    return {
        "score": score,
        "matched": matched,
        "missing": missing,
    }