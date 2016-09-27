#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils import *


class Handler:
    def __init__(self, logger):
        self.logger = logger

    # Handler method to handle the current message
    def handler(self, bot, update):
        message = update.message.text
        chat_id = update.message.chat_id
        reply = "Hello World!"
        bot.sendMessage(chat_id, reply)

    # Returns True if this handler can handle this message
    # Only one handler will be able accept a message and accepted
    # message won't be passed to other handlers in the queue
    def filter(self, telegram_message):
        message = telegram_message.text
        if containsBotName(message) and containsAll(message, ['foobar']):
            return True
        return False
