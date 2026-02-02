import streamlit as st
import pandas as pd
from db import engine
from queries import MATCH_QUERY

st.title("🎯 Candidate Matching")

job_id = st.number_input("Enter Job ID", 1)

if st.button("Find Best Candidates"):
    df = pd.read_sql(MATCH_QUERY, engine, params=(job_id, job_id))
    st.dataframe(df)
