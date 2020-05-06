import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI

PhotoPath = "C:/Users/Matheus/Desktop/covid"
IGUSER = "botcovidinstagram@gmail.com"
PASSWD = "7iCbnGnCJeWXCP7"


IGCaption = "#covid"
os.chdir(PhotoPath)
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])
print(ListFiles)
print("Total Photo in this folder:" + str(len(ListFiles)))


igapi = InstagramAPI(IGUSER, PASSWD)
igapi.login()


for i, _ in enumerate(ListFiles):
    photo = ListFiles[i]
    print("Progress :" + str([i + 1]) + " of " + str(len(ListFiles)))
    print("Now Uploading this photo to instagram: " + photo)
    igapi.uploadPhoto(photo, caption=IGCaption, upload_id=None)
    os.remove(photo)

    n = randint(700,900)
    print("Sleep upload for seconds: " + str(n))
    time.sleep(n) 