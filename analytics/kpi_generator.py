def generate_kpis(df_passage, df_transaction, unmatched):
    # Ensure 'Time Stamp' column is datetime
    if 'Time Stamp' in df_passage.columns:
        df_passage['Time Stamp'] = pd.to_datetime(df_passage['Time Stamp'])
    else:
        raise KeyError("Expected 'Time Stamp' column not found in passage data")

    matched_count = len(df_passage) - len(unmatched)
    total_unmatched = len(unmatched)
    total_passages = len(df_passage)

    return {
        "Total Passages": total_passages,
        "Matched Passages": matched_count,
        "Unmatched Passages": total_unmatched,
        "Passage Match Rate (%)": round((matched_count / total_passages) * 100, 2) if total_passages > 0 else 0,
        "Avg Vehicles Per Hour": df_passage.groupby(df_passage['Time Stamp'].dt.hour).size().mean()
    }
