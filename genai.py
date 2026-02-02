import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def extract_skills(resume_text):
    prompt = f"""
    Extract ONLY technical skills from the resume below.
    Return them as a comma-separated list.

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    skills_text = response.choices[0].message.content
    return [s.strip().lower() for s in skills_text.split(",")]
