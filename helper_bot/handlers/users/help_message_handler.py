from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from loader import bot
from states.help_state import HelpStates

# The helper sends a message
async def receive_help_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    confessor_id = data.get("confessor_id")

    if not confessor_id:
        await message.answer("❌ Cannot find the confessor for this session.")
        return

    # Send helper's message anonymously to confessor
    await bot.send_message(
        chat_id=confessor_id,
        text=f"💌 Someone wants to help you:\n\n{message.text}"
    )

    await message.answer("✅ Your message has been delivered to the confessor!")
    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(receive_help_message, state=HelpStates.waiting_for_message)
