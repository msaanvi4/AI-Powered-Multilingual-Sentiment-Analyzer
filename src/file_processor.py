import pandas as pd

from src.sentiment import analyze_sentiment
from src.language_detector import detect_language


def analyze_uploaded_text(text):

    lines = text.splitlines()

    results = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        result = analyze_sentiment(line)

        results.append({
            "Sentence": line,
            "Language": detect_language(line),
            "Sentiment": result["label"].capitalize(),
            "Confidence (%)": round(result["score"] * 100, 2)
        })

    return pd.DataFrame(results)