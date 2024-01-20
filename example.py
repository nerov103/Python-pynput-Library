from pynput.mouse import Listener, Button, Controller



# def one_click(x, y, button, pressed):
#     if button == Button.left:
#         print(f"Left button clicked!")

#     # print(f"Mouse Clicked at ({x} and ({y})) with {button.name}")

# lisner = Listener(on_click=one_click)

# lisner.start()

"""
Function Number tow
"""


# def my_listener(x, y, btn, prss):
#     if btn == Button.right:
#         print("Press Right Button on Mouse!")
#     if btn == Button.left:
#         print("Press Left Button on MOuse!")
#     if btn == Button.middle:
#         print("Press Mouse Home Button!")

# # listen = Listener(on_click=my_listener)
# # listen.start()

# with Listener(on_click=my_listener) as listen:
#     listen.join()

"""
print the x and y proction valus
in my disply 
on  mouse pointer
"""
# def my_click(x, y, btn, press):
#     print(f"Mouse clicked at ({x}), ({y}) with {btn.name}")

#     if  btn == Button.left and press:
#         Controller().position = (100, 200)


# def my_move(x, y):
#     print(f"Mouse move to ({x}), ({y})")

# def my_scroll(x, y, dx, dy):
#     print(f"Mouse moved to ({x}), ({y})")

 
# with Listener() as lis:
#     lis.join()



import os

get_url = os.name
print(get_url)



