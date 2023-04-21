from telethon import functions, types
from telethon.sync import TelegramClient
from telethon import TelegramClient, sync
from telethon import TelegramClient, events, sync
from noir import *
import sqlite3

##
chats = [
    "https://t.me/tproger",
    "https://t.me/t0digital",
    "https://t.me/+6nb3N2eyqzkyNzI6",
    "https://t.me/journal_academy",
    "https://t.me/books_osint",
    "https://t.me/thecodemedia",
    "https://t.me/books_osint",
    "https://t.me/htmlacademy",
    "https://t.me/SQL_and_DB_Learning",
    "https://t.me/cppproglib",
    "https://t.me/csharpproglib",
    "https://t.me/rust_code",
    "https://t.me/golang_org",
    "https://t.me/itcour1",
    "https://t.me/railshub",
    "https://t.me/pascalabc_official",
    "https://t.me/Assembler_course",
    "https://t.me/usePerlOrDie",
    "https://telegram.me/modernperl",
    "https://t.me/javaproglib",
    "https://t.me/javaquize",
    "https://t.me/booksjava",
    "https://t.me/pythonist_ru",
    "https://t.me/pythonetc",
    "https://t.me/frontendInterview",
    "https://t.me/exploitex",
    "https://t.me/whackdoor",
    "https://t.me/dataleak",
    "https://t.me/tproger_official",
    "https://t.me/unilecs",
    "https://t.me/proglibrary",
    "https://t.me/techrocks",
    "https://t.me/nuancesprog",
    "https://t.me/ai_machinelearning_big_data",
    "https://t.me/cgallies",
    "https://t.me/zbrush_ru",
    "https://t.me/datalytx",
    "https://t.me/smart_data_channel",
    "https://t.me/disdoc",
    "https://t.me/kojima_calls",
    "https://t.me/backtracking",
    "https://telegram.me/forwebdev",

    ]

##chats = ["https://t.me/+6nb3N2eyqzkyNzI6"]

con = sqlite3.connect('users.db')
cur = con.cursor()
api_id = 21752276 
api_hash = "8ec899e56465c9343c09b2b35d153443"

client = TelegramClient("final", api_id, api_hash)
print(cur.execute("SELECT user, liked, disliked, muted, prev_channel FROM data").fetchall())


@client.on(events.NewMessage())
async def normal_handler(event):
    message = event.message
    ident = message.peer_id.user_id
    f = False
    for data in cur.execute("SELECT user, liked, disliked FROM data").fetchall():
        if data[0] == str(ident):
            f = True
            break
    if not f:
        add_user(ident)
        ent = await client.get_entity(int(ident))
        await client.send_message(ent, f'Здравствуй, новый пользователь. Напиши /help для объяснения того, кто я и что я такое)))')
    if message.message == '/help':
         await message.reply('you can /mute the bot to switch the notifications off and /unmute to switch the on. Type /clear_recs to clear the recommendations list')
    elif message.message == '/mute':
        await message.reply('notifications off')
        cur.execute(f"""UPDATE data
                   SET muted = 1
                   WHERE user = {str(ident)}""")
        con.commit()
##        calling a function which switches on messages to this guy
    elif message.message == '/unmute':
        await message.reply('notifications on')
        cur.execute(f"""UPDATE data
                   SET muted = 0
                   WHERE user = {str(ident)}""")
        con.commit()
##        calling a function which switches off messages to this guy
    elif message.message == '/like':
##        if was a chan before
        fff = cur.execute(f"SELECT user, liked, disliked, muted, prev_channel FROM data where user = {str(ident)}").fetchall()
        if fff[0][-1] != '':
            liked = fff[0][1].strip('[').strip(']') + ', ' + fff[0][-1]
            cur.execute(f"""UPDATE data
                       SET liked = '{str(liked).strip('[]')}'
                       WHERE user = {str(ident)}""")
            con.commit()
            await message.reply('we will try to show more such content')
        else:
            await message.reply('You have no post to assess for now ((((')        
    elif message.message == '/dislike':
##        as well as upper
        fff = cur.execute(f"SELECT user, liked, disliked, muted, prev_channel FROM data where user = {str(ident)}").fetchall()
        if fff[0][-1] != '':        
            disliked = fff[0][2].strip('[').strip(']')+ ', ' + fff[0][-1]
            print(disliked)
            cur.execute(f"""UPDATE data
                       SET disliked = '{str(disliked).strip('[]')}'
                       WHERE user = {str(ident)}""")
            con.commit()
            await message.reply('we will try to show less such content')
        else:
            await message.reply('You have no post to assess for now ((((')        

##        calling a function which adds this to non-reks
    elif message.message == '/clear_recs':
        await message.reply('recommendations are clear now')
        cur.execute(f"""UPDATE data
                   SET liked = '', disliked = ''
                   WHERE user = {str(ident)}""")
        con.commit()
    else:
        await message.reply('sorry, cannot get what you mean :). Use /help please.')
    
        
        



@client.on(events.NewMessage(chats=chats))

async def normal_handler(event):
    if isinstance(event.chat, types.Channel):
        username = event.chat.username
        await client.send_message("https://t.me/+iVaDWyzEnIowZDNi", f'A publication from: {event.chat.title}')
        await client.send_message("https://t.me/+iVaDWyzEnIowZDNi", event.message)
        idents = recipients(event.message)
        for i in idents:
            fff = cur.execute(f"SELECT user, disliked, muted FROM data where user = {i}").fetchall()
##            print(str(hash(event.chat.title)), fff[0][1].strip('[').strip(']').split(', '))
##            print(event.chat.title)
            if int(fff[0][2]) or str(event.chat.title) in fff[0][1].strip('[').strip(']').split(', '):
                continue
            else:
                ent = await client.get_entity(int(i))
                cur.execute(f"""UPDATE data
                           SET prev_channel = '{str(event.chat.title)}'
                           WHERE user = {str(i)}""")
                con.commit()
                await client.send_message(ent, f'A publication from: {event.chat.title}')
                await client.send_message(ent, event.message)
                await client.send_message(ent, f'type /like if you like such content and /dislike if not.')


client.start()
client.run_until_disconnected()
