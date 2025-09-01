from aiogram import Dispatcher, types
from loader import dp, bot
from gtts import gTTS
import os

GREETING_AUDIO = "welcome.ogg"

# Generates greeting audio once
if not os.path.exists(GREETING_AUDIO):
    tts = gTTS("Welcome to TrustTalk. You can confess anonymously to offer help. Use the buttons below.", lang = "en")
    tts.save(GREETING_AUDIO)

@dp.message_handler(commands = ["start"])
async def start(message: types.Message):
    text = "👋 Welcome to the TrustTalk! Send your confession as voice or text."
    await message.answer(text)

    # Sends audio greeting
    with open(GREETING_AUDIO, "rb") as audio:
        await message.answer_voice(audio)
def register_handlers(dp:Dispatcher):
    dp.register_message_handler(start, commands=["start"])
