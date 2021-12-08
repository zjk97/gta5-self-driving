#credit to python tutorial 
#https://pythonprogramming.net/next-steps-python-plays-gta-v/

import numpy as np
from screenReading import grab_screen
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D
import pyautogui
from getKeys import key_check


#the mask to save space and focus on lines. 
def region(img):
    mask = np.zeros_like(img)
    vertices = np.array([[0,600],[0,400], [200,200], [600,200], [800,400], [800,600], [500, 600], [500, 300], [300, 300], [300, 600], [0,600]], np.int32)
    cv2.fillPoly(mask, [vertices], 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

#convert keyboard input to onehot vectors 
def convert_to_onehot(keys):
    if "A" in keys:
        return [1, 0, 0, 0]
    elif "W" in keys:
        return [0, 1, 0, 0]
    elif "D":
        return [0, 0, 1, 0]
    else:
        return [0, 0, 0, 1]




def main():

    sample_number = 1
    train_data = []
    #last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    while True:
        screen = grab_screen(region=(0,40,800,600))

        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)

        screen = cv2.GaussianBlur(screen,(5,5),0)

        screen =  cv2.Canny(screen, 80, 200)

        screen = region(screen)

        screen = cv2.resize(screen, (80, 60))

        keyPressed = key_check()

        onehot = convert_to_onehot(keyPressed)
        # print(onehot)

        train_data.append([screen, onehot])
        
        if len(train_data) % 1000 == 0:
            print("the size of training data is: " + str(len(train_data)))
            if len(train_data) % 10000 == 0:
                file_name = "gta_train_data_{}.npy".format(sample_number)
                np.save(file_name, train_data)
                print("10 thousand samples achieved, saved")
                train_data = []
                sample_number += 1

        # curTime = time.time() - last_time
        # last_time = time.time()
        # print("grab screen took " + str(curTime))
if __name__ == '__main__':
    main()