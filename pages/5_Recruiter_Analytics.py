import streamlit as st
import pandas as pd
from db import engine

st.title("📊 Recruiter Analytics")

query = """
SELECT s.skill_name, COUNT(*) AS demand
FROM job_skills js
JOIN skills s ON js.skill_id = s.skill_id
GROUP BY s.skill_name
ORDER BY demand DESC
"""

df = pd.read_sql(query, engine)
st.bar_chart(df.set_index("skill_name"))
