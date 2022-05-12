import keyboard

def record_key(event):
    print(event.name)

keyboard.on_release(callback=record_key)