import numpy as np
import cv2
import pyautogui
import time
time.sleep(3)
for x in range(200,1000):
    image = pyautogui.screenshot()

    # since the pyautogui takes as a
    # PIL(pillow) and in RGB we need to
    # convert it to numpy array and BGR
    # so we can write it to the disk
    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)
    # writing it to the disk using opencv
    #cv2.imwrite(f"C:/Users/emill/PycharmProjects/lanewinrates/pics/{x}", image)
    cv2.imwrite(f"C:/Users/emill/PycharmProjects/lanewinrates/pics/{x}.png", image)

    print(x)
    time.sleep(1)