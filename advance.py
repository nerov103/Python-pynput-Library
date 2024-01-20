from pynput.keyboard import Listener, Key

def on_press(key):
    print(key)
    

def on_release(key):
    print(key)
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()




