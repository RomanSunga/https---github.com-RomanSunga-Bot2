from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Получить')],
    [KeyboardButton(text='Зарегистрироваться'), KeyboardButton(text='Обновить аниме')]
],                                                             

                                resize_keyboard= True,
                                input_field_placeholder = 'Нажми кнопку милый')











