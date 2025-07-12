import sys
import os
import streamlit as st
import pandas as pd

# 🔁 Ensure root path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 📦 Backend core modules
from backend.data_loader import load_passage_data, load_transaction_data
from backend.matcher import match_transactions
from backend.analyser import analyse_passage_quality
from backend.logger import save_to_sqlite

# 📊 KPI + Plot modules
from analytics.kpi_generator import generate_kpis
from analytics.plot_generator import (
    plot_vehicle_class_distribution,
    plot_passage_time_trend,
    plot_match_ratio_pie
)

# ✅ Streamlit page config
st.set_page_config(page_title="Traffic Tolling AI Tool", layout="wide")
st.title("🚦 Traffic Tolling Analytics & Deficiency Detection")

# 🔼 File uploaders
uploaded_passage = st.file_uploader("📤 Upload Passage File", type=["csv", "xlsx"])
uploaded_transaction = st.file_uploader("📤 Upload Transaction File", type=["csv", "xlsx"])

if uploaded_passage and uploaded_transaction:
    # 📥 Load Data
    df_passage = load_passage_data(uploaded_passage)
    df_transaction = load_transaction_data(uploaded_transaction)

    # --- Fix: Rename datetime column to 'timestamp' ---
    if 'Time Stamp' in df_passage.columns:
        df_passage = df_passage.rename(columns={'Time Stamp': 'timestamp'})
    elif 'TS' in df_passage.columns:
        df_passage = df_passage.rename(columns={'TS': 'timestamp'})

    # Convert 'timestamp' column to datetime (coerce errors)
    df_passage['timestamp'] = pd.to_datetime(df_passage['timestamp'], errors='coerce')

    # 📄 Show raw data previews
    st.subheader("📄 Preview: Passage Data")
    st.dataframe(df_passage.head())

    st.subheader("📄 Preview: Transaction Data")
    st.dataframe(df_transaction.head())

    # 🔍 Match & analyze
    st.success("✅ Matching and analysis started...")
    matched, unmatched = match_transactions(df_passage, df_transaction)

    st.subheader("✅ Matched Transactions")
    st.dataframe(matched)

    st.subheader("❌ Unmatched Passages")
    st.dataframe(unmatched)

    issues = analyse_passage_quality(unmatched)

    st.subheader("⚠️ Detected Issues")
    st.write(issues)

    if st.button("💾 Save to SQLite"):
        save_to_sqlite(matched, unmatched, issues)
        st.success("✅ Results saved to SQLite database")

    # 📈 KPIs
    st.markdown("---")
    st.header("📊 Key Insights & Analytics")

    kpis = generate_kpis(df_passage, df_transaction, unmatched)
    st.subheader("📈 Key Performance Indicators")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Passages", kpis["Total Passages"])
    col2.metric("Matched Passages", kpis["Matched Passages"])
    col3.metric("Unmatched Passages", kpis["Unmatched Passages"])

    # 📉 Visuals
    st.subheader("📊 Visual Analytics")

   # plot_vehicle_class_distribution(df_passage)
    plot_passage_time_trend(df_passage)
    plot_match_ratio_pie(kpis["Matched Passages"], kpis["Unmatched Passages"])

    # 🖼 Show saved plot images (optional fallback)
    st.image("docs/vehicle_class_distribution.png", caption="Vehicle Class Distribution")
    st.image("docs/passage_hourly_trend.png", caption="Hourly Passage Trend")
    st.image("docs/match_ratio_pie.png", caption="Match vs Unmatched Ratio")




