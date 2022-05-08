# -*- coding: utf-8 -*-

import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
from PyQt5 import QtWidgets
from main_menu import Ui_MainWindow

TOGGLE_KEY = KeyCode(char="t")
timing = 40
clicking = False
mouse = Controller()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()


    def clicker():
        while True:
            if clicking:
                mouse.click(Button.left, 1)
                time.sleep(timing * 0.001)
            else:
                time.sleep(0.1)


    def toggle_event(key):
        if key == TOGGLE_KEY:
            global clicking
            clicking = not clicking

    ui.setupUi(MainWindow)
    MainWindow.show()

    threading.Thread(target=clicker).start()
    Listener(on_press=toggle_event).start()

    sys.exit(app.exec_())
