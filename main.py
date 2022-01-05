from telegram.bot import Bot
from telegram.ext import Updater,Dispatcher, CommandHandler, CallbackContext
from telegram.update import Update
import settings

# bot = Bot(token='5004960896:AAHdBx7XQ0Nju_vcputVTKd2hG-WD4uBhzo')
# print(bot.get_me())
updater = Updater(token=settings.TELEGRAM_TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Salom')
    context.bot.send_message(chat_id = update.message.chat_id, text = 'Salom yana bir bor')

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
