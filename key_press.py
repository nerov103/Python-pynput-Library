from pynput.keyboard import Key, Controller
import pynput

keyboard = Controller()
# print(dir(pynput.keyboard.Key.space))


keyboard.press(Key.space)
keyboard.release(Key.space)


keyboard.press('a')
keyboard.release('a')







  