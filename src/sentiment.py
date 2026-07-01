from transformers import pipeline
import streamlit as st


@st.cache_resource
def load_model():
    print("Loading AI model...")

    return pipeline(
        "sentiment-analysis",
        model="cardiffnlp/twitter-xlm-roberta-base-sentiment"
    )


classifier = load_model()


def analyze_sentiment(text):
    return classifier(text)[0]