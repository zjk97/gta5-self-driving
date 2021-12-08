from directkeys import PressKey, ReleaseKey, W, A, D
import time


def forward():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    time.sleep(0.05)

def left():
    PressKey(A)
    PressKey(W)
    ReleaseKey(D)
    ReleaseKey(A)
    time.sleep(0.05)
    ReleaseKey(W)


def rigth():
    PressKey(D)
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    time.sleep(0.05)
    ReleaseKey(W)
