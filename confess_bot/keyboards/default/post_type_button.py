from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_post_type_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard=True)
    keyboard.add(
        KeyboardButton("🎤 Send as Voice"),
        KeyboardButton("📝 Send as Text")
    )
    return keyboard
