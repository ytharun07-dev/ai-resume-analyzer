def generate_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:

        suggestions.append(
            f"Consider adding '{skill}' if you have experience with it."
        )

    if not suggestions:
        suggestions.append(
            "Excellent! Your resume covers all required skills."
        )

    return suggestions