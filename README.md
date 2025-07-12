# Traffic-Tolling-AI-App
This app analyzes traffic passage and transaction data to detect inconsistencies like: - Vehicle passed without valid number plate - Missing tag/transaction linkage - Duplicate or unmatched vehicle records
# -------------------- README.md --------------------
# \U0001F4C8 Traffic Toll AI Project

This app analyzes traffic passage and transaction data to detect inconsistencies like:
- Vehicle passed without valid number plate
- Missing tag/transaction linkage
- Duplicate or unmatched vehicle records

## \U0001F4C2 Folder Structure
```
streamlit_app/ - Web frontend
backend/       - Logic & utils
data/          - Sample CSV/XLS files
database/      - Future SQLite logs
```

## ⚡ Usage
```
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

## \U0001F5C3 Future Scope
- Save logs in SQLite
- Email alerts for tolling failures
- Add prediction for fraud/passback
