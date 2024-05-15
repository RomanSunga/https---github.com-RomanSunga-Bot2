import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, F, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import app.keyboards as kb
import random
import requests
from bs4 import BeautifulSoup


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
   await message.answer_sticker('CAACAgIAAxkBAAEL8npmIW5tVf_A2HOIXh7e9dPVeSTYgwACVzIAAlZfGEuQ00oChUPYQzQE')
   await message.answer_sticker('CAACAgIAAxkBAAEL8nxmIW5xuuIVlSg1jbSReusrur94PQACKiUAAua_GUtodTWTfplsujQE')
   await message.answer_sticker('CAACAgIAAxkBAAEL8n5mIW5zwuVvP-4Gbt3dOCMmSJl4eAACuS8AAgS3EEuL1jlbFPjxTTQE')
   await message.answer(f'Привет,{message.from_user.first_name}, я бот который будет давать ссылку на аниме☢️',
                        reply_markup=kb.main)

@router.message(Command('help'))
async def inst_message(message: Message):
    await message.answer("Если вы хотите получить аниме, нажмите кнопку ПОЛУЧИТЬ. Так же вы можете получать аниме по вашему вкусу нажми кнопку ЗАРЕГИСТРИРОВАТЬСЯ.")


@router.message(F.text == 'Получить')
async def get_random_anime_link(message: Message):
    conn = sqlite3.connect('links.db')
    cursor = conn.cursor()
    cursor.execute("SELECT link FROM links ORDER BY RANDOM() LIMIT 1")
    random_anime_link = cursor.fetchone()
    if random_anime_link:
        await message.answer(f'Держи дорогой😘: {random_anime_link[0]}')
    else:
        await message.answer('К сожалению, в данный момент нет доступных ссылок на аниме😟')


def update_database():
    # Устанавливаем соединение с базой данных links.db
    conn = sqlite3.connect('links.db')
    cursor = conn.cursor()

    # Получаем HTML-код страницы
    url = 'https://studioband.info/tops.html'
    response = requests.get(url)
    html = response.content

    # Используем BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Находим все ссылки на аниме
    anime_links = soup.find_all('a', href=True)

    # Обновляем базу данных новыми ссылками
    for link in anime_links:
        cursor.execute("INSERT INTO links (link) VALUES (?)", (link['href'],))

    conn.commit()
    conn.close()

# Проверяем команду пользователя
@router.message(Command('update'))
async def update(message:Message):
    if message == "/update":
        update_database()
        print("База данных успешно обновлена!")
    else:
        print("Команда не распознана.")





@router.message(F.photo)
async def photo_message(message: Message):
    await message.reply("Следуй инструкции дебил🤡")

@router.message(F.text)
async def get_text(message: Message):
    await message.reply("Следуй инструкции дебил🤡")




