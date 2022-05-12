from pynput.keyboard import Controller, Key

keyboard = Controller()
key = "a"

keyboard.press(key)
keyboard.release(key)