#!/usr/bin/python
# -*- coding: utf-8 -*-


class Start :
    def __init__(self, logger):
        self.logger = logger

    def handler(self, bot, update):
        chat_id = update.message.chat_id
        start_message = ["I'm Cyan",
                         "I'm a natural talking bot, but still in development process.",
                         "For starters, I know few stuffs :",
                         "- define <word>",
                         "- shorten url [url.short]"]
        bot.sendMessage(chat_id, '\n'.join(start_message))
