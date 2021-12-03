from pynput.keyboard import Key, Controller

keyboard = Controller()

def forward():
    keyboard.press('w')
    keyboard.release('w')

def backward():
    keyboard.press('s')
    keyboard.release('s')

def left():
    keyboard.press('a')
    keyboard.release('a')

def right():
    keyboard.press('d')
    keyboard.release('d')