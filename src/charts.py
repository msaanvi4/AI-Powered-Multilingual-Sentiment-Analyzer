import matplotlib

# Use a non-GUI backend
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


def generate_chart(csv_file):

    df = pd.read_csv(csv_file)

    counts = df["Sentiment"].value_counts()

    plt.figure(figsize=(6, 4))

    plt.bar(counts.index, counts.values)

    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig("outputs/sentiment_chart.png")

    plt.close()

    print("\n📊 Chart saved to outputs/sentiment_chart.png")