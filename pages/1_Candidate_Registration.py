import streamlit as st
from db import engine
from genai import extract_skills
from sqlalchemy import text

st.title("🧑 Candidate Registration")

name = st.text_input("Candidate Name")
experience = st.number_input("Experience (years)", 0, 30)
resume = st.text_area("Paste Resume Text")

if st.button("Register Candidate"):
    skills = extract_skills(resume)

    with engine.begin() as conn:
        result = conn.execute(
            text("INSERT INTO users(name, experience) VALUES (:n, :e)"),
            {"n": name, "e": experience}
        )
        user_id = result.lastrowid

        for skill in skills:
            conn.execute(
                text("INSERT IGNORE INTO skills(skill_name) VALUES (:s)"),
                {"s": skill}
            )

            skill_id = conn.execute(
                text("SELECT skill_id FROM skills WHERE skill_name=:s"),
                {"s": skill}
            ).scalar()

            conn.execute(
                text("INSERT IGNORE INTO user_skills VALUES (:u, :s)"),
                {"u": user_id, "s": skill_id}
            )

    st.success("✅ Candidate registered successfully")
