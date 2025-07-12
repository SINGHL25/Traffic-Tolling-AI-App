# -------------------- backend/matcher.py --------------------
def match_transactions(passage_df, transaction_df):
    merged = passage_df.merge(transaction_df, how='left', left_on='Transaction 1 ID', right_on='Id')
    matched = merged[~merged['Serial Number'].isnull()]
    unmatched = passage_df[~passage_df['Transaction 1 ID'].isin(transaction_df['Id'])]
    return matched, unmatched
