# -------------------- backend/analyser.py --------------------
def analyse_passage_quality(unmatched_df):
    issues = {}
    no_front_lpn = unmatched_df['Front LPN'].isnull().sum()
    no_tag = unmatched_df['Transaction 1 ID'].isnull().sum()
    issues['Missing Front LPN'] = no_front_lpn
    issues['Missing Tag (Transaction ID)'] = no_tag
    return issues
