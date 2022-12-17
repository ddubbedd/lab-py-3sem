import sys

from PyQt6 import QtWidgets

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

    # os.remove('/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_1/X.csv')
    # os.remove('/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_1/Y.csv')
    # shutil.rmtree('/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_2/dataset')
    # os.mkdir('/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_2/dataset')
    # shutil.rmtree('/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_3/dataset')
    # os.mkdir('/Users/aleksandragorbuncova/PycharmProjects/lab-py-3sem/lab2/lab2_3/dataset')
    # lab1.split_into_files()
    # lab2.write_to_file()
    # lab3.write_to_file()
    # lab4.run()
