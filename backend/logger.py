import sqlite3
from datetime import datetime
import os

# import firebase_admin
# from firebase_admin import credentials, firestore

# # Init Firebase
# firebase_path = os.getenv("FIREBASE_CRED_PATH", "firebase_key.json")
# if os.path.exists(firebase_path) and not firebase_admin._apps:
#     cred = credentials.Certificate(firebase_path)
#     firebase_admin.initialize_app(cred)
#     db = firestore.client()
# else:
#     db = None

def save_to_sqlite(matched, unmatched, issues):
    conn = sqlite3.connect("database/results.sqlite")
    matched.to_sql("matched_passages", conn, if_exists="append", index=False)
    unmatched.to_sql("unmatched_passages", conn, if_exists="append", index=False)

    issue_table = [(datetime.now().isoformat(), k, v) for k, v in issues.items()]
    conn.execute("CREATE TABLE IF NOT EXISTS issue_summary (timestamp TEXT, issue_type TEXT, count INTEGER)")
    conn.executemany("INSERT INTO issue_summary VALUES (?, ?, ?)", issue_table)
    conn.commit()
    conn.close()

    # # 🔥 Save to Firebase (Disabled)
    # if db:
    #     doc = {
    #         "timestamp": datetime.now().isoformat(),
    #         "issues": issues,
    #         "matched_count": len(matched),
    #         "unmatched_count": len(unmatched)
    #     }
    #     db.collection("traffic_logs").add(doc)

