from .constants import (
    BACKEND_SKILLS,
    FRONTEND_SKILLS,
    DATABASE_SKILLS,
    DEVOPS_SKILLS,
    AI_SKILLS,
    SOFT_SKILLS,
)


def categorize_skills(matched, missing):

    categories = {
        "Backend": {
            "matched": [],
            "missing": []
        },
        "Frontend": {
            "matched": [],
            "missing": []
        },
        "Database": {
            "matched": [],
            "missing": []
        },
        "DevOps": {
            "matched": [],
            "missing": []
        },
        "AI / ML": {
            "matched": [],
            "missing": []
        },
        "Soft Skills": {
            "matched": [],
            "missing": []
        },
    }

    for skill in matched:

        if skill in BACKEND_SKILLS:
            categories["Backend"]["matched"].append(skill)

        elif skill in FRONTEND_SKILLS:
            categories["Frontend"]["matched"].append(skill)

        elif skill in DATABASE_SKILLS:
            categories["Database"]["matched"].append(skill)

        elif skill in DEVOPS_SKILLS:
            categories["DevOps"]["matched"].append(skill)

        elif skill in AI_SKILLS:
            categories["AI / ML"]["matched"].append(skill)

        elif skill in SOFT_SKILLS:
            categories["Soft Skills"]["matched"].append(skill)

    for skill in missing:

        if skill in BACKEND_SKILLS:
            categories["Backend"]["missing"].append(skill)

        elif skill in FRONTEND_SKILLS:
            categories["Frontend"]["missing"].append(skill)

        elif skill in DATABASE_SKILLS:
            categories["Database"]["missing"].append(skill)

        elif skill in DEVOPS_SKILLS:
            categories["DevOps"]["missing"].append(skill)

        elif skill in AI_SKILLS:
            categories["AI / ML"]["missing"].append(skill)

        elif skill in SOFT_SKILLS:
            categories["Soft Skills"]["missing"].append(skill)

    return categories