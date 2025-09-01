from aiogram import executor
from loader import dp
from handlers.users import start_handler, help_message_handler

start_handler.register_handlers(dp)
help_message_handler.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
