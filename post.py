from instabot import Bot
from login import *

bot = Bot()

bot.login(username = username, password = password)

bot.upload_photo("D:\Dev\Projetos\Covid\COVIDInstagramBot\img\covid.jpg",
				caption ="Covid test")
