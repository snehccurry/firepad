from pynput.keyboard import Key, Listener

import time
def on_press(key):
    try:
        print(f"Key {key} pressed")
    except AttributeError:
        # Ignore special keys without a name attribute
        pass

def on_release(key):
    print(f"Key {key} released")
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    time.sleep(0.2)
    listener.join()
