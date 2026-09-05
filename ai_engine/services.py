def review_code(code):

    score = 5

    strengths = []
    weaknesses = []
    recommendations = []

    complexity = "O(1)"

    if "for " in code:
        complexity = "O(n)"
        score += 1

    if code.count("for ") >= 2:
        complexity = "O(n²)"
        score += 1

    if "def " in code:
        score += 2
        strengths.append(
            "Functions used correctly."
        )

    if "return" in code:
        score += 1
        strengths.append(
            "Returns output properly."
        )

    if len(code) < 50:
        weaknesses.append(
            "Code may be too short."
        )

    recommendations.append(
        "Practice optimization techniques."
    )

    return {

        "score": min(score, 10),

        "complexity": complexity,

        "strengths": strengths,

        "weaknesses": weaknesses,

        "recommendations": recommendations

    }