from aiogram.dispatcher.filters.state import State, StatesGroup

class HelpStates(StatesGroup):
    waiting_for_message = State()
