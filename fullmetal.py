#!/usr/bin/python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, NetworkError)
import logging
from Handlers import *
import Handlers.utils

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
        logger.info("# remove update.message.chat_id from conversation list")
    except BadRequest:
        logger.info("# handle malformed requests - read more below!")
    except TimedOut:
        logger.info("# handle slow connection problems")
    except NetworkError:
        logger.info("# handle other connection problems")
    except TelegramError:
        logger.info("# handle all other telegram related errors")


def main():
    telegram_bot_token = utils.getValueFromJson("TelegramBotToken")
    updater = Updater(token=telegram_bot_token)
    dispatcher = updater.dispatcher

    define = Define(logger)
    define_handler = MessageHandler([define.filter], define.handler)
    dispatcher.add_handler(define_handler)

    url_shortner = UrlShortener(logger)
    url_shortner_handler = MessageHandler([url_shortner.filter], url_shortner.handler)
    dispatcher.add_handler(url_shortner_handler)

    url_shortner = UrlShortener(logger)
    url_shortner_handler = MessageHandler([url_shortner.filter], url_shortner.handler)
    dispatcher.add_handler(url_shortner_handler)

    google_search = GoogleSearch(logger)
    google_search_handler = MessageHandler([google_search.filter], google_search.handler)
    dispatcher.add_handler(google_search_handler)

    start = Start(logger)
    start_handler = CommandHandler('start', start.handler)
    dispatcher.add_handler(start_handler)

    user_info = UserInfo(logger)
    user_info_handler = CommandHandler('info', user_info.handler)
    dispatcher.add_handler(user_info_handler)

    unknown = Unknown(logger)
    unknown_handler = MessageHandler([Filters.command], unknown.handler)
    dispatcher.add_handler(unknown_handler)

    dispatcher.add_error_handler(error_callback)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
