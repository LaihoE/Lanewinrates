import cv2
import numpy
import pyautogui
import time

for i in range(380,606):
    pic=cv2.imread(f"C:/Users/emill/PycharmProjects/lanewinrates/pics/{i}.png")
    crop_img = pic[450:470, 710:730]
    cv2.imwrite(f"C:/Users/emill/PycharmProjects/lanewinrates/cleanpics/{i}.png", crop_img)



