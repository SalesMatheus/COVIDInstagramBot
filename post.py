from instabot import Bot
from login import *
import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint

bot = Bot()

bot.login(username = username, password = password)

PhotoPath = "D:\Dev\Projetos\Covid\COVIDInstagramBot\img"
IGCaption = "#programminglife #covid"
os.chdir(PhotoPath)
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])
print(ListFiles)
print("Total de fotos na pagina:" + str(len(ListFiles)))

for i, _ in enumerate(ListFiles):
    photo = ListFiles[i]
    print("Progresso :" + str([i + 1]) + " of " + str(len(ListFiles)))
    print("Publicando foto: " + photo)
    bot.upload_photo(photo, caption=IGCaption, upload_id=None)
    #os.remove(photo)
    n = randint(700,900)
    print("Sleep upload for seconds: " + str(n))
    time.sleep(n)

