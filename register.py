import pyautogui
import pywinauto
import matplotlib.pyplot as plt
import win32gui
from pynput.mouse import Listener


def on_move(x, y):
    # print(x, y)
    pass


def on_click(x, y, button, pressed):
    # print(x, y, button, pressed)
    pass


def on_scroll(x, y, dx, dy):
    print(x, y, dx, dy)
    # pass


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()

# flags, hcursor, (x,y) = win32gui.GetCursorInfo()
#
# myScreenshot = pyautogui.screenshot()
# plt.imshow(myScreenshot)
