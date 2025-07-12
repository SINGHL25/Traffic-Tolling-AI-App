# -------------------- backend/logger.py --------------------
import sqlite3
from datetime import datetime

def save_to_sqlite(matched, unmatched, issues):
    conn = sqlite3.connect("database/results.sqlite")
    matched.to_sql("matched_passages", conn, if_exists="append", index=False)
    unmatched.to_sql("unmatched_passages", conn, if_exists="append", index=False)

    # Save issues summary
    issue_table = [(datetime.now().isoformat(), k, v) for k, v in issues.items()]
    conn.execute("CREATE TABLE IF NOT EXISTS issue_summary (timestamp TEXT, issue_type TEXT, count INTEGER)")
    conn.executemany("INSERT INTO issue_summary VALUES (?, ?, ?)", issue_table)
    conn.commit()
    conn.close()
