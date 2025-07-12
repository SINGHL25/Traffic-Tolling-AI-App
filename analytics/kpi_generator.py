def generate_kpis(df_passage, df_transaction, unmatched_df):
    # Try to find timestamp column dynamically (case insensitive)
    timestamp_col = None
    for col in df_passage.columns:
        if "time" in col.lower():
            timestamp_col = col
            break

    if timestamp_col is not None:
        try:
            df_passage[timestamp_col] = pd.to_datetime(df_passage[timestamp_col], errors='coerce')
            df_passage["hour"] = df_passage[timestamp_col].dt.hour
            hourly_avg = df_passage.groupby("hour").size().mean()
        except Exception as e:
            hourly_avg = 0
    else:
        hourly_avg = 0  # fallback if no timestamp column found

    total_passages = len(df_passage)
    matched_count = len(df_transaction)
    total_unmatched = len(unmatched_df)

    kpis = {
        "Total Passages": total_passages,
        "Matched Passages": matched_count,
        "Unmatched Passages": total_unmatched,
        "Passage Match Rate (%)": round((matched_count / total_passages) * 100, 2) if total_passages > 0 else 0,
        "Avg Vehicles Per Hour": round(hourly_avg, 2)
    }

    return kpis
