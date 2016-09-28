#!/usr/bin/python
# -*- coding: utf-8 -*-

from unidecode import unidecode
from pprint import pprint
import json
import requests
from utils import *


class UserInfo:
    def __init__(self, logger):
        self.logger = logger

    def handler(self, bot, update):
        user = update.message.from_user
        user_id = user.id
        chat_id = update.message.chat_id
        chat_member = bot.getChatMember(chat_id, user_id)
        first_name = user.first_name
        last_name = user.last_name
        username = user.username
        if not username:
            username = "Not specified"
        status = chat_member.status

        reply = ["User ID : " + str(user_id),
                 "Name : " + first_name + ' ' + last_name,
                 "Username : " + username,
                 "Status : " + status]
        bot.sendMessage(chat_id, '\n'.join(reply))
