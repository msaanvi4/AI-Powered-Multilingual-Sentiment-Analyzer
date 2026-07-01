from langdetect import detect

languages = {
    "en": "🇺🇸 English",
    "hi": "🇮🇳 Hindi",
    "ta": "🇮🇳 Tamil",
    "te": "🇮🇳 Telugu",
    "kn": "🇮🇳 Kannada",
    "ml": "🇮🇳 Malayalam",
    "bn": "🇧🇩 Bengali",
    "gu": "🇮🇳 Gujarati",
    "mr": "🇮🇳 Marathi",
    "pa": "🇮🇳 Punjabi",
    "ur": "🇵🇰 Urdu",
    "fr": "🇫🇷 French",
    "de": "🇩🇪 German",
    "es": "🇪🇸 Spanish",
    "it": "🇮🇹 Italian",
    "pt": "🇵🇹 Portuguese",
    "ru": "🇷🇺 Russian",
    "ja": "🇯🇵 Japanese",
    "ko": "🇰🇷 Korean",
    "zh": "🇨🇳 Chinese",
    "ar": "🇸🇦 Arabic"
}


def detect_language(text):
    try:
        code = detect(text)
        return languages.get(code, f"🌍 {code.upper()}")
    except:
        return "Unknown"