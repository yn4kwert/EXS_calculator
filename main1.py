from PyQt5 import QtWidgets, QtGui, QtCore
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

MT5A_FL_HEAD_LEN = 60
MT5A_FL_HEAD_LEN_UP_DEV = 1.2
MT5A_FL_HEAD_LEN_LOW_DEV = 1.2
MT5A_FL_BASE_LEN = 60
MT5A_FL_BASE_LEN_UP_DEV = 1.2
MT5A_FL_BASE_LEN_LOW_DEV = 1.2

MT5_HEAD_LEN = 50
MT5_HEAD_LEN_UP_DEV = 1.1
MT5_HEAD_LEN_LOW_DEV = 1.1
MT5_BASE_LEN = 50
MT5_BASE_LEN_UP_DEV = 1.1
MT5_BASE_LEN_LOW_DEV = 1.1
MT2A_HEAD_LEN = 40
MT2A_HEAD_LEN_UP_DEV = 0.8
MT2A_HEAD_LEN_LOW_DEV = 0.8
MT2A_BASE_LEN = 40
MT2A_BASE_LEN_UP_DEV = 0.8
MT2A_BASE_LEN_LOW_DEV = 0.8

'''
class - CamelCase
Method and func - lower_case_with_underscores or likeThatName
 global variable - _global_var_name
 Constants - CAP_WORDS'''


class main_window(QtWidgets.QMainWindow):


    def __init__(self):
        super(main_window, self).__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
        self.ui_main.putImageHere.setPixmap(pixmap)

    def show_main_window(self):
        #self.ui.pushButton_chkConstValues.clicked.connect(self.close)
        self.ui_main.pushButton_chkConstValues.clicked.connect(self.show_constant_window)
        #self.ui.pushButton_pumpCalc.clicked.connect(self.close)
        self.ui_main.pushButton_pumpCalc.clicked.connect(self.show_pumpCalc_window)
        #self.ui.pushButton_aboutProg.clicked.connect(self.close)
        self.ui_main.pushButton_aboutProg.clicked.connect(self.show_about_window)

        self.ui_main.pushButton_ChiefTech.clicked.connect(self.change_user)

    def show_constant_window(self):
        self.ui = constant_window()
        self.ui.show()
        self.ui.close_constant_window()

    def show_about_window(self):
        print(user)
        self.ui = about_window()
        self.ui.show()
        self.ui.close_about_window()

    def show_pumpCalc_window(self):
        self.ui = pumpCalc_window()
        self.ui.show()
        self.ui.close_pumpCalc_window()

    def change_user(self):

        global user
        global flag
        print('start')
        # print(self.ui.label_currentUser.text())
        if self.ui_main.label_currentUser.text() == 'Технолог': #Ломается тут
            print('end')
            #Было изначально:
            # dialog = ClssDialog(self)
            # dialog.exec_()

            self.dialog_password = ClssDialog()
            self.dialog_password.exec_()


            if flag == "Canceled":
                print('Canceled')
            elif flag == "Empty":
                print('Empty')
            elif flag == "Invalid Password":
                print('Access denied')
                # print(user)
            elif flag == "Valid Password":
                print('Ok')
                user = 'Главный технолог'
                self.ui_main.label_currentUser.setText('Главный технолог')
                flag = "Empty"
                # print(user)

            else:
                print(flag)
                print('smth went wrong when chek user flags')
                 # print(user)

        elif self.ui_main.label_currentUser.text() == 'Главный технолог':
            user = 'Технолог'
            self.ui_main.label_currentUser.setText('Технолог')
            # print(user)
        else:
            print(flag)
            print('smth went wrong. Wrong user type')

'''This class is responsible for password input dialog box operation
Description of this dialog box is implemented 'on place' and not imported from other modules'''
class ClssDialog(QtWidgets.QDialog):
    #global PASSWORD
    global flag
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
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.lineEdit.setObjectName("lineEdit")

    '''This method describes what should happen if button Cancel is pressed'''
    def btnClosed(self):

        global flag
        flag = 'Canceled'
        self.close()

    '''This method describes what should happen if button OK is pressed'''
    def btnOk(self):

        global flag
        if self.lineEdit.text() == PASSWORD:
            flag = 'Valid Password'
            self.close()
        else:
            flag = 'Invalid Password'
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                           "Неправильный пароль",
                                           "Вы ввели неправильный пароль!\nПопробуйте еще раз",
                                           buttons=QtWidgets.QMessageBox.Ok,
                                           parent=self)
            dialog.exec_()

    # def closeEvent(self, event):
    #     global flag
    #     # Переопределить colseEvent
    #     print('closed')
    #     flag = 'Canceled'
    #     event.accept()

        # if reply == QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()
'''This class fully describes behavior of the window "Constant window"'''

