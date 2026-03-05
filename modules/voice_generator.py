from gtts import gTTS
import os

def generate_voice(text, filename, lang):

    if lang not in ["en","hi","ur"]:
        lang = "en"

    tts = gTTS(text=text, lang=lang)

    os.makedirs("assets/audio", exist_ok=True)

    path = f"assets/audio/{filename}.mp3"

    tts.save(path)

    return path