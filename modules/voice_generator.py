from gtts import gTTS
import os

def generate_voice(text, filename, lang):
    # Mapping to Indian regional accents
    lang_map = {
        "en": "en-in", # Indian English
        "hi": "hi",    # Hindi
        "ur": "ur"     # Urdu
    }
    target_lang = lang_map.get(lang, "hi")

    try:
        tts = gTTS(text=text, lang=target_lang)
        os.makedirs("assets/audio", exist_ok=True)
        path = f"assets/audio/{filename}.mp3"
        tts.save(path)
        return path
    except Exception as e:
        print(f"Voice Error: {e}")
        return None