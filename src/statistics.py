import pandas as pd
from src.charts import generate_chart


def show_statistics(csv_file):

    df = pd.read_csv(csv_file)

    positive = (df["Sentiment"] == "positive").sum()
    negative = (df["Sentiment"] == "negative").sum()
    neutral = (df["Sentiment"] == "neutral").sum()

    total = len(df)

    print("\n" + "=" * 50)
    print("📊 SENTIMENT STATISTICS")
    print("=" * 50)

    print(f"😊 Positive : {positive}")
    print(f"😞 Negative : {negative}")
    print(f"😐 Neutral  : {neutral}")

    print("-" * 50)
    print(f"📝 Total Reviews : {total}")
    print("=" * 50)

    generate_chart(csv_file)