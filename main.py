from src.statistics import show_statistics
from src.file_processor import analyze_file
from src.sentiment import analyze_sentiment
from src.language_detector import detect_language
from src.utils import emoji

while True:

    print("\n" + "=" * 50)
    print("🌍 MULTILINGUAL SENTIMENT ANALYZER")
    print("=" * 50)
    print("1. Analyze a sentence")
    print("2. Analyze a text file")
    print("3. View statistics ")
    print("4. Exit")

    choice = input("\nChoose an option (1-4): ")

    if choice == "4":
        print("\n👋 Thank you for using the analyzer!")
        break

    elif choice == "1":

        text = input("\nEnter a sentence: ")

        result = analyze_sentiment(text)

        sentiment = result["label"].lower()
        confidence = result["score"] * 100
        language = detect_language(text)

        print("\n" + "=" * 50)
        print("RESULT")
        print("=" * 50)
        print(f"Sentence   : {text}")
        print(f"Language   : {language}")
        print(f"Sentiment  : {emoji[sentiment]} {sentiment.capitalize()}")
        print(f"Confidence : {confidence:.2f}%")
        print("=" * 50)

    elif choice == "2":

        print("\nAnalyzing file...")

        df = analyze_file(
        "data/reviews.txt",
        "outputs/results.csv"
        )

        print("\nAnalysis Complete!\n")

        print(df)

        print("\nResults saved to outputs/results.csv")

    elif choice == "3":

        try:
            show_statistics("outputs/results.csv")
        except FileNotFoundError:
            print("\n❌ No analysis found.")
            print("Please analyze a text file first.")

    else:
        print("\n❌ Invalid choice. Please enter a number between 1 and 4.")