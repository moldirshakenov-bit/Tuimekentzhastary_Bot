import asyncio
import os
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# Получаем токен из переменных окружения
TOKEN = "8286523290:AAHHCNQmARWrXDQk44Hy-GnNwkhl2qQvTXs"

# Инициализация диспетчера
dp = Dispatcher()

# Функция для создания главной клавиатуры
def get_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="О нас"),
                KeyboardButton(text="Направления")
            ],
            [
                KeyboardButton(text="Контакты")
            ]
        ],
        resize_keyboard=True, # Подгоняет размер кнопок
        input_field_placeholder="Выберите нужный раздел..."
    )

# Обработчик команды /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в <b>Молодежный ресурсный центр!</b> 🎉\n\n"
        "Выберите интересующий вас раздел в меню ниже:",
        reply_markup=get_main_keyboard()
    )

# Обработчик кнопки "О нас"
@dp.message(F.text == "О нас")
async def process_about(message: Message):
    text = (
        "🏢 <b>О нас</b>\n\n"
        "Молодежный ресурсный центр — это открытое пространство для реализации инициатив, "
        "поддержки талантов и развития молодежи. Мы помогаем молодым людям "
        "найти свое призвание, получить новые навыки и воплотить идеи в жизнь."
    )
    await message.answer(text)

# Обработчик кнопки "Направления"
@dp.message(F.text == "Направления")
async def process_directions(message: Message):
    text = (
        "🎯 <b>Наши основные направления:</b>\n\n"
        "1. <b>Волонтерство</b> — социальные, экологические и культурные проекты.\n"
        "2. <b>Трудоустройство</b> — помощь в поиске работы, стажировки и профориентация.\n"
        "3. <b>Досуг и спорт</b> — творческие кружки, спортивные секции и турниры.\n"
        "4. <b>Психологическая и юр. поддержка</b> — бесплатные консультации для молодежи."
    )
    await message.answer(text)

# Обработчик кнопки "Контакты"
@dp.message(F.text == "Контакты")
async def process_contacts(message: Message):
    text = (
        "📞 <b>Наши контакты:</b>\n\n"
        "📍 <b>Адрес:</b> ул. Толе би, д. 1\n"
        "☎️ <b>Телефон:</b> +7 (727) XXX-XX-XX\n"
        "📧 <b>Email:</b> info@mrc.kz\n"
        "🕒 <b>Режим работы:</b> Пн-Пт, 09:00 - 18:00\n\n"
        "🌐 <i>Следите за нами в социальных сетях: @mrc_youth</i>"
    )
    await message.answer(text)

# Главная функция запуска
async def main():
    # Проверка наличия токена
    if not TOKEN:
        print("Ошибка: Переменная окружения BOT_TOKEN не задана!")
        sys.exit(1)
        
    # Инициализация бота с дефолтным форматированием HTML
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    print("Бот успешно запущен...")
    # Запуск поллинга (прослушивания обновлений)
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запуск асинхронного приложения
    asyncio.run(main())
