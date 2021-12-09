import numpy as np
from numpy.core.fromnumeric import argmax
# from tensorflow import keras
from screenReading import grab_screen
import cv2
import time
# from directkeys import PressKey,ReleaseKey, W, A, S, D
# import gta
# from getKeys import key_check
import commandlist
from keyboard_inputs import record_screen
from tensorflow.keras import models
import tensorflow as tf

def main():
    WIDTH = 800
    HEIGHT = 600
    MODEL_NAME = "pygta5-car-fast-0.01-alexnetv2-4-epochs-400K-data.model"
    
    model = models.load_model(MODEL_NAME)
    
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    while True:
        screen = grab_screen(region=(0,40,800,600))
        new_screen, _ = record_screen(screen)

        # cv2.imshow('window', new_screen)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break

        new_screen = cv2.resize(new_screen, (800, 600))

        new_screen = np.asarray(new_screen).reshape(-1,WIDTH,HEIGHT,1)
        new_screen = tf.convert_to_tensor(new_screen, dtype=tf.float64)

        prediction = model.predict(new_screen)[0]
        print(prediction)
        
        decision = argmax(prediction)

        if decision == 0:
            commandlist.left()
        if decision == 1:
            commandlist.forward()
        if decision == 2:
            commandlist.right()
        if decision == 3:
            commandlist.back()

        print(decision)

if __name__ == "__main__":
    main()