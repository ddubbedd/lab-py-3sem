import os
import shutil
import sys

from PyQt6 import QtWidgets

from lab2.lab2_1 import lab1
from lab2.lab2_2 import lab2
from lab2.lab2_3 import lab3
from lab2.lab2_4 import lab4
from main_window_class import Window1

stylesheet = """
    QMainWindow {
        background-image: url("photo.jpg"); 
        background-repeat: no-repeat; 
        background-position: center
    }
"""


def application() -> None:
    """Функция для показа окна"""
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    window = Window1()
    window.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    application()