class constant_window(QtWidgets.QMainWindow):


    '''Design of constant window is created via QtDesigner and was transformed to .py file from .ui
    Method init initialize this class from the constant_window.py module
    AND put an image-logo from .png file (why .qrc?) I GUES IT SHOULD BE IMPLEMENTED AS A STAND ALONE METHOD for re-using
    AND makes columns width expand in dependence of window width'''
    def __init__(self):
        global MT_hidden

        super(constant_window, self).__init__()
        self.ui = Ui_CheckConstantWindow()
        self.ui.setupUi(self)

        '''Put a logo'''
        #self.put_a_logo()
        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
        self.ui.putImageHere.setPixmap(pixmap)
        self.ui.label_currentUser.setText(user)
        '''Expand columns' width'''
        self.ui.tableWidgetMTHousing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetMTDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetMTLDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetMTBearing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetMTHB.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        '''UNCOMMENT THIS when releasing the program
        vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'''
        # if user != 'Главный технолог':
        #     self.disable_tables_if_not_chief_tech()
        '''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''

        self.ui.pushButton_TPSLine.clicked.connect(self.hide_all_MT, MT_hidden)
        self.ui.pushButton_initTableMTHousing.clicked.connect(self.upload_xlsx_file)
        #self.ui.pushButton_hideMTHousing.clicked.connect(self.button_hide_clicked) #replaced with universal method ''button_hide2_clicked''

        self.ui.btn_save_changes.clicked.connect(self.btn_save_changes_clicked)
        self.calculate_and_block_uneditable_MT_housing_table_values()
        #self.ui.TestButton.clicked.connect(self.calculate_and_block_uneditable_MT_housing_table_values)

        self.ui.pushButton_hideMTHousing.clicked.connect(lambda checked, btn_name='MTHousing': self.button_hide2_clicked(btn_name))
        self.ui.pushButton_hideMTHB.clicked.connect(lambda checked, btn_name='MTHB': self.button_hide2_clicked(btn_name))
        self.ui.pushButton_hideMTDif.clicked.connect(lambda checked, btn_name='MTDif': self.button_hide2_clicked(btn_name))
        self.ui.pushButton_hideMTLDif.clicked.connect(lambda checked, btn_name='MTLDif': self.button_hide2_clicked(btn_name))
        self.ui.pushButton_hideMTBearing.clicked.connect(lambda checked, btn_name='MTBearing': self.button_hide2_clicked(btn_name))
    #def put_a_logo(self):

    '''This method performs calculation of MT housings working length and blocks calculated values for edit even for cheif technologist'''
    def calculate_and_block_uneditable_MT_housing_table_values(self):
        rows = self.ui.tableWidgetMTHousing.rowCount()
        print(rows)
        for row in range(rows):
            work_housing_len_nom = round(
                                        float(self.ui.tableWidgetMTHousing.item(row, 4).text())
                                        - MT5A_FL_HEAD_LEN
                                        - MT5A_FL_BASE_LEN
                                        , 3)
            print(work_housing_len_nom)
            work_housing_len_max = round(
                                        float(self.ui.tableWidgetMTHousing.item(row, 4).text())
                                        + float(self.ui.tableWidgetMTHousing.item(row, 5).text())
                                        - (MT5A_FL_HEAD_LEN - MT5A_FL_HEAD_LEN_LOW_DEV)
                                        - (MT5A_FL_BASE_LEN - MT5A_FL_BASE_LEN_LOW_DEV)
                                        , 3)
            print(work_housing_len_max)
            work_housing_len_min = round(
                                        float(self.ui.tableWidgetMTHousing.item(row, 4).text())
                                        - float(self.ui.tableWidgetMTHousing.item(row, 6).text())
                                        - (MT5A_FL_HEAD_LEN + MT5A_FL_HEAD_LEN_LOW_DEV)
                                        - (MT5A_FL_BASE_LEN + MT5A_FL_BASE_LEN_LOW_DEV)
                                        , 3)
            print(work_housing_len_min)

            item = self.ui.tableWidgetMTHousing.setItem(row, 7, QtWidgets.QTableWidgetItem(str(work_housing_len_nom)))
            item = self.ui.tableWidgetMTHousing.item(row, 7)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            item = self.ui.tableWidgetMTHousing.setItem(row, 8, QtWidgets.QTableWidgetItem(str(work_housing_len_max)))
            item = self.ui.tableWidgetMTHousing.item(row, 8)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            item = self.ui.tableWidgetMTHousing.setItem(row, 9, QtWidgets.QTableWidgetItem(str(work_housing_len_min)))
            item = self.ui.tableWidgetMTHousing.item(row, 9)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)


    '''This method blocks TableWidgets in constant_window if current user is not chief technologist'''
    def disable_tables_if_not_chief_tech(self):

        self.ui.tableWidgetMTHousing.setEnabled(False)
        self.ui.tableWidgetMTHB.setEnabled(False)
        self.ui.tableWidgetMTDif.setEnabled(False)
        self.ui.tableWidgetMTLDif.setEnabled(False)
        self.ui.tableWidgetMTBearing.setEnabled(False)


    def hide_all_MT(self):
        global MT_hidden

        self.ui.tableWidgetMTHousing.setVisible(MT_hidden)
        self.ui.tableWidgetMTHB.setVisible(MT_hidden)
        self.ui.tableWidgetMTDif.setVisible(MT_hidden)
        self.ui.tableWidgetMTLDif.setVisible(MT_hidden)
        self.ui.tableWidgetMTBearing.setVisible(MT_hidden)

        self.ui.pushButton_hideMTHousing.setVisible(MT_hidden)
        self.ui.label_MT_Housing.setVisible(MT_hidden)
        self.ui.pushButton_initTableMTHousing.setVisible(MT_hidden)

        self.ui.pushButton_hideMTHB.setVisible(MT_hidden)
        self.ui.label_MT_HB.setVisible(MT_hidden)
        self.ui.pushButton_initTableMTHB.setVisible(MT_hidden)

        self.ui.pushButton_hideMTDif.setVisible(MT_hidden)
        self.ui.label_MT_Dif.setVisible(MT_hidden)
        self.ui.pushButton_initTableMTDif.setVisible(MT_hidden)

        self.ui.pushButton_hideMTLDif.setVisible(MT_hidden)
        self.ui.label_MT_LDif.setVisible(MT_hidden)
        self.ui.pushButton_initTableMTLDif.setVisible(MT_hidden)

        self.ui.pushButton_hideMTBearing.setVisible(MT_hidden)
        self.ui.label_MT_Bearing.setVisible(MT_hidden)
        self.ui.pushButton_initTableMTBearing.setVisible(MT_hidden)

        MT_hidden = not MT_hidden

    '''This method allows to hide Table widget of MT Housings by clicking Hide/Unhide button'''


    # def button_hide_clicked(self):
    #     if self.ui.pushButton_hideMTHousing.text() == 'Hide':
    #         self.ui.tableWidgetMTHousing.setVisible(False)
    #         self.ui.pushButton_hideMTHousing.setText('Unhide')
    #     else:
    #         self.ui.tableWidgetMTHousing.setVisible(True)
    #         self.ui.pushButton_hideMTHousing.setText('Hide')

    '''This method allows to hide any Table widget dependantly on clicked button Hide/Unhide 
    It is not safe to use eval() - needed to be replaced'''
    def button_hide2_clicked(self, btn_name):
        if eval('self.ui.pushButton_hide'+btn_name+'.text()') == 'Hide':
            eval('self.ui.tableWidget'+btn_name+'.setVisible(False)')
            eval('self.ui.pushButton_hide'+btn_name+'.setText(\'Unhide\')')
        else:
            eval('self.ui.tableWidget'+btn_name+'.setVisible(True)')
            eval('self.ui.pushButton_hide'+btn_name+'.setText(\'Hide\')')

        # return(constant_window)

    def close_constant_window(self):
        self.ui.pushButton_Close.clicked.connect(self.close)
        #self.ui.pushButton_backToMainWindow.clicked.connect(self.show_main_window)
    ''' This method allows to upload all cells values from xslx table to my program. I.e. initialize the table.
    I guess, it's better to transform it into the func or to think how to reuse this method'''
    def upload_xlsx_file(self):
        self.ui.tableWidgetMTHousing.clearContents()
        xl = pd.read_excel('./MT_housing.xlsx', header=0, index_col=0)
        #self.ui.tableWidgetMTHousing.clear()
        rows, cols = xl.shape
        self.ui.tableWidgetMTHousing.setRowCount(rows)
        for row in range(rows):
            for col in range(cols):
                self.ui.tableWidgetMTHousing.setItem(row, col, QtWidgets.QTableWidgetItem(str(xl.iloc[row][col])))
        self.calculate_and_block_uneditable_MT_housing_table_values()

    def btn_save_changes_clicked(self):
        '''This method should save all changes to the memory'''
        pass
    # def show_main_window(self):
    #     self.ui = main_window()
    #     self.ui.show()
    #     self.ui.show_main_window()

class about_window(QtWidgets.QMainWindow):

    def __init__(self):
        super(about_window, self).__init__()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)
        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
        self.ui.putImageHere.setPixmap(pixmap)
        self.ui.label_currentUser.setText(user)

    def close_about_window(self):
        self.ui.pushButton_Close.clicked.connect(self.close)
        #self.ui.pushButton_backToMainWindow.clicked.connect(self.show_main_window)

    # def show_main_window(self):
    #     self.ui = main_window()
    #     self.ui.show()
    #     self.ui.show_main_window()

class pumpCalc_window(QtWidgets.QMainWindow):

    def __init__(self):
        super(pumpCalc_window, self).__init__()
        self.ui = Ui_PumpCalcWindow()
        self.ui.setupUi(self)
        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
        self.ui.putImageHere.setPixmap(pixmap)
        self.ui.label_currentUser.setText(user)

    def close_pumpCalc_window(self):
        self.ui.pushButton_Close.clicked.connect(self.close)
        #self.ui.pushButton_backToMainWindow.clicked.connect(self.show_main_window)

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