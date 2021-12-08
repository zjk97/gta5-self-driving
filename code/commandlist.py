from directkeys import PressKey, ReleaseKey, W, A, D, S
import time


def forward():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    time.sleep(0.09)

def left():
    PressKey(A)
    PressKey(W)
    ReleaseKey(D)
    ReleaseKey(A)
    time.sleep(0.09)
    ReleaseKey(W)


def right():
    PressKey(D)
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    time.sleep(0.09)
    ReleaseKey(W)

def back():
    PressKey(S)
    ReleaseKey(A)
    ReleaseKey(D)
    ReleaseKey(W)
    time.sleep(0.09)
    ReleaseKey(S)
