from instabot import Bot
from login import *
import os
import time
from os import listdir
from os.path import isfile, join
from random import randint
from generator import generator
import rootpath

Path = rootpath.detect()

bot = Bot()

bot.login(username = username, password = password)

while True:
    PhotoPath = Path + "/BotUploads"
    IGCaption = "#programminglife #covid"
    os.chdir(PhotoPath)
    generator()
    ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])
    print(ListFiles)
    print("Total de fotos na pasta: " + str(len(ListFiles)))

    c = 0

    for i, _ in enumerate(ListFiles):

            c += 1
            photo = ListFiles[i]
            print("Progresso :" + str([i + 1]) + " de " + str(len(ListFiles)))
            print("Carregando foto: " + photo)
            bot.upload_photo(photo, caption=IGCaption, upload_id=None)
            os.remove(photo + '.REMOVE_ME')

            if c < len(ListFiles):
                # aguardar por 60 a 120s
                n = randint(10, 20)
                print(f"Aguardando por : {n} segundos")
                time.sleep(n)

            if c == len(ListFiles):
                print("Uploads Finalizados! Aguardando por 24 horas para novas atualizações.")
                time.sleep(86400)