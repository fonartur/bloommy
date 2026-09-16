from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

TOKEN="XXXXXXX"
BD="sqlite:///db.db"
ADMIN_ID="1028962949"

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
