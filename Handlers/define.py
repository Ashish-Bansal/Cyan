#!/usr/bin/python
# -*- coding: utf-8 -*-

from unidecode import unidecode
from pprint import pprint
import json
import requests
from utils import *


class Define:
    def __init__(self, logger):
        self.logger = logger

    def getWordMeaning(self, word):
        url = 'http://api.urbandictionary.com/v0/define?term=' + word
        response = requests.get(url).text
        definition = json.loads(response)['list'][0]['definition']
        return definition

    def handler(self, bot, update):
        message = update.message.text.lower()
        chat_id = update.message.chat_id
        message = removeBotName(message)
        message = ' '.join(message.split())

        try:
            word = ' '.join(message.split()[1:])
            definition = self.getWordMeaning(unidecode(word))
            bot.sendMessage(chat_id, definition)
        except IndexError:
            error_message = "Go learn the language first!"
            bot.sendMessage(chat_id, error_message)

    def filter(self, telegram_message):
        message = telegram_message.text
        if containsBotName(message) and containsAll(message, ['define']) :
            return True
        return False
