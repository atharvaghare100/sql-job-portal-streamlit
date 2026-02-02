# =========================
# Candidate Matching Query
# =========================

MATCH_QUERY = """
WITH matched AS (
    SELECT
        us.user_id,
        COUNT(*) AS matched_skills
    FROM user_skills us
    JOIN job_skills js
        ON us.skill_id = js.skill_id
    WHERE js.job_id = %s
    GROUP BY us.user_id
),
total AS (
    SELECT COUNT(*) AS total_skills
    FROM job_skills
    WHERE job_id = %s
)
SELECT
    u.name AS candidate_name,
    u.experience,
    ROUND((m.matched_skills / t.total_skills) * 100, 2) AS match_percentage,
    RANK() OVER (
        ORDER BY (m.matched_skills / t.total_skills) DESC
    ) AS ranking
FROM matched m
JOIN users u
    ON m.user_id = u.user_id
CROSS JOIN total t
ORDER BY ranking;
"""

# =========================
# Acceptance Probability Query
# =========================

ACCEPTANCE_QUERY = """
WITH matched AS (
    SELECT
        us.user_id,
        COUNT(*) AS matched_skills
    FROM user_skills us
    JOIN job_skills js
        ON us.skill_id = js.skill_id
    WHERE js.job_id = %s
    GROUP BY us.user_id
),
total AS (
    SELECT COUNT(*) AS total_skills
    FROM job_skills
    WHERE job_id = %s
)
SELECT
    u.user_id,
    u.name AS candidate_name,
    u.experience,
    ROUND(m.matched_skills / t.total_skills, 3) AS skill_match_ratio
FROM matched m
JOIN users u
    ON u.user_id = m.user_id
CROSS JOIN total t
ORDER BY skill_match_ratio DESC;
"""
