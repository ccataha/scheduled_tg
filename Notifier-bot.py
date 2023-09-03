from telegram import Bot
from telegram.ext import Updater
import schedule
import time
import asyncio
import yaml

with open("config.yml", 'r') as stream:
        config = yaml.safe_load(stream)

TOKEN = config['TOKEN']
CHAT_ID = config['CHAT_ID']
SCHEDULED_MESSAGE = config['SCHEDULED_MESSAGE']

async def send_message(bot, text):
    await bot.send_message(chat_id=CHAT_ID, text=text)

def task():
    asyncio.run(send_message(Bot(token=TOKEN), SCHEDULED_MESSAGE))

def main():
    schedule.every().day.at("06:59").do(task)
    schedule.every().day.at("10:59").do(task)
    schedule.every().day.at("15:59").do(task)
    schedule.every().day.at("20:59").do(task)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()