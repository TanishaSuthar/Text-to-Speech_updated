from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
import argostranslate.translate
import os
from gtts import gTTS
import uuid

app = FastAPI()

# Load installed languages once on startup
argostranslate.translate.load_installed_languages()

def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    installed_languages = argostranslate.translate.get_installed_languages()

    from_lang = next((lang for lang in installed_languages if lang.code == source_lang), None)
    to_lang = next((lang for lang in installed_languages if lang.code == target_lang), None)

    if not from_lang:
        raise Exception(f"Source language '{source_lang}' not installed.")
    if not to_lang:
        raise Exception(f"Target language '{target_lang}' not installed.")

    translation = from_lang.get_translation(to_lang)
    if not translation:
        raise Exception(f"No translation installed from '{source_lang}' to '{target_lang}'.")

    return translation.translate(text)


@app.post("/text-to-speech/")
async def text_to_speech(
    text: str = Form(...),
    source_lang: str = Form(...),  # e.g. 'en' or 'hi'
    target_lang: str = Form(...)   # e.g. 'hi' or 'en'
):
    # Step 1: Translate the text
    translated_text = translate_text(text, source_lang, target_lang)

    # Step 2: Convert translated text to speech
    tts = gTTS(text=translated_text, lang=target_lang)
    os.makedirs("audio", exist_ok=True)
    filename = f"audio/{uuid.uuid4()}.mp3"
    tts.save(filename)

    # Step 3: Return the audio file as response
    return FileResponse(filename, media_type="audio/mpeg", filename="speech.mp3")

@app.get("/")
def home():
    return {"message": "Text-to-Speech Translator API is running. Use /docs for API docs."}
