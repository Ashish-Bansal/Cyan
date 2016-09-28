#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json

BOT_NAMES = ['cyan', 'baby', 'fullmetal']
TOP_LEVEL_DOMAIN_FILENAME = "tlds-alpha-by-domain.txt"
JSON_FILENAME = "api_keys.json"


def containsBotName(message):
    message = message.lower()
    for name in BOT_NAMES:
        if name in message:
            return True
    return False


def containsAll(message, words):
    lowercase_message = message.lower()
    for word in words :
        if word not in lowercase_message:
            return False
    return True


def removeBotName(message):
    words = message.split()
    for name in BOT_NAMES:
        if name in message:
            words.remove(name)
    return ' '.join(words)


def isUrl(possible_url):
    possible_url = possible_url.lower()
    if possible_url.startswith("http") or possible_url.startswith("ftp") :
        return True

    script_dir = os.path.dirname(__file__)
    abs_tlds_path = os.path.join(script_dir, TOP_LEVEL_DOMAIN_FILENAME)

    with open(abs_tlds_path) as f:
        for line in f:
            if line.startswith('#'):
                continue
            if possible_url.endswith(line.lower().strip('\t\n\r')):
                return True
    return False


def getValueFromJson(key_name):
    script_dir = os.path.dirname(__file__)
    abs_json_filepath = os.path.join(script_dir, JSON_FILENAME)
    values = json.loads(open(abs_json_filepath).read())
    return values[key_name]


def leaveGroup(bot, chat_id):
    bot.leaveChat(chat_id)


def kickFromGroup(bot, chat_id, user_id):
    bot_id = bot.id
    if isAdmin(bot, chat_id, bot_id):
        bot.kickChatMember(chat_id, user_id)
        return True
    else:
        return False


def unbanFromGroup(bot, chat_id, user_id):
    bot_id = bot.id
    if isAdmin(bot, chat_id, bot_id):
        bot.unbanChatMember(chat_id, user_id)
        return True
    else:
        return False


def isAdmin(bot, chat_id, user_id):
    chat_member = bot.getChatMember(chat_id, user_id)
    status = chat_member.status
    if status.lower() == "administrator":
        return True
    else:
        return False
