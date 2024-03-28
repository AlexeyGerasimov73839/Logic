#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("21176917", default=None, cast=int)
API_HASH = config("6fcbda80e78e7209a661c63f23d76c7b", default=None)
BOT_TOKEN = config("6437214223:AAE_ZJ2uu17Wu-lOkejNtvNL8c5x5qohtpE", default=None)
SESSION = config("BAFDIlUAw6J8FoO7iICcRlGsMTgrwTdEBQdtwlqgLbqTxz9wOv8xHzysyQClTCK3A46z2z8GZ2eoFYZtwoN8F2jW2g8XmyqEhsIJc7qSrb1VKfWhjugYCwZrzzwOqyGK9lE-8ZXBI44DS-zK7piSOTAUh-7YCGfc-Gj5__l6Svs9mPuOmwZ5PyOPAPGelqACH2h9YrvdR3Rk4xXaQj2eP0klxOmrwpyvtm27XUVQvEeuwLF4s3jCyHvHmHbSP-7ngqcCiz35kCcubyg_2YDJPqIjvT1-jMRr-HNoAE-7zjSMOxHfvpSLip2Sl4gIYrieqcJhr7SfpVnbj2yRNABLCKTfud2wTwAAAAGcDxs3AA", default=None)
FORCESUB = config("Oxicaine01", default=None)
AUTH = config("6913202999", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
