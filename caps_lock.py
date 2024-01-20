from pynput.keyboard import Listener, Key

def on_hit(key):
    print(key)

    

    if key == Key.esc:
        return False

with Listener(on_press=on_hit) as lis:
    lis.join()


