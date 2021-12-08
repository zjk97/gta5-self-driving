#credit to python tutorial 
#https://pythonprogramming.net/next-steps-python-plays-gta-v/

import numpy as np
from screenReading import grab_screen
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D
import pyautogui




def draw_lines(img,lines):
    if lines is not None:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 3)


def region(img):
    mask = np.zeros_like(img)
    vertices = np.array([[0,600],[0,400], [200,200], [600,200], [800,400], [800,600], [500, 600], [500, 300], [300, 300], [300, 600], [0,600]], np.int32)
    cv2.fillPoly(mask, [vertices], 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def average(image, lines):
    left =[]
    right =[]
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        y_int = parameters[1]
        if slope < 0:
            left.append((slope, y_int))
        else:
            right.append((slope, y_int))
    right_avg = np.average(right, axis=0)
    left_avg = np.average(left, axis=0)
    left_line = make_points(image, left_avg)
    right_line = make_points(image, right_avg)
    return np.array([left_line, right_line])

def make_points(image, average):
    slope, y_int = average 
    y1 = image.shape[0]
    y2 = int(y1 * (3/5))
    x1 = int((y1 - y_int) // slope)
    x2 = int((y2 - y_int) // slope)
    return np.array([x1, y1, x2, y2])

def display_lines(image, lines):
    if lines is not None:
        for line in lines:
            coords = line[0]
            cv2.line(image, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 3)

def record_screen(image):
    #copy of image
    raw_image = np.copy(image)

    #change color to gray so that we can use canny edge detector.      
    screen = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
    #reduce the size of the input frame. 
    

    #use gaussian blur to remove noises
    screen = cv2.GaussianBlur(screen,(5,5),0)

    # # edge detection
    screen =  cv2.Canny(screen, 80, 200)
        
    # #get partial screen. 
    screen = region(screen)

    #get lines
    #lines = cv2.HoughLinesP(screen, 2, np.pi/180, 100, np.array([]), minLineLength=30, maxLineGap=15)

    #draw_lines(screen, lines)
    
    # average_line = average(raw_image, lines)
        
    # display_lines(raw_image, lines)

    return screen, raw_image


def main():
    
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    while True:
        screen = grab_screen(region=(0,40,800,600))
        new_screen, raw_image = record_screen(screen)
        #new_screen = cv2.resize(new_screen, (80, 60))
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
if __name__ == '__main__':
    main()