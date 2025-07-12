import pandas as pd

def generate_kpis(df_passage, df_transaction, df_unmatched):
    total_passages = len(df_passage)
    total_transactions = len(df_transaction)
    total_unmatched = len(df_unmatched)
    matched_count = total_passages - total_unmatched

    return {
        "Total Passages": total_passages,
        "Total Transactions": total_transactions,
        "Matched Passages": matched_count,
        "Unmatched Passages": total_unmatched,
        "Passage Match Rate (%)": round((matched_count / total_passages) * 100, 2),
        "Avg Vehicles Per Hour": df_passage.groupby(df_passage['timestamp'].dt.hour).size().mean()
    }

