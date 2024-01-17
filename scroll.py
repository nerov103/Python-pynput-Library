from pynput.mouse import Controller
from time import sleep

sleep(2)
mouse = Controller()
mouse.scroll(dx=10, dy=0)
# Simulate scrolling right by 3 steps
# mouse.scroll(3, 0)


