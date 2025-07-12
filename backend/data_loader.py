# backend/data_loader.py

import pandas as pd

def load_passage_data(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # Normalize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Parse timestamp
    if 'time_stamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['time_stamp'])

    return df


def load_transaction_data(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # Normalize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Parse timestamp
    if 'time_stamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['time_stamp'])

    return df
