#!/usr/bin/python
# -*- coding: utf-8 -*-

from unidecode import unidecode
from pprint import pprint
import json
import requests
from telegram import Message
from utils import *


class UrlShortener:
    API_KEY_NAME = 'GoogleUrlShortener'
    API_URL = 'https://www.googleapis.com/urlshortener/v1/url?key=' + getValueFromJson(API_KEY_NAME)

    def __init__(self, logger):
        self.logger = logger

    def handler(self, bot, update):
        message = update.message.text.lower().strip()
        chat_id = update.message.chat_id
        message = removeBotName(message)
        words = message.split()

        reply = list()
        for word in words:
            if isUrl(word):
                reply.append(word + " => " + self.getShortUrl(word))

        if not reply:
            reply.append("Are you fu*king kidding me ?")
            reply.append("There's no URL in the given text")

        bot.sendMessage(chat_id, '\n'.join(reply))

    def getShortUrl(self, url):
        header = {'Content-Type': 'application/json'}
        param = json.dumps({'longUrl': url})
        response = requests.post(self.API_URL, param, headers=header)
        return unidecode(response.json()['id'])

    def filter(self, telegram_message):
        message = telegram_message.text
        if containsBotName(message) and containsAll(message, ['short', 'url']):
            return True
        return False
