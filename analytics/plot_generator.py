import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

# Ensure the docs folder exists before saving plots
os.makedirs("docs", exist_ok=True)

def plot_vehicle_class_distribution(df_passage):
    plt.figure(figsize=(10, 5))
    # Use the correct column name, e.g., 'Vehicle Class'
    sns.countplot(x='Vehicle Class', data=df_passage)
    plt.title('Vehicle Class Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("docs/vehicle_class_distribution.png")
    plt.close()

def plot_passage_time_trend(df_passage):
    # Convert 'Time Stamp' to datetime if not already
    if not pd.api.types.is_datetime64_any_dtype(df_passage['Time Stamp']):
        df_passage['Time Stamp'] = pd.to_datetime(df_passage['Time Stamp'], errors='coerce')

    df_passage['hour'] = df_passage['Time Stamp'].dt.hour
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
    plt.figure(figsize=(6, 6))
    plt.pie(
        [matched_count, unmatched_count],
        labels=["Matched", "Unmatched"],
        autopct="%1.1f%%",
        colors=["#4CAF50", "#F44336"]
    )
    plt.title("Passage Match vs Unmatched")
    plt.tight_layout()
    plt.savefig("docs/match_ratio_pie.png")
    plt.close()

