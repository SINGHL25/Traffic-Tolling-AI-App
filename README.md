# Traffic-Tolling-AI-App
This app analyzes traffic passage and transaction data to detect inconsistencies like: - Vehicle passed without valid number plate - Missing tag/transaction linkage - Duplicate or unmatched vehicle records
# -------------------- README.md --------------------
# 📈 Traffic Toll AI Project

This app analyzes traffic passage and transaction data to detect:
- Vehicle passage with missing number plates
- Unlinked or failed transactions
- Tagless or unmatched entries

## 📁 Folder Structure
```
streamlit_app/ - Web frontend (Streamlit)
backend/       - Logic, analysis, and DB logging
data/          - Upload CSV/XLS data
database/      - SQLite logs (local DB)
powerbi/       - Power BI .pbix dashboard
```

## 🚀 Getting Started
```bash
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

## 📊 Power BI Insights
Use `powerbi/traffic_dashboard.pbix` with the `results.sqlite` DB as your source to analyze:
- Matching success rate
- Rejected vehicle passages
- Most common passage failure reason

## 🧪 Next Steps
- Firebase logging
- Voice alerts on critical tolling errors
- API-based live tolling status feed

