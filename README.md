# 🌍 AI-Powered Multilingual Sentiment Analyzer

An AI-powered web application that performs multilingual sentiment analysis using state-of-the-art Natural Language Processing (NLP) models. Built with **Hugging Face Transformers**, **Streamlit**, and **Python**, the application detects the language of the input text, predicts its sentiment, and provides interactive visualizations for both individual sentences and uploaded text files.

---

## ✨ Features

- 🌍 Supports multilingual sentiment analysis
- 🤖 AI-powered sentiment prediction using Hugging Face Transformers
- 🌐 Automatic language detection
- 📝 Analyze a single sentence in real time
- 📂 Upload and analyze `.txt` files
- 📊 Interactive statistics dashboard
- 📈 Sentiment distribution bar chart
- 🥧 Sentiment distribution pie chart
- 🔍 Filter results by language, sentiment, or keywords
- 📥 Export analysis results as CSV
- 💻 Clean and responsive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- Pandas
- Matplotlib
- LangDetect

---

## 📁 Project Structure

```
AI-Powered-Multilingual-Sentiment-Analyzer/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── sample_reviews.txt
│   └── reviews.txt
│
├── outputs/
│
└── src/
    ├── file_processor.py
    ├── language_detector.py
    ├── sentiment.py
    ├── utils.py
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/AI-Powered-Multilingual-Sentiment-Analyzer.git
```

Move into the project folder:

```bash
cd AI-Powered-Multilingual-Sentiment-Analyzer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📖 How to Use

### Single Sentence Analysis

1. Open the **Home** page.
2. Enter a sentence in any supported language.
3. Click **Analyze**.
4. View:
   - Detected language
   - Sentiment
   - Confidence score

---

### File Analysis

1. Open **Analyze File**.
2. Upload a `.txt` file.
3. View:
   - Analysis results
   - Statistics
   - Interactive charts
4. Download the results as a CSV file.

---

## 🌍 Supported Languages

The application supports multilingual sentiment analysis using a multilingual transformer model.

Examples include:

- 🇺🇸 English
- 🇮🇳 Hindi
- 🇮🇳 Tamil
- 🇮🇳 Telugu
- 🇮🇳 Kannada
- 🇮🇳 Malayalam
- 🇧🇩 Bengali
- 🇮🇳 Gujarati
- 🇮🇳 Marathi
- 🇮🇳 Punjabi
- 🇵🇰 Urdu
- 🇫🇷 French
- 🇩🇪 German
- 🇪🇸 Spanish
- 🇮🇹 Italian
- 🇵🇹 Portuguese
- 🇷🇺 Russian
- 🇯🇵 Japanese
- 🇰🇷 Korean
- 🇨🇳 Chinese
- 🇸🇦 Arabic

---

## 📊 Screenshots

### Home Page

*(Add screenshot after deployment.)*

---

### File Analysis

*(Add screenshot after deployment.)*

---

### Statistics Dashboard

*(Add screenshot after deployment.)*

---

## 🔮 Future Improvements

- PDF document analysis
- Excel and CSV uploads
- Dark mode
- Sentiment history
- User authentication
- REST API
- Model comparison dashboard
- Emotion detection
- Named Entity Recognition (NER)

---

## 👩‍💻 Author

**Saanvi Maharana**

GitHub:
https://github.com/YOUR_GITHUB_USERNAME

LinkedIn:
(Add your LinkedIn profile)

---

## 📄 License

This project is developed for learning, portfolio, and educational purposes.