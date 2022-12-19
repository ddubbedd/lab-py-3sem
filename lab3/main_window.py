import sys

from PyQt6 import QtWidgets
from main_window_class import Window1


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
