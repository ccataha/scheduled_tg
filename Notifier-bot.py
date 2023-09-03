from telegram import Bot
from telegram.ext import Updater
from datetime import datetime
import schedule
import time
import asyncio
import yaml
import logging

logging.basicConfig( format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

try:
        with open("config.yml", 'r') as stream:
                config = yaml.safe_load(stream)
        logging.info('Config loaded.')
except Exception as e:
        logging.error(f"Could not load config: {e}")
        exit

TOKEN = config['TOKEN']
CHAT_ID = config['CHAT_ID']
SCHEDULED_MESSAGE = config['SCHEDULED_MESSAGE']
logging.info('Variables loaded.')

async def send_message(bot, text):
    await bot.send_message(chat_id=CHAT_ID, text=text)

def task():
    asyncio.run(send_message(Bot(token=TOKEN), SCHEDULED_MESSAGE))
    logging.info(f"{datetime.now()} - message sent.")

def main():
    schedule.every().day.at("06:59").do(task)
    schedule.every().day.at("10:59").do(task)
    schedule.every().day.at("15:59").do(task)
    schedule.every().day.at("01:26").do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
