from telegram.bot import Bot
from telegram.ext import Updater,Dispatcher, CommandHandler, CallbackContext,MessageHandler
from telegram.ext.filters import Filters
from telegram.update import Update
import requests
import settings

# bot = Bot(token='5004960896:AAHdBx7XQ0Nju_vcputVTKd2hG-WD4uBhzo')
# print(bot.get_me())
updater = Updater(token=settings.TELEGRAM_TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Assalomu alaykum! Vikipediya botga xush kelibsiz! Biror maʼlumot izlash uchun /search "kalit so`z" yozing. Masalan /search Uzbekistan')

def search(update: Update, context: CallbackContext):
    args = context.args
    if len(args) == 0:
        update.message.reply_text('Hech bo`lmas nimadir kiriting. Malalan /search Uzbekistan')
    else:
        search_text = ' '.join(args)
        response = requests.get('https://uz.wikipedia.org/w/api.php',{
            'action':'opensearch',
            'search':search_text,
            'limit':1,
            'namespace':0,
            'format':'json',
        })
        result = response.json()
        link = result[3]
        if len(link):
            update.message\
                .reply_text('Sizning so`rovingiz bo`yicha havola: ' + link[0])
        else:

            update.message\
                .reply_text('Sizning so`rovingiz bo`yicha hech narsa topilmadi :(')

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
dispatcher.add_handler(MessageHandler(Filters.all, start))

updater.start_polling()
updater.idle()
