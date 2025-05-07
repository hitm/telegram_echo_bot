import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
import os
print("Бот был автоматически перезапущен через GitHub webhook!")
TOKEN = "182639399:AAFY5sCAHF_1CUGQXlxLoqVjAicZ2f5UWTo"
WEBHOOK_URL = "https://knwldgs.ru/webhook"
WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = 8443

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)

async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(app):
    await bot.delete_webhook()

async def main():
    app = web.Application()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path="/webhook")
    setup_application(app, dp, bot=bot)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, WEBAPP_HOST, WEBAPP_PORT)
    await site.start()
    print(f"Bot running on https://knwldgs.ru/webhook")
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())

