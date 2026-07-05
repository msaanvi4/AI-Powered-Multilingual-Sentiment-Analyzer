import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from src.sentiment import analyze_sentiment
from src.language_detector import detect_language
from src.csv_sources import extract_text_entries
from src.file_processor import analyze_uploaded_text
from src.utils import emoji

st.set_page_config(
    page_title="AI-Powered Multilingual Sentiment Analyzer",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
<style>
.block-container {padding-top:2rem;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🌍 Navigation")
page = st.sidebar.radio(
    "Choose a page",
    ["🏠 Home", "📂 Analyze File", "📊 Statistics", "ℹ About"]
)

if page == "🏠 Home":
    st.title("🌍 AI-Powered Multilingual Sentiment Analyzer")
    st.markdown("### AI Powered Language & Sentiment Detection")

    left, right = st.columns([2,1])

    with left:
        text = st.text_area(
            "Enter a sentence",
            height=180,
            placeholder="Type a sentence in any supported language..."
        )
        analyze = st.button("🚀 Analyze")

    with right:
        st.info("""
### Features
- 🌍 Language Detection
- 😊 Sentiment Analysis
- 🤖 Hugging Face Model
- ⚡ Fast Inference
""")

    if analyze:
        if not text.strip():
            st.warning("Please enter some text.")
        else:
            with st.spinner("Analyzing..."):
                result = analyze_sentiment(text)
                sentiment = result["label"].lower()
                confidence = result["score"] * 100
                language = detect_language(text)

            st.success("Analysis Complete!")

            c1, c2, c3 = st.columns(3)
            c1.metric("🌍 Language", language)
            c2.metric("😊 Sentiment", f"{emoji.get(sentiment,'')} {sentiment.capitalize()}")
            c3.metric("📊 Confidence", f"{confidence:.2f}%")

elif page == "📂 Analyze File":
    st.title("📂 Analyze Text File")

    uploaded_file = st.file_uploader(
        "Upload a .txt or .csv file",
        type=["txt", "csv"]
    )

    if uploaded_file is not None:
        if uploaded_file.name.lower().endswith(".csv"):
            try:
                rows = extract_text_entries(pd.read_csv(uploaded_file))
                text = "\n".join(rows)
            except ValueError as error:
                st.error(f"Could not load CSV: {error}")
                st.stop()
        else:
            text = uploaded_file.read().decode("utf-8")

        with st.spinner("Analyzing file..."):
            df = analyze_uploaded_text(text)

        st.success("Analysis Complete!")

        st.subheader("🔍 Filters")
        col1, col2, col3 = st.columns(3)

        search = col1.text_input("Search")
        lang = col2.selectbox("Language", ["All"] + sorted(df["Language"].unique().tolist()))
        senti = col3.selectbox("Sentiment", ["All"] + sorted(df["Sentiment"].unique().tolist()))

        filtered = df.copy()

        if search:
            filtered = filtered[
                filtered["Sentence"].str.contains(search, case=False, na=False)
            ]

        if lang != "All":
            filtered = filtered[filtered["Language"] == lang]

        if senti != "All":
            filtered = filtered[filtered["Sentiment"] == senti]

        st.subheader("📊 Statistics")
        pos = (filtered["Sentiment"] == "Positive").sum()
        neg = (filtered["Sentiment"] == "Negative").sum()
        neu = (filtered["Sentiment"] == "Neutral").sum()

        a, b, c = st.columns(3)
        a.metric("😊 Positive", pos)
        b.metric("😞 Negative", neg)
        c.metric("😐 Neutral", neu)

        counts = filtered["Sentiment"].value_counts()

        st.subheader("📊 Sentiment Distribution")
        fig, ax = plt.subplots(figsize=(6,4))
        ax.bar(counts.index, counts.values)
        ax.set_xlabel("Sentiment")
        ax.set_ylabel("Count")
        st.pyplot(fig)

        st.subheader("🥧 Sentiment Breakdown")
        fig2, ax2 = plt.subplots(figsize=(5,5))
        ax2.pie(counts.values, labels=counts.index, autopct="%1.1f%%")
        st.pyplot(fig2)

        st.subheader("📋 Results")
        st.dataframe(filtered, use_container_width=True)

        csv = filtered.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇ Download Results",
            csv,
            file_name="results.csv",
            mime="text/csv"
        )

elif page == "📊 Statistics":
    st.title("📊 Statistics Dashboard")
    st.info("Upload a text file in the 'Analyze File' page to view interactive statistics and charts.")

else:
    st.title("ℹ About")
    st.markdown("""
## AI-Powered Multilingual Sentiment Analyzer

This application uses Hugging Face Transformers to analyze sentiment across multiple languages.

### Features
- 🌍 Automatic Language Detection
- 😊 AI Sentiment Analysis
- 📂 Batch Text File Analysis
- 📊 Interactive Charts
- 📥 CSV Export

### Tech Stack
- Python
- Streamlit
- Hugging Face Transformers
- Pandas
- Matplotlib
- LangDetect
""")
