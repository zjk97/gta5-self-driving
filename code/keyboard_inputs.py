#credit to python tutorial 
#https://pythonprogramming.net/next-steps-python-plays-gta-v/

import numpy as np
from screenReading import grab_screen
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D
import pyautogui





def region(img):
    mask = np.zeros_like(img)
    vertices = np.array([[0,600],[0,400], [200,200], [600,200], [800,400], [800,600], [500, 600], [500, 300], [300, 300], [300, 600], [0,600]], np.int32)
    cv2.fillPoly(mask, [vertices], 255)
    masked = cv2.bitwise_and(img, mask)
    return masked



def record_screen(image):
    #copy of image
    raw_image = np.copy(image)

    #change color to gray so that we can use canny edge detector.      
    screen = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
    #use gaussian blur to remove noises
    screen = cv2.GaussianBlur(screen,(5,5),0)

    # # edge detection
    screen =  cv2.Canny(screen, 80, 200)
        
    # #get partial screen. 
    screen = region(screen)

    return screen, raw_image


def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    while True:
        screen = grab_screen(region=(0,40,800,600))
        new_screen, _ = record_screen(screen)
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
if __name__ == '__main__':
    main()