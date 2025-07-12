import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_vehicle_class_distribution(df_passage):
    plt.figure(figsize=(10, 5))
    sns.countplot(x='vehicle_class', data=df_passage)
    plt.title('Vehicle Class Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("docs/vehicle_class_distribution.png")
    plt.close()

def plot_passage_time_trend(df_passage):
    df_passage['hour'] = df_passage['timestamp'].dt.hour
    hourly = df_passage.groupby('hour').size()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=hourly.index, y=hourly.values)
    plt.title('Vehicle Passage Trend by Hour')
    plt.xlabel('Hour')
    plt.ylabel('Vehicle Count')
    plt.grid(True)
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
    plt.savefig("docs/match_ratio_pie.png")
    plt.close()

