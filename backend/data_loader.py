import pandas as pd

def load_passage_data(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # Rename 'Time Stamp' to 'timestamp' if it exists
    for col in df.columns:
        if col.strip().lower() == "time stamp":
            df = df.rename(columns={col: "timestamp"})
            break

    # Convert timestamp column to datetime
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df


def load_transaction_data(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # Rename 'Time Stamp' to 'timestamp' if it exists
    for col in df.columns:
        if col.strip().lower() == "time stamp":
            df = df.rename(columns={col: "timestamp"})
            break

    # Convert timestamp column to datetime
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df
