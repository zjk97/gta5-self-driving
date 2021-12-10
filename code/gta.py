import imp
from operator import pos
import os

from matplotlib.pyplot import axis
# import gym
import numpy as np
from numpy.lib.function_base import cov
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
# from win32gui import WidenPath

# from directkeys import D

# Killing optional CPU driver warnings

# DO NOT ALTER MODEL CLASS OUTSIDE OF TODOs. OTHERWISE, YOU RISK INCOMPATIBILITY
# WITH THE AUTOGRADER AND RECEIVING A LOWER GRADE.


class GTA(tf.keras.Model):
    def __init__(self, width, height):
        super(GTA, self).__init__()
        self.model_width = width
        self.model_height = height
        
        # TODO: Define network parameters and optimizer
        self.my_layer = Sequential()
        self.my_layer.add(Conv2D(128, kernel_size=(3,3), activation='relu'))
        self.my_layer.add(MaxPool2D(pool_size=(2,2), strides=(1,1), padding='valid'))
        self.my_layer.add(Conv2D(256, kernel_size=(3,3), activation='relu'))
        self.my_layer.add(Conv2D(256, kernel_size=(3,3), activation='relu'))
        self.my_layer.add(MaxPool2D(pool_size=(2,2), strides=(1,1), padding='valid'))
        self.my_layer.add(BatchNormalization())
        self.my_layer.add(Conv2D(256, kernel_size=(3,3), activation='relu'))
        self.my_layer.add(Conv2D(128, kernel_size=(3,3), activation='relu'))
        self.my_layer.add(Conv2D(100, kernel_size=(3,3), activation='relu'))
        self.my_layer.add(MaxPool2D(pool_size=(2,2), strides=(1,1), padding='valid'))
        self.my_layer.add(Flatten())
        self.my_layer.add(Dense(400, activation='tanh'))
        self.my_layer.add(Dropout(0.5))
        self.my_layer.add(Dense(200, activation='tanh'))
        self.my_layer.add(Dropout(0.5))
        self.my_layer.add(Dense(4, activation='softmax'))
    def call(self, inputs):
        x = self.my_layer(inputs)
        x = tf.reshape(x, [-1, 4])
        return x