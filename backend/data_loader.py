# -------------------- backend/data_loader.py --------------------
import pandas as pd

def load_passage_data(file):
    if file.name.endswith('.xlsx'):
        return pd.read_excel(file)
    return pd.read_csv(file)

def load_transaction_data(file):
    if file.name.endswith('.xlsx'):
        return pd.read_excel(file)
    return pd.read_csv(file)

