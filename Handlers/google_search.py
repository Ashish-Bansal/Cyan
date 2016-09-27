#!/usr/bin/python
# -*- coding: utf-8 -*-

from unidecode import unidecode
from pprint import pprint
import json
import requests
from telegram import Message
from utils import *

class GoogleSearch:
    # Based on 1-index
    START = 1
    API_KEY_NAME = 'GoogleCustomSearch'
    API_SECRET = getValueFromJson(API_KEY_NAME)
    CUSTOM_SEARCH_ENGINE_ID_NAME = "GoogleCustomSearchEngineId"
    CUSTOM_SEARCH_ENGINE_ID = getValueFromJson(CUSTOM_SEARCH_ENGINE_ID_NAME)
    RESULT_COUNT = 5

    def __init__(self, logger):
        self.logger = logger

    def handler(self, bot, update):
        message = update.message.text.lower().strip()
        chat_id = update.message.chat_id
        message = removeBotName(message)
        query = ' '.join(message.split()[1:])

        reply = self.getSearchResults(query)
        if not reply :
            reply.append("Do you live in Hell ?")
            reply.append("There's no such thing in this world.")
        bot.sendMessage(chat_id, '\n'.join(reply))

    def getSearchResults(self, query):
        header = {'Content-Type': 'application/json'}
        request_url = self.getRequestUrl(str(self.START), str(self.RESULT_COUNT), query)
        response = requests.get(request_url, headers=header)
        search_results = response.json()['items']
        results = list()
        count = 0
        while count < self.RESULT_COUNT:
            results.append('-' * 8)
            results.append(search_results[count]['title'])
            results.append(search_results[count]['link'])
            count += 1
        return results

    def getRequestUrl(self, start, count, query):
        url = ['https://www.googleapis.com/customsearch/v1?',
               'cx=', self.CUSTOM_SEARCH_ENGINE_ID,
               '&num=', count,
               '&start=', start,
               '&key=', self.API_SECRET,
               '&q=', query]
        return ''.join(url)

    def filter(self, telegram_message):
        message = telegram_message.text
        if containsBotName(message) and containsAll(message, ['search']) :
            return True
        return False
