from instabot import Bot
from login import *
import os
import time
from os import listdir
from os.path import isfile, join
from random import randint
from grafico import generator

bot = Bot()

bot.login(username = username, password = password)

PhotoPath = "D:\Dev\Projetos\Covid\COVIDInstagramBot\img"
IGCaption = "#programminglife #covid"
os.chdir(PhotoPath)
generator()
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])
print(ListFiles)
print("Total de fotos na pasta:" + str(len(ListFiles)))

for i, _ in enumerate(ListFiles):
    photo = ListFiles[i]
    print("Progresso :" + str([i + 1]) + " de " + str(len(ListFiles)))
    print("Carregando foto: " + photo)
    bot.upload_photo(photo, caption=IGCaption, upload_id=None)
    os.remove(photo +'.REMOVE_ME')

    # aguardar por 60 a 120s
    n = randint(60,120)
    print(n)
    print("Aguardando por : " + str(n) + " segundos")
    # time.sleep(n)

