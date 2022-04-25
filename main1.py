from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
import resources_rc

from constant_window import Ui_CheckConstantWindow
from main_window import Ui_MainWindow
from pumpCalc_window import Ui_PumpCalcWindow
from about_window import Ui_AboutWindow

import sys
flag = ''
PASSWORD = '123'
user = 'Технолог'
class main_window(QtWidgets.QMainWindow):


    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
        self.ui.putImageHere.setPixmap(pixmap)

    def change_user(self):
        global user
        global flag
        # print(self.ui.label_currentUser.text())
        if self.ui.label_currentUser.text() == 'Технолог':
            dialog = ClssDialog(self)
            dialog.exec_()

            """В нижних условиях проблема в том, что при проверке каждого условия вызывается метод
            И из-за этого, даже при нажатии кнопки Cansle, произойдет проверка условия dialog.btnOk() ==?"""
            if flag == "Canceled":
                print('Cancled')
            elif flag == "Invalid Password":
                print('Access denied')
                # print(user)
            elif flag == "Valid Password":
                print('Ok')
                user = 'Главный технолог'
                self.ui.label_currentUser.setText('Главный технолог')
                # print(user)

            else:
                print(flag)
                print('smth went wrong when chek user flags')
                 # print(user)


        elif self.ui.label_currentUser.text() == 'Главный технолог':
            user = 'Технолог'
            self.ui.label_currentUser.setText('Технолог')
            # print(user)
        else:
            print(flag)
            print('smth went wrong. Wrong user type')

    def show_main_window(self):
        #self.ui.pushButton_chkConstValues.clicked.connect(self.close)
        self.ui.pushButton_chkConstValues.clicked.connect(self.show_constant_window)
        #self.ui.pushButton_pumpCalc.clicked.connect(self.close)
        self.ui.pushButton_pumpCalc.clicked.connect(self.show_pumpCalc_window)
        #self.ui.pushButton_aboutProg.clicked.connect(self.close)
        self.ui.pushButton_aboutProg.clicked.connect(self.show_about_window)

        self.ui.pushButton_mainTech.clicked.connect(self.change_user)

    def show_constant_window(self):
        self.ui2 = constant_window()
        self.ui2.show()
        self.ui2.close_constant_window()

    def show_about_window(self):
        print(user)
        self.ui3 = about_window()

        self.ui3.show()
        self.ui3.close_about_window()

    def show_pumpCalc_window(self):
        self.ui4 = pumpCalc_window()
        self.ui4.show()
        self.ui4.close_pumpCalc_window()


class ClssDialog(QtWidgets.QDialog):
    #global PASSWORD

    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)
        self.setWindowTitle("InputPassword")
        self.resize(508, 114)

        self.pushButton_Cancel = QtWidgets.QPushButton(self)
        self.pushButton_Cancel.setGeometry(QtCore.QRect(70, 80, 80, 25))
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.pushButton_Cancel.setText("Отмена")
        self.pushButton_Cancel.clicked.connect(self.btnClosed)

        self.pushButton_Ok = QtWidgets.QPushButton(self)
        self.pushButton_Ok.setGeometry(QtCore.QRect(340, 80, 80, 25))
        self.pushButton_Ok.setObjectName("pushButton_Ok")
        self.pushButton_Ok.setText("Ок")
        self.pushButton_Ok.clicked.connect(self.btnOk)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 20, 451, 17))
        self.label.setObjectName("label")
        self.label.setText("Введите пароль, чтобы получить права Главного технолога")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 351, 23))
        self.lineEdit.setObjectName("lineEdit")

    def btnClosed(self):
        global flag
        self.close()
        flag = 'Canceled'

    def btnOk(self):
        global flag
        if self.lineEdit.text() == PASSWORD:
            self.close()
            flag = 'Valid Password'
            #return ("Valid Password")
        else:
            flag = 'Invalid Password'
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                           "Неправильный пароль",
                                           "Вы ввели неправильный пароль!\nПопробуйте еще раз",
                                           buttons=QtWidgets.QMessageBox.Ok,
                                           parent=self)
            dialog.exec_()
            #return ("Invalid Password")
            '''Insert here error popup message'''


class constant_window(QtWidgets.QMainWindow):

    def __init__(self):
        super(constant_window, self).__init__()
        self.ui2 = Ui_CheckConstantWindow()
        self.ui2.setupUi(self)
        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
        self.ui2.putImageHere.setPixmap(pixmap)
        self.ui2.label_currentUser.setText(user)

        # self.table = QtWidgets.QTableWidget(self.centralwidget)
        # self.table.setObjectName("test table")
        # self.table.setColumnCount(3)
        # self.table.setRowCount(3)
        # item = QtWidgets.QTableWidgetItem()
        # self.table.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.table.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.table.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.table.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.table.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.table.setHorizontalHeaderItem(2, item)
        # self.button = QtWidgets.QPushButton()
        # self.button.resize(200, 200)
        # self.button.setText('but')
        # self.ui2.tableWidget.setCellWidget(1, 1, self.button)

        self.ui2.tableWidgetMTHousing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui2.tableWidgetMTDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui2.tableWidgetMTLDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui2.tableWidgetMTBearing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui2.tableWidgetMTHB.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)




    def close_constant_window(self):
        self.ui2.pushButton_Close.clicked.connect(self.close)
        #self.ui2.pushButton_backToMainWindow.clicked.connect(self.show_main_window)

    # def show_main_window(self):
    #     self.ui = main_window()
    #     self.ui.show()
    #     self.ui.show_main_window()

class about_window(QtWidgets.QMainWindow):

    def __init__(self):
        super(about_window, self).__init__()
        self.ui3 = Ui_AboutWindow()
        self.ui3.setupUi(self)
        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
        self.ui3.putImageHere.setPixmap(pixmap)
        self.ui3.label_currentUser.setText(user)

    def close_about_window(self):
        self.ui3.pushButton_Close.clicked.connect(self.close)
        #self.ui3.pushButton_backToMainWindow.clicked.connect(self.show_main_window)

    # def show_main_window(self):
    #     self.ui = main_window()
    #     self.ui.show()
    #     self.ui.show_main_window()

class pumpCalc_window(QtWidgets.QMainWindow):

    def __init__(self):
        super(pumpCalc_window, self).__init__()
        self.ui4 = Ui_PumpCalcWindow()
        self.ui4.setupUi(self)
        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
        self.ui4.putImageHere.setPixmap(pixmap)
        self.ui4.label_currentUser.setText(user)

    def close_pumpCalc_window(self):
        self.ui4.pushButton_Close.clicked.connect(self.close)
        #self.ui4.pushButton_backToMainWindow.clicked.connect(self.show_main_window)

    # def show_main_window(self):
    #     self.ui = main_window()
    #     self.ui.show()
    #     self.ui.show_main_window()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = main_window()
    w.show()
    w.show_main_window()
    #w.back_to_main_window()
    sys.exit(app.exec_())