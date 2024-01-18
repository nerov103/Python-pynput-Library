from pynput.keyboard import Key, Controller
from time import sleep


sleep(2)
# keyboard = Controller()
# keyboard.press("a")
# keyboard.release("a")
# with keyboard.pressed(Key.shift):
#     keyboard.press('a')
#     keyboard.release('a')


# Type two upper case As
keyboard = Controller()
keyboard.press('A')
keyboard.release('A')
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')
