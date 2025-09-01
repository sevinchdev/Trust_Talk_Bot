from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def create_help_button(post_owner_id: int) -> InlineKeyboardButton:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text = "🤝 Offer Help",
            callback_data= f"offer_help:{post_owner_id}"
        )
    )
    return keyboard