import csv
from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import time

sqlEngine = create_engine('')
dbConnection = sqlEngine.connect()


def opggloop():
    champlist = ["DrMundo"]
    path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
    DRIVER_PATH = path
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    for champion in champlist:
        print(champion)
        url = f"https://u.gg/lol/champions/{champion}/matchups?patch=11_7"
        print(url)
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "rt-tr-group")))
        time.sleep(1)
        x=driver.find_element_by_class_name('rt-tbody').text

        mainchamp = driver.find_element_by_class_name('champion-name').text
        print(x)
        file1 = open("myfile.txt", "w")
        # \n is placed to indicate EOL (End of Line)
        print(x)
        file1.write(x)
        file1.close()
        champname=""
        wr=""
        matches=""
        name_step=9
        with open("myfile.txt", 'r+') as file:
            next(file)
            for counter,line in enumerate(file):
                line=line.strip('\n')
                if counter % name_step==0:
                    champname = line
                if (counter-1) % name_step==0:
                    wr=line
                if (counter-7) % name_step==0:
                    matches=line
                    df=pd.DataFrame([[champname,wr,matches]],columns=["champ","wr","matches"])
                    df.to_sql(name=f'{champion}', con=dbConnection, index=False, if_exists='append')
opggloop()