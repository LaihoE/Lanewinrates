import cv2
import pyautogui
import numpy as np
import time
import os
import pandas as pd
import pymysql
method = cv2.TM_SQDIFF_NORMED
from sqlalchemy import create_engine
sqlEngine = create_engine('')
dbConnection = sqlEngine.connect()
import mysql.connector
import pyscreenshot as ImageGrab

mydb = mysql.connector.connect(
)

blue_players=[]
red_players=[]

while True:
    print("---------------------------------------------------------------------------")
    image = ImageGrab.grab(bbox=(10, 50, 150, 600))
    screenshot = cv2.cvtColor(np.array(image),
                              cv2.COLOR_RGB2BGR)
    for filename in os.listdir('C:/Users/emill/PycharmProjects/lanewinrates/cleanpics/'):
        if filename.endswith(".png"):
            small_image = cv2.imread(f"C:/Users/emill/PycharmProjects/lanewinrates/cleanpics/{filename}")
            result = cv2.matchTemplate(small_image, screenshot, method)
            # We want the minimum squared difference
            mn, _, mnLoc, _ = cv2.minMaxLoc(result)
            if mn < 0.01:
                player=filename[:-4]
                if player not in blue_players:
                    blue_players.append(player)
        else:
            continue

    image = ImageGrab.grab(bbox=(1150, 50, 1250, 600))
    screenshot = cv2.cvtColor(np.array(image),
                              cv2.COLOR_RGB2BGR)
    for filename in os.listdir('C:/Users/emill/PycharmProjects/lanewinrates/cleanpics/'):
        if filename.endswith(".png"):

            small_image = cv2.imread(f"C:/Users/emill/PycharmProjects/lanewinrates/cleanpics/{filename}")
            result = cv2.matchTemplate(small_image, screenshot, method)
            # We want the minimum squared difference
            mn, _, mnLoc, _ = cv2.minMaxLoc(result)
            if mn < 0.001:
                player=filename[:-4]
                if player not in red_players:
                    red_players.append(player)
        else:
            continue

    for teammate in blue_players:
        teammate_list=[]
        matches=0
        champ=""
        wr=""
        mycursor = mydb.cursor()
        mycursor.execute(f'SELECT * FROM {teammate} WHERE champ="{red_players[0]}" or champ="{red_players[1]}" or champ="{red_players[2]}" or champ="{red_players[3]}" or champ="{red_players[4]}"')
        myresult = mycursor.fetchall()
        print(teammate,myresult)
        teammate_list.append(myresult)

    time.sleep(0.1)




