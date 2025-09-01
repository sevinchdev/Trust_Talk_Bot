from vosk import Model, KaldiRecognizer
import wave
import json
import os

MODEL_PATH = "vosk_models/vosk-model-small-en-us-0.15"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Vosk model not found at: {MODEL_PATH}")

# Load Vosk Model
model = Model(MODEL_PATH)

async def transcribe_audio(file_path):
    wf = wave.open(file_path, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in [8000, 16000, 44100]:
        raise ValueError("Audio file must be WAV mono PCM.")

    rec = KaldiRecognizer(model, wf.getframerate())
    result = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            result += res.get("text", "") + " "

    res = json.loads(rec.FinalResult())
    result += res.get("text", "")

    wf.close()
    return result.strip()
