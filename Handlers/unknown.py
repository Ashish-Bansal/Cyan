#!/usr/bin/python
# -*- coding: utf-8 -*-

from unidecode import unidecode
from pprint import pprint
import json
import requests
from utils import *
from random import shuffle


class Unknown:
    start = 0
    replies = ["I'm not obliged to answer you bitch",
               "How dare you to command me like this ?"]

    def __init__(self, logger):
        self.logger = logger
        shuffle(self.replies)

    def handler(self, bot, update):
        chat_id = update.message.chat_id
        if self.start == len(self.replies):
            self.start = 0
        bot.sendMessage(chat_id, self.replies[self.start])
        self.start += 1
