
import os
from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot
from utils.misc.speech_to_text import transcribe_audio
from states.confession_state import ConfessionStates
from aiogram.dispatcher import FSMContext
from keyboards.default.post_type_button import get_post_type_keyboard
from pydub import AudioSegment

TEMP_FOLDER = "temp_audio"
os.makedirs(TEMP_FOLDER, exist_ok=True)

async def handle_voice(message: types.Message, state: FSMContext):
    voice = message.voice

    # Download the voice file
    file = await message.bot.get_file(voice.file_id)
    file_path = file.file_path
    downloaded_file = await message.bot.download_file(file_path)

    # Save as OGG
    temp_ogg_path = os.path.join(TEMP_FOLDER, f"{voice.file_id}.ogg")
    with open(temp_ogg_path, "wb") as f:
        f.write(downloaded_file.read())

    # Convert OGG → WAV mono PCM
    from pydub import AudioSegment
    audio = AudioSegment.from_ogg(temp_ogg_path)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)
    temp_wav_path = os.path.join(TEMP_FOLDER, f"{voice.file_id}.wav")
    audio.export(temp_wav_path, format="wav", codec="pcm_s16le")

    # Transcribe
    text = await transcribe_audio(temp_wav_path)

    # Save in FSM
    await state.update_data(transcribed_text=text, voice_file_path=temp_ogg_path)

    # ✅ Set FSM state
    await ConfessionStates.waiting_for_post_type.set()

    # Asks user choice( with instructions)
    await message.answer(
        "✅ Your confession is ready.\n"
        "How do you want to send it?\n"
        "(Press the button 'Send as Voice' on the left-bottom of the screen to send your confession as voice message.\n"
        "Press the button 'Send as Text' on the right-bottom of the screen to send your confession as text message.)",
        reply_markup=get_post_type_keyboard()
    )

    # Moves to the next state
    await ConfessionStates.waiting_for_post_type.set()

    # Removes WAV
    os.remove(temp_wav_path)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_voice, content_types=types.ContentType.VOICE, state=None)
