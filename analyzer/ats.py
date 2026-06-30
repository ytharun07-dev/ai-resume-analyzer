import re

TECH_SKILLS = [
    "python",
    "django",
    "html",
    "css",
    "javascript",
    "bootstrap",
    "sql",
    "mysql",
    "oracle",
    "git",
    "github",
    "docker",
    "aws",
    "linux",
    "rest",
    "api",
    "react",
    "flask",
    "pandas",
    "numpy",
    "excel",
    "power bi",
    "communication",
    "problem solving",
]


def calculate_ats_score(resume_text, job_description):

    resume = resume_text.lower()
    job = job_description.lower()

    matched = []
    missing = []

    for skill in TECH_SKILLS:

        if skill in job:

            if skill in resume:
                matched.append(skill)
            else:
                missing.append(skill)

    if len(matched) + len(missing) == 0:
        score = 0
    else:
        score = round(
            len(matched) / (len(matched) + len(missing)) * 100
        )

    return {
        "score": score,
        "matched": matched,
        "missing": missing,
    }