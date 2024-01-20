from pynput.keyboard import Listener, Key


def one_key(ky):
    if ky == Key.ctrl:
        print(f"Pressed: {ky}")
    elif ky == Key.enter:
        print(f"Pressed: {ky}")

def on_relase(re_key):
    print(f"Key_Release")








with Listener(on_press=one_key, on_release=on_relase) as listenr:
    print("With For Press Any Key....")
    listenr.join()


    
"""
Identifying Specific Keys: Use the key object's attributes to check for specific keys

"""