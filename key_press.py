from pynput.keyboard import Controller, Key
from time import sleep


keybord = Controller()

sleep(2)
keybord.press(Key.space)
keybord.release(Key.space)
print("Fast Space Dan!")
sleep(1)
# keybord.press(Key.space)
# keybord.release(Key.space)
keybord.press('X')
keybord.press(Key.enter)
keybord.release(Key.enter)


print("Program end!")

"""in this cod ima
 how how to use pynput 
 library press and Key.release method
 """

