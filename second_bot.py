# Импортируем необходимые классы.
import logging
from telegram.ext import Application, MessageHandler, filters
import sqlite3


BOT_TOKEN = '6010071125:AAHKwsxUvnBIBpHe-W7Oi3CTfbuaObE_Bc0'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def echo(update, context):
    con = sqlite3.connect('users.db')
    cur = con.cursor()    
    text = update.message.text
    ident = update.message.from_user.id
    f = False
    for data in cur.execute("SELECT user, liked, disliked FROM data"):
        if data[0] == str(ident):
            f = True
            break
    if not f:
        pass
##        add_user(ident)
    if text == '/help':
         await update.message.reply_text('you can /mute the bot to switch the notifications off and /unmute to switch the on')
    elif text == '/mute':
        await update.message.reply_text('notifications off')
##        calling a function which switches on messages to this guy
    elif text == '/unmute':
        await update.message.reply_text('notifications on')
##        calling a function which switches off messages to this guy
    elif text == '/like':
        await update.message.reply_text('we will try to show more such content')
##        calling a function which addes this to reks
    elif text == '/dislike':
        await update.message.reply_text('we will try to show less such content')
##        calling a function which adds this to non-reks
    else:
        await update.message.reply_text('sorry, cannot get what you mean :). Use /help please.')


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
