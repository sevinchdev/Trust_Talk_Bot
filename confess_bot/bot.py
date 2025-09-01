from aiogram import executor
from loader import dp
import logging

# Import handlers
from handlers.users import start_handler, voice_handler, confessions_handler

# Register handlers
start_handler.register_handlers(dp)
voice_handler.register_handlers(dp)
confessions_handler.register_handlers(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

