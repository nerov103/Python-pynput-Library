
from pynput.keyboard import Listener

def on_press(Ke):
    print(f"Pressed: {Ke}")

def on_release(Key):
    print(f"Release: {Key}")



with Listener(on_press=on_press,on_release=on_release) as lis:
    print("Listening for keyboard events...")
    lis.join()


