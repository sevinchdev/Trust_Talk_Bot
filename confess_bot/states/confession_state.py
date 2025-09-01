from aiogram.dispatcher.filters.state import State, StatesGroup

class ConfessionStates(StatesGroup):
    waiting_for_voice = State()
    waiting_for_post_type = State()  #After transcription, bot asks whether to send voice or text