import re
from .constants import TECH_SKILLS


def calculate_ats_score(resume_text, job_description):

    resume = resume_text.lower()
    job = job_description.lower()

    matched = []
    missing = []

    for skill in TECH_SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, job):

            if re.search(pattern, resume):
                matched.append(skill)
            else:
                missing.append(skill)

    total = len(matched) + len(missing)

    score = round((len(matched) / total) * 100) if total else 0

    return {
        "score": score,
        "matched": matched,
        "missing": missing,
    }