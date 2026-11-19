"""Telegram clients and shared context."""
from telethon import TelegramClient
from telethon.sessions import StringSession

from . import config

user = TelegramClient(StringSession(config.SESSION_STRING), config.API_ID, config.API_HASH)
bot = TelegramClient(StringSession(), config.API_ID, config.API_HASH)
bot.parse_mode = "html"


class Ctx:
    owner = None
    bot_username = None


ctx = Ctx()
