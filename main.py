print("Scanner started")

import constants as keys
from telegram.ext import *
import yahoofinancescraper as yfs
from telegram import *
import requests
import bs4
import time

bot = Bot(keys.API_KEY)
def start_command(update, context):
    update.message.reply_text('Welcome to CSB news scanner! /scrape to start the scanner')

def scrape_function(update, context):   
    while True:
        del yfs.news[:]
        yfs.scrape()

        if yfs.news != yfs.latest_news:
            yfs.sort()
            bot.send_message(chat_id=update.effective_chat.id, text=yfs.news[0])
    
        else:
            pass
        
        time.sleep(5)
    


def main():


    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))

    dp.add_handler(CommandHandler("scrape", scrape_function))

    updater.start_polling()
    updater.idle()

main()