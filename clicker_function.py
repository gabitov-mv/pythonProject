import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="t")
click_all = False
click_1 = False
click_2 = False
click_3 = False
click_4 = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.04)


def toggle_event(key, toggle_key, ):
    if key == toggle_key:
        global clicking
        clicking = not clicking


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
