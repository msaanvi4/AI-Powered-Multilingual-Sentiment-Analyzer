import streamlit as st
import matplotlib.pyplot as plt

from src.sentiment import analyze_sentiment
from src.language_detector import detect_language
from src.file_processor import analyze_uploaded_text
from src.utils import emoji

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="AI-Powered Multilingual Sentiment Analyzer",
    page_icon="🌍",
    layout="wide"
)

# ==========================
# SIDEBAR
# ==========================
st.sidebar.title("🌍 Navigation")

page = st.sidebar.radio(
    "Choose a page",
    ["🏠 Home", "📂 Analyze File", "📊 Statistics", "ℹ About"]
)

# ==========================
# HOME
# ==========================
if page == "🏠 Home":

        st.title("🌍 AI-Powered Multilingual Sentiment Analyzer")   
        st.markdown("### AI Powered Language & Sentiment Detection")

    text = st.text_area("Enter a sentence", height=150)
    analyze = st.button("🚀 Analyze")

    if analyze:

        if text.strip() == "":
            st.warning("Enter text first!")
        else:
            with st.spinner("Analyzing..."):

                result = analyze_sentiment(text)

                sentiment = result["label"].lower()
                confidence = result["score"] * 100
                language = detect_language(text)

            st.success("Done!")

            c1, c2, c3 = st.columns(3)

            c1.metric("🌍 Language", language)
            c2.metric("😊 Sentiment", sentiment.capitalize())
            c3.metric("📊 Confidence", f"{confidence:.2f}%")

# ==========================
# ANALYZE FILE
# ==========================
elif page == "📂 Analyze File":

    st.title("📂 File Analysis")

    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

    if uploaded_file is not None:

        text = uploaded_file.read().decode("utf-8")

        with st.spinner("Analyzing..."):
            df = analyze_uploaded_text(text)

        st.success("Analysis Complete!")

        # ================= FILTERS =================
        st.subheader("🔍 Filters")

        col1, col2, col3 = st.columns(3)

        search = col1.text_input("Search")

        lang = col2.selectbox("Language", ["All"] + list(df["Language"].unique()))
        senti = col3.selectbox("Sentiment", ["All"] + list(df["Sentiment"].unique()))

        filtered = df.copy()

        if search:
            filtered = filtered[filtered["Sentence"].str.contains(search, case=False)]

        if lang != "All":
            filtered = filtered[filtered["Language"] == lang]

        if senti != "All":
            filtered = filtered[filtered["Sentiment"] == senti]

        # ================= STATS =================
        st.subheader("📊 Stats")

        pos = (filtered["Sentiment"] == "Positive").sum()
        neg = (filtered["Sentiment"] == "Negative").sum()
        neu = (filtered["Sentiment"] == "Neutral").sum()

        c1, c2, c3 = st.columns(3)

        c1.metric("😊 Positive", pos)
        c2.metric("😞 Negative", neg)
        c3.metric("😐 Neutral", neu)

        # ================= BAR CHART =================
        st.subheader("📊 Sentiment Distribution")

        counts = filtered["Sentiment"].value_counts()

        fig, ax = plt.subplots()
        ax.bar(counts.index, counts.values)
        st.pyplot(fig)

        # ================= PIE CHART =================
        st.subheader("🥧 Sentiment Breakdown")

        fig2, ax2 = plt.subplots()
        ax2.pie(counts.values, labels=counts.index, autopct="%1.1f%%")
        st.pyplot(fig2)

        # ================= TABLE =================
        st.subheader("📋 Results")

        st.dataframe(filtered, use_container_width=True)

        # ================= DOWNLOAD =================
        csv = filtered.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇ Download Results",
            csv,
            file_name="results.csv",
            mime="text/csv"
        )

# ==========================
# STATISTICS
# ==========================
elif page == "📊 Statistics":

    st.title("📊 Dashboard")

    st.info("Full analytics dashboard coming soon.")

# ==========================
# ABOUT
# ==========================
else:

    st.title("ℹ About")

    st.write("""
This project demonstrates:

- Multilingual Sentiment Analysis
- Hugging Face Transformers
- Streamlit Dashboard
- File Upload & Filtering
- Data Visualization
""")