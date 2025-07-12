# ------------------ app.py (updated) ------------------
import sys
import os
import streamlit as st
import pandas as pd
import sqlite3

# Add project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.data_loader import load_passage_data, load_transaction_data
from backend.matcher import match_transactions
from backend.analyser import analyse_passage_quality
from backend.logger import save_to_sqlite

# ✅ Streamlit page config
st.set_page_config(page_title="Traffic Tolling AI Tool", layout="wide")
st.title("🚦 Traffic Tolling Analytics & Deficiency Detection")

uploaded_passage = st.file_uploader("📥 Upload Passage CSV", type=["csv", "xlsx"])
uploaded_transaction = st.file_uploader("📥 Upload Transaction CSV", type=["csv", "xlsx"])

if uploaded_passage and uploaded_transaction:
    df_passage = load_passage_data(uploaded_passage)
    df_transaction = load_transaction_data(uploaded_transaction)

    st.subheader("📄 Preview: Passage")
    st.dataframe(df_passage.head())

    st.subheader("📄 Preview: Transaction")
    st.dataframe(df_transaction.head())

    st.success("🔍 Matching and Analysis in progress...")
    matched, unmatched = match_transactions(df_passage, df_transaction)

    st.subheader("✅ Matched Transactions")
    st.dataframe(matched)

    st.subheader("❌ Unmatched Passages")
    st.dataframe(unmatched)

    issues = analyse_passage_quality(unmatched)
    st.subheader("⚠️ Detected Issues")
    st.write(issues)

    if st.button("💾 Save to Database"):
        save_to_sqlite(matched, unmatched, issues)
        st.success("🗂 Results saved to SQLite database.")

# -------------------------------------
# 📊 View Saved Logs from SQLite Database
# -------------------------------------
st.sidebar.subheader("📊 View Saved Logs")

if st.sidebar.button("Show Past Results"):
    try:
        conn = sqlite3.connect("database/results.sqlite")

        st.subheader("🟢 Matched Passages")
        matched_df = pd.read_sql_query("SELECT * FROM matched_passages", conn)
        st.dataframe(matched_df)

        st.subheader("🔴 Unmatched Passages")
        unmatched_df = pd.read_sql_query("SELECT * FROM unmatched_passages", conn)
        st.dataframe(unmatched_df)

        st.subheader("⚠️ Issue Summary")
        issues_df = pd.read_sql_query("SELECT * FROM issue_summary", conn)
        st.dataframe(issues_df)

        conn.close()
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")


