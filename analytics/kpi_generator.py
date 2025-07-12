import pandas as pd

def generate_kpis(df_passage, df_transaction, unmatched_df):
    # ✅ Correct column name based on your passage file
    if "Time Stamp" in df_passage.columns:
        df_passage["Time Stamp"] = pd.to_datetime(df_passage["Time Stamp"], errors='coerce')
        df_passage["hour"] = df_passage["Time Stamp"].dt.hour
    else:
        # Fallback to a default datetime column or raise a message
        df_passage["hour"] = pd.NaT

    total_passages = len(df_passage)
    matched_count = len(df_transaction)
    total_unmatched = len(unmatched_df)

    hourly_avg = df_passage.groupby("hour").size().mean() if "hour" in df_passage.columns else 0

    return {
        "Total Passages": total_passages,
        "Matched Passages": matched_count,
        "Unmatched Passages": total_unmatched,
        "Passage Match Rate (%)": round((matched_count / total_passages) * 100, 2) if total_passages > 0 else 0,
        "Avg Vehicles Per Hour": round(hourly_avg, 2)
    }
