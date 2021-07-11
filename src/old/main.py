import pyautogui
import pywinauto
import matplotlib.pyplot as plt
import win32api
import win32con
import pynput
import maps as maps_module
import time
import random


# def click(x, y):
#     x = screen_size[0] - x
#     win32api.SetCursorPos((x, y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def main():
    time.sleep(1)  # Time to move cursor to dofus screen
    screen_size = (3840, 2160)
    mouse = pynput.mouse.Controller()
    keyboard = pynput.keyboard.Controller()
    is_running = [True]
    is_stopped = [True]

    def on_press(key, first_bool, second_bool):
        try:
            # print('alphanumeric key {0} pressed'.format(key.char))
            pass
        except AttributeError:
            # print('special key {0} pressed'.format(key))
            if repr(key) == 'Key.f1':
                first_bool[0] = not first_bool[0]
            if repr(key) == 'Key.f10':
                second_bool[0] = False

    def shift_click(x, y, num=1):
        mouse.position = (x, y)
        with keyboard.pressed(pynput.keyboard.Key.shift):
            mouse.click(pynput.mouse.Button.left, num)

    def click(x, y, num=1):
        mouse.position = (x, y)
        mouse.click(pynput.mouse.Button.left, num)

    listener = pynput.keyboard.Listener(on_press=lambda x: on_press(x, is_running, is_stopped))
    listener.start()

    shift_click(10, 0)
    maps = maps_module.mine_04_28()

    loc0 = maps_module.Location('monde12', (4, 28), 1, 'mine', 1)
    m = [e for e in maps if e.loc == loc0][0]
    to_collect = ['fer']
    while is_stopped[0]:
        while is_running[0]:
            # Collecting
            click(2155, 2067)
            nb_potential_res = 0
            for res in to_collect:
                for e in m.res[res]:
                    nb_potential_res += 1
                    shift_click(e[0], e[1])
                    time.sleep(1 + random.gauss(0, 0.1))
            print('Harvest done')
            # Moving map
            time.sleep(nb_potential_res * (3 + 1))
            x_exit, y_exit, loc = random.choice(m.exits['mine'])
            m = [e for e in maps if e.loc == loc][0]
            click(x_exit, y_exit)
            time.sleep(5)
            print("The map should have changed.")


if __name__ == '__main__':
    main()
