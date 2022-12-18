import datetime

from PyQt6 import QtCore, QtGui
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QWidget, QInputDialog

from lab2.lab2_1 import lab1
from lab2.lab2_2 import lab2
from lab2.lab2_3 import lab3

from lab2.lab2_4.lab4 import find_data1, find_data2, find_data3, find_data4

stylesheet = """
    QMainWindow {
        background-image: url("photo2.jpg"); 
        background-repeat: no-repeat; 
        background-position: center
    }
"""


class Window2(QWidget):
    def setup(self, MainWindow, date, path):
        self.date = datetime.date(int(date[4:8]), int(date[2:4]), int(date[0:2]))
        self.folderPath = path
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(530, 500)
        MainWindow.setStyleSheet(stylesheet)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 10, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));\n"
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
            "color: rgb(255, 255, 255);")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 350, 141, 71))
        self.pushButton_2.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 150, 141, 71))
        self.pushButton_3.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 250, 141, 71))
        self.pushButton_4.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(140, 100, 231, 31))
        self.pushButton_1.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_1.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate(MainWindow)
        self.add_functions()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная №3"))
        self.label.setText(_translate("MainWindow", f"Поиск данных за {self.date}"))
        self.pushButton_1.setText(_translate("MainWindow", "По основному файлу"))
        self.pushButton_2.setText(_translate("MainWindow", "По неделям"))
        self.pushButton_3.setText(_translate("MainWindow", "По двум файлам"))
        self.pushButton_4.setText(_translate("MainWindow", "По годам"))

    def add_functions(self):
        self.pushButton_1.clicked.connect(self.fingDataWindowAll)
        self.pushButton_2.clicked.connect(self.fingDataWindowXY)
        self.pushButton_3.clicked.connect(self.fingDataWindowYear)
        self.pushButton_4.clicked.connect(self.fingDataWindowWeek)

    def fingDataWindowAll(self):
        window = QMessageBox()
        window.setText('Данные из основного файла:\n' + ' '.join(find_data1(self.date, self.folderPath)[0]))
        window.setIcon(QMessageBox.Icon.Information)
        window.exec()

    def fingDataWindowXY(self):
        window = QMessageBox()
        window.setText("Данные из двух файлов:\n" + ' '.join(find_data2(self.date)[0]))
        window.setIcon(QMessageBox.Icon.Information)
        window.exec()

    def fingDataWindowYear(self):
        window = QMessageBox()
        window.setText("Данные из файлов по годам:\n" + ' '.join(find_data3(self.date)[0]))
        window.setIcon(QMessageBox.Icon.Information)
        window.exec()

    def fingDataWindowWeek(self):
        window = QMessageBox()
        window.setText("Данные из файлов по неделям:\n" + ' '.join(find_data4(self.date)[0]))
        window.setIcon(QMessageBox.Icon.Information)
        window.exec()
