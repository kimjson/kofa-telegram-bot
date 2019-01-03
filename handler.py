import datetime
import logging

from bs4 import BeautifulSoup
from models import Chat
import json
import os
import requests
import telegram
import time
import uuid

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


OK_RESPONSE = {
    'statusCode': 200,
    'headers': {'Content-Type': 'application/json'},
    'body': json.dumps('ok')
}
ERROR_RESPONSE = {
    'statusCode': 400,
    'body': json.dumps('Oops, something went wrong!')
}


def get_telegram_bot():
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    if not TELEGRAM_TOKEN:
        logger.error('The TELEGRAM_TOKEN must be set')
        raise NotImplementedError

    return telegram.Bot(TELEGRAM_TOKEN)


def webhook(event, context):
    bot = get_telegram_bot()
    logger.info('Event: {}'.format(event))

    if event.get('httpMethod') == 'POST' and event.get('body'):
        logger.info('Message received')
        message = telegram.Update.de_json(
            json.loads(event.get('body')), bot).message

        chat_id = message.chat.id
        received_text = message.text
        sent_text = None

        if received_text == '/start':
            sent_text = """안녕하세요. 이 봇은 한국영상자료원에 게시물(현재는 새로운 상영프로그램)이 업데이트될 때 알려주는 봇입니다.
            버그나 궁금한 점은 다음을 통해 제보해주세요: https://twitter.com/mrsteinkim."""

            Chat.create(telegram_id=chat_id)
            logger.info(f'Telegram user {chat_id} added')

        bot.sendMessage(chat_id=chat_id, text=sent_text)
        logger.info(f'Message sent: {sent_text}')

        return OK_RESPONSE

    return ERROR_RESPONSE


def run(event, context):
    current_time = datetime.datetime.now().time()
    name = context.function_name
    logger.info("Your cron function " + name + " ran at " + str(current_time))

    bot = get_telegram_bot()
    # get telegram users
