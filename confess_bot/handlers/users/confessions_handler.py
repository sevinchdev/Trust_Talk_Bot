
import os
import uuid
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot
from states.confession_state import ConfessionStates
from keyboards.default.post_type_button import get_post_type_keyboard
from data.confessions_db import add_confession

CONFESSION_CHANNEL = "@TRUST_TALKK"  # Your confession channel username

# Inline button: View Post in Channel
def get_view_post_button():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            "🔗 View Post in Channel",
            url=f"https://t.me/{CONFESSION_CHANNEL.replace('@','')}"
        )
    )
    return keyboard

# Inline button: Offer Help
def get_offer_help_keyboard(confession_id: str):
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            "🤝 Offer Help",
            url=f"https://t.me/Trust_talk_help_bot?start={confession_id}"
        )
    )

# Handles user's choice: Send as Text or Send as Voice
async def process_post_choice(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = data.get("transcribed_text")
    voice_file_path = data.get("voice_file_path")

    # Generate unique confession ID
    confession_id = str(uuid.uuid4())
    add_confession(confession_id, message.from_user.id)

    # If the user chooses to send as text
    if message.text == "📝 Send as Text":
        await bot.send_message(
            chat_id=CONFESSION_CHANNEL,
            text=f"🕊 Anonymous confession:\n\n{text}",
            reply_markup=get_offer_help_keyboard(confession_id)
        )
        await message.answer(
            "✅ Your confession was sent as text.\n"
            "Below is a button to view it in the channel:",
            reply_markup=get_view_post_button()
        )

        # Delete the temporary voice file if it exists
        if voice_file_path and os.path.exists(voice_file_path):
            os.remove(voice_file_path)

    # If the user chooses to send as voice
    elif message.text == "🎤 Send as Voice":
        if voice_file_path and os.path.exists(voice_file_path):
            with open(voice_file_path, "rb") as voice:
                await bot.send_voice(
                    chat_id=CONFESSION_CHANNEL,
                    voice=voice,
                    caption="🕊 Anonymous confession:",
                    reply_markup=get_offer_help_keyboard(confession_id)
                )
            os.remove(voice_file_path)
            await message.answer(
                "✅ Your confession was sent as voice.\n"
                "Below is a button to view it in the channel:",
                reply_markup=get_view_post_button()
            )
        else:
            await message.answer("❌ Could not find the voice file.")

    await state.finish()

# Registering the handler
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(process_post_choice, state=ConfessionStates.waiting_for_post_type)
