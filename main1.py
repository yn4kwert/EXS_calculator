from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
import resources_rc

from constant_window import Ui_CheckConstantWindow
from main_window import Ui_MainWindow
from pumpCalc_window import Ui_PumpCalcWindow
from about_window import Ui_AboutWindow

import sys
import pandas as pd


flag = ''
PASSWORD = '123'
user = 'Технолог'
MT_hidden = False

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

'''This class is responsible for password input dialog box operation
Description of this dialog box is implemented 'on place' and not imported from other modules'''
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

    '''This method describes what should happen if button Cancel is pressed'''
    def btnClosed(self):
        global flag
        self.close()
        flag = 'Canceled'

    '''This method describes what should happen if button OK is pressed'''
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

'''This class fully describes behavior of the window "Constant window"'''

class constant_window(QtWidgets.QMainWindow):


    '''Design of constant window is created via QtDesigner and was transformed to .py file from .ui
    Method init initialize this class from the constant_window.py module
    AND put an image-logo from .png file (why .qrc?) I GUES IT SHOULD BE IMPLEMENTED AS A STAND ALONE METHOD for re-using
    AND makes columns width expand in dependence of window width'''
    def __init__(self):
        global MT_hidden

        super(constant_window, self).__init__()
        self.ui2 = Ui_CheckConstantWindow()
        self.ui2.setupUi(self)

        '''Put a logo'''
        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
        self.ui2.putImageHere.setPixmap(pixmap)
        self.ui2.label_currentUser.setText(user)
        '''Expand columns' width'''
        self.ui2.tableWidgetMTHousing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui2.tableWidgetMTDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui2.tableWidgetMTLDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui2.tableWidgetMTBearing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui2.tableWidgetMTHB.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.ui2.pushButton_TPSLine.clicked.connect(self.hide_all_MT, MT_hidden)
        self.ui2.pushButton_initTableMTHousing.clicked.connect(self.upload_xlsx_file)
        #self.ui2.pushButton_hideMTHousing.clicked.connect(self.button_hide_clicked) #replaced with universal method ''button_hide2_clicked''

        self.ui2.pushButton_hideMTHousing.clicked.connect(lambda checked, btn_name='MTHousing': self.button_hide2_clicked(btn_name))
        self.ui2.pushButton_hideMTHB.clicked.connect(lambda checked, btn_name='MTHB': self.button_hide2_clicked(btn_name))
        self.ui2.pushButton_hideMTDif.clicked.connect(lambda checked, btn_name='MTDif': self.button_hide2_clicked(btn_name))
        self.ui2.pushButton_hideMTLDif.clicked.connect(lambda checked, btn_name='MTLDif': self.button_hide2_clicked(btn_name))
        self.ui2.pushButton_hideMTBearing.clicked.connect(lambda checked, btn_name='MTBearing': self.button_hide2_clicked(btn_name))

    def hide_all_MT(self):
        global MT_hidden

        self.ui2.tableWidgetMTHousing.setVisible(MT_hidden)
        self.ui2.tableWidgetMTHB.setVisible(MT_hidden)
        self.ui2.tableWidgetMTDif.setVisible(MT_hidden)
        self.ui2.tableWidgetMTLDif.setVisible(MT_hidden)
        self.ui2.tableWidgetMTBearing.setVisible(MT_hidden)

        self.ui2.pushButton_hideMTHousing.setVisible(MT_hidden)
        self.ui2.label_MT_Housing.setVisible(MT_hidden)
        self.ui2.pushButton_initTableMTHousing.setVisible(MT_hidden)

        self.ui2.pushButton_hideMTHB.setVisible(MT_hidden)
        self.ui2.label_MT_HB.setVisible(MT_hidden)
        self.ui2.pushButton_initTableMTHB.setVisible(MT_hidden)

        self.ui2.pushButton_hideMTDif.setVisible(MT_hidden)
        self.ui2.label_MT_Dif.setVisible(MT_hidden)
        self.ui2.pushButton_initTableMTDif.setVisible(MT_hidden)

        self.ui2.pushButton_hideMTLDif.setVisible(MT_hidden)
        self.ui2.label_MT_LDif.setVisible(MT_hidden)
        self.ui2.pushButton_initTableMTLDif.setVisible(MT_hidden)

        self.ui2.pushButton_hideMTBearing.setVisible(MT_hidden)
        self.ui2.label_MT_Bearing.setVisible(MT_hidden)
        self.ui2.pushButton_initTableMTBearing.setVisible(MT_hidden)

        MT_hidden = not MT_hidden

    '''This method allows to hide Table widget of MT Housings by clicking Hide/Unhide button'''
    # def button_hide_clicked(self):
    #     if self.ui2.pushButton_hideMTHousing.text() == 'Hide':
    #         self.ui2.tableWidgetMTHousing.setVisible(False)
    #         self.ui2.pushButton_hideMTHousing.setText('Unhide')
    #     else:
    #         self.ui2.tableWidgetMTHousing.setVisible(True)
    #         self.ui2.pushButton_hideMTHousing.setText('Hide')

    '''This method allows to hide any Table widget dependantly on clicked button Hide/Unhide 
    It is not safe to use eval() - needed to be replaced'''
    def button_hide2_clicked(self, btn_name):
        if eval('self.ui2.pushButton_hide'+btn_name+'.text()') == 'Hide':
            eval('self.ui2.tableWidget'+btn_name+'.setVisible(False)')
            eval('self.ui2.pushButton_hide'+btn_name+'.setText(\'Unhide\')')
        else:
            eval('self.ui2.tableWidget'+btn_name+'.setVisible(True)')
            eval('self.ui2.pushButton_hide'+btn_name+'.setText(\'Hide\')')

        # return(constant_window)

    def close_constant_window(self):
        self.ui2.pushButton_Close.clicked.connect(self.close)
        #self.ui2.pushButton_backToMainWindow.clicked.connect(self.show_main_window)
    ''' This method allows to upload all cells values from xslx table to my program. I.e. initialize the table.
    I guess, it's better to transform it into the func or to think how to reuse this method'''
    def upload_xlsx_file(self):
        xl = pd.read_excel('./MT_housing.xlsx', header=0, index_col=0)
        #self.ui2.tableWidgetMTHousing.clear()
        rows, cols = xl.shape
        self.ui2.tableWidgetMTHousing.setRowCount(rows)
        for row in range(rows):
            for col in range(cols):
                self.ui2.tableWidgetMTHousing.setItem(row, col, QtWidgets.QTableWidgetItem(str(xl.iloc[row][col])))

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



    # for item in xl:
    #     print(xl[item])


    # Load a sheet into a DataFrame by name: df1
    #df1 = xl.parse('Sheet1')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = main_window()
    w.show()
    w.show_main_window()
    #w.back_to_main_window()
    sys.exit(app.exec_())