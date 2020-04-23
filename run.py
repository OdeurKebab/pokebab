from pynput.keyboard import Key, Controller
import win32gui
import threading
import time
import string
import random


def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def typeMessage():
    keyboard.press(random.choice(string.ascii_letters))
    keyboard.release(random.choice(string.ascii_letters))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def processMessage():
    # Show discord
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)

    for i in top_windows:
        # print(i[1])
        if "discord" in i[1].lower():
            print(i)
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])

            typeMessage()
            break

if __name__ == "__main__":
    string.ascii_letters
    keyboard = Controller()

    for i in range(5):
        processMessage()
        time.sleep(5)








