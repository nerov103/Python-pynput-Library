from pynput.mouse import Controller
import time


time.sleep(1)

mouse = Controller()
# x = mouse.position

while True:
    print(f"Your Mouse Pointer Create Proction {mouse.position}")




#https://github.com/attreyabhatt/Python-Keylogger