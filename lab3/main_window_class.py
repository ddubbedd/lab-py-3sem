import sys

from PyQt6 import QtCore, QtGui
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QWidget, QInputDialog, QDialog

from lab2.lab2_1 import lab1
from lab2.lab2_2 import lab2
from lab2.lab2_3 import lab3
from second_window_class import Window2

stylesheet = """
    QMainWindow {
        background-image: url("photo.jpg"); 
        background-repeat: no-repeat; 
        background-position: center
    }
"""


class Window1(QWidget):
    def setup(self, MainWindow):

        self.folderpath = ""
        while self.folderpath == "":
            self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Выберите папку с датасетом"
            )

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
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 100, 231, 31))
        self.pushButton_5.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate(MainWindow)
        self.addFunctions()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная №3"))
        self.label.setText(_translate("MainWindow", "Лабораторная работа №3"))
        self.pushButton_2.setText(_translate("MainWindow", "Датасет на два\n"
                                                           "файла"))
        self.pushButton_3.setText(_translate("MainWindow", "Датасет\n"
                                                           "по годам"))
        self.pushButton_4.setText(_translate("MainWindow", "Датасет\n"
                                                           "по неделям"))
        self.pushButton_5.setText(_translate("MainWindow", "Найти данные по дате"))

    def addFunctions(self):
        self.pushButton_2.clicked.connect(self.splitXY)
        self.pushButton_3.clicked.connect(self.splitYear)
        self.pushButton_4.clicked.connect(self.splitWeek)
        self.pushButton_5.clicked.connect(self.findData)

    def splitXY(self):
        lab1.split_into_files(self.folderpath)
        ok_window = QMessageBox()
        ok_window.setWindowTitle('Успешно')
        ok_window.setText('Разделение на два файла прошло успешно!')
        ok_window.setIcon(QMessageBox.Icon.Information)
        ok_window.exec()

    def splitYear(self):
        lab2.write_to_file(self.folderpath)
        ok_window = QMessageBox()
        ok_window.setWindowTitle('Успешно')
        ok_window.setText('Разделение по годам прошло успешно!')
        ok_window.setIcon(QMessageBox.Icon.Information)
        ok_window.exec()

    def splitWeek(self):
        lab3.write_to_file(self.folderpath)
        ok_window = QMessageBox()
        ok_window.setWindowTitle('Успешно')
        ok_window.setText('Разделение по неделям прошло успешно!')
        ok_window.setIcon(QMessageBox.Icon.Information)
        ok_window.exec()

    def exWindow(self, ex):
        window = QMessageBox()
        window.setWindowTitle('Ошибка')
        window.setText(ex)
        window.setIcon(QMessageBox.Icon.Warning)
        window.exec()

    def showWindow2(self, date):
        """Функция для показа окна"""
        self.MainWindow = QtWidgets.QMainWindow()
        self.window = Window2()
        self.window.setup(self.MainWindow, date[0: 2]+'/'+date[2: 4]+'/'+date[4: 8])
        self.MainWindow.show()

    def checkDate(self, text):
        if len(text) == 8 or text.isdigit() != False:
            if 2008 <= int(text[4: 8]) <= 2022:
                days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                if 1 <= int(text[2: 4]) <= 12:
                    if 1 <= int(text[0: 2]) <= days[int(text[2: 4]) - 1]:
                        return True
        return False

    def findData(self) -> None:
        text, ok = QInputDialog.getText(self, 'Поиск по дате 2008г-2022г',
                                        'Введите дату в формате ДДММГГГГ:')

        if ok:
            if not self.checkDate(text):
                self.exWindow('Неверный ввод даты!')
                return
            else:
                self.dateFind = text
                self.showWindow2(self.dateFind)
