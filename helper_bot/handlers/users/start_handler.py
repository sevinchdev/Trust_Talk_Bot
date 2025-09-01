from aiogram import types, Dispatcher
from loader import bot

async def start_helper(message: types.Message):
    # Extract confession_id if present
    args = message.get_args()
    if args:
        confession_id = args
        await message.answer(
            f"🤝 Welcome! You are offering help for confession ID: {confession_id}\n"
            "Please type your message, and we will forward it to the confessor."
        )
        # Save this confession_id in user state or database if needed
    else:
        await message.answer(
            "Welcome to HelperBot!\n\n"
            "Click 'Offer Help' under a confession in the channel to start helping someone."
        )

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_helper, commands=["start"])
