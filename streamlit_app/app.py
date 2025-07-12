# -------------------- streamlit_app/app.py --------------------
import streamlit as st
import pandas as pd
from backend.data_loader import load_passage_data, load_transaction_data
from backend.matcher import match_transactions
from backend.analyser import analyse_passage_quality
from backend.logger import save_to_sqlite

st.set_page_config(page_title="Traffic Tolling AI Tool", layout="wide")
st.title("🚦 Traffic Tolling Analytics & Deficiency Detection")

uploaded_passage = st.file_uploader("Upload Passage CSV", type=["csv", "xlsx"])
uploaded_transaction = st.file_uploader("Upload Transaction CSV", type=["csv", "xlsx"])

if uploaded_passage and uploaded_transaction:
    df_passage = load_passage_data(uploaded_passage)
    df_transaction = load_transaction_data(uploaded_transaction)

    st.subheader("Preview: Passage")
    st.dataframe(df_passage.head())

    st.subheader("Preview: Transaction")
    st.dataframe(df_transaction.head())

    st.success("Matching and Analysis in progress...")
    matched, unmatched = match_transactions(df_passage, df_transaction)

    st.subheader("Matched Transactions")
    st.dataframe(matched)

    st.subheader("Unmatched Passages")
    st.dataframe(unmatched)

    issues = analyse_passage_quality(unmatched)
    st.subheader("Detected Issues")
    st.write(issues)

    if st.button("Save to Database"):
        save_to_sqlite(matched, unmatched, issues)
        st.success("Results saved to SQLite database.")
