#!/usr/bin/python
# -*- coding: utf-8 -*-

from unidecode import unidecode
from pprint import pprint
import json
import requests
from utils import *


class Say:
    def __init__(self, logger):
        self.logger = logger

    def handler(self, bot, update):
        message = update.message.text.lower()
        chat_id = update.message.chat_id
        message = removeBotName(message)
        message = ' '.join(message.split())

    def filter(self, telegram_message):
        message = telegram_message.text
        if containsBotName(message) and containsAll(message, ['define']) :
            return True
        return False
