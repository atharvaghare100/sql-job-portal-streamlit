import streamlit as st
import pandas as pd
from db import engine
from queries import ACCEPTANCE_QUERY
from ml_model import predict_acceptance

st.title("📈 Offer Acceptance Probability")

# Step 1: Select Job
job_id = st.number_input("Select Job ID", min_value=1)

if job_id:
    df = pd.read_sql(
        ACCEPTANCE_QUERY,
        engine,
        params=(job_id, job_id)
    )

    if df.empty:
        st.warning("No candidates matched for this job.")
    else:
        st.subheader("Matched Candidates")

        st.dataframe(df)

        # Step 2: Select Candidate
        candidate_name = st.selectbox(
            "Select Candidate",
            df["candidate_name"]
        )

        selected = df[df["candidate_name"] == candidate_name].iloc[0]

        skill_match = selected["skill_match_ratio"]
        experience = selected["experience"]

        # Step 3: Predict
        if st.button("Predict Acceptance Probability"):
            prob = predict_acceptance(skill_match, experience)

            st.success(
                f"Acceptance Probability for {candidate_name}: {prob:.2f}"
            )
