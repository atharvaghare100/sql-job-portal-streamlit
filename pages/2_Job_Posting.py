import streamlit as st
from db import engine
from sqlalchemy import text

st.title("📌 Job Posting")

title = st.text_input("Job Title")
min_exp = st.number_input("Minimum Experience", 0, 20)
skills = st.text_input("Required Skills (comma separated)")

if st.button("Post Job"):
    with engine.begin() as conn:
        result = conn.execute(
            text("INSERT INTO jobs(title, min_experience) VALUES (:t, :e)"),
            {"t": title, "e": min_exp}
        )
        job_id = result.lastrowid

        for skill in skills.split(","):
            skill = skill.strip().lower()

            conn.execute(
                text("INSERT IGNORE INTO skills(skill_name) VALUES (:s)"),
                {"s": skill}
            )

            skill_id = conn.execute(
                text("SELECT skill_id FROM skills WHERE skill_name=:s"),
                {"s": skill}
            ).scalar()

            conn.execute(
                text("INSERT IGNORE INTO job_skills VALUES (:j, :s)"),
                {"j": job_id, "s": skill_id}
            )

    st.success("✅ Job posted successfully")
