import logging
from telegram.ext import Application, MessageHandler, filters, ConversationHandler, CommandHandler
from telegram import ReplyKeyboardMarkup
from start_poll import *
import easy_poll

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)


def main():
    application = Application.builder().token("6060990323:AAFSzwlY3K7Tn2gac0bKKoe5Mn66nOMQo2o").build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_response)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_response)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    application.add_handler(CommandHandler("да", easy_poll.yes))
    application.add_handler(CommandHandler("нет", easy_poll.no))
    application.run_polling()
    reply_keyboard = [['/address', '/phone']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    application.add_handler(conv_handler)
    application.run_polling()





if __name__ == '__main__':
    main()
