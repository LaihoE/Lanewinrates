import numpy as np
import cv2
import pyautogui
import time
time.sleep(3)
for x in range(200,1000):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)

    cv2.imwrite(f"C:/Users/emill/PycharmProjects/lanewinrates/pics/{x}.png", image)
    print(x)
    time.sleep(1)
