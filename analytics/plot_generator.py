import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_vehicle_class_distribution(df_passage):
    os.makedirs("docs", exist_ok=True)  # Ensure output folder exists

    # Check for vehicle class column (case-insensitive and common variants)
    possible_cols = ['vehicle_class', 'Vehicle Class', 'vehicle class']
    col = next((c for c in possible_cols if c in df_passage.columns), None)
    if col is None:
        raise ValueError(f"Vehicle Class column not found. Columns available: {df_passage.columns.tolist()}")

    plt.figure(figsize=(10, 5))
    sns.countplot(x=col, data=df_passage)
    plt.title('Vehicle Class Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("docs/vehicle_class_distribution.png")
    plt.close()

def plot_passage_time_trend(df_passage):
    os.makedirs("docs", exist_ok=True)

    # Check timestamp column name
    possible_ts_cols = ['timestamp', 'Timestamp', 'Time Stamp', 'time_stamp']
    ts_col = next((c for c in possible_ts_cols if c in df_passage.columns), None)
    if ts_col is None:
        raise ValueError(f"Timestamp column not found. Columns available: {df_passage.columns.tolist()}")

    # Convert to datetime if not already
    if not pd.api.types.is_datetime64_any_dtype(df_passage[ts_col]):
        df_passage[ts_col] = pd.to_datetime(df_passage[ts_col], errors='coerce')

    df_passage['hour'] = df_passage[ts_col].dt.hour

    hourly = df_passage.groupby('hour').size()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=hourly.index, y=hourly.values)
    plt.title('Vehicle Passage Trend by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Vehicle Count')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("docs/passage_hourly_trend.png")
    plt.close()

def plot_match_ratio_pie(matched_count, unmatched_count):
    os.makedirs("docs", exist_ok=True)

    plt.figure(figsize=(6, 6))
    plt.pie(
        [matched_count, unmatched_count],
        labels=["Matched", "Unmatched"],
        autopct="%1.1f%%",
        colors=["#4CAF50", "#F44336"],
        startangle=90
    )
    plt.title("Passage Match vs Unmatched")
    plt.tight_layout()
    plt.savefig("docs/match_ratio_pie.png")
    plt.close()


