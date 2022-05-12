from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
import resources_rc

from constant_window import Ui_CheckConstantWindow
from main_window import Ui_MainWindow
from pumpCalc_window import Ui_PumpCalcWindow
from about_window import Ui_AboutWindow
from new_item_window import Ui_DialogCreateNewItem

import sys
import pandas as pd

flag = ''
PASSWORD = '123'
user = 'Технолог'
MT_hidden = False
EZLine_hidden = False
REDA_hidden = False
Other_hidden = False

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

# class all_windows(QtWidgets.QMainWindow):
#
#     def __init__(self):
#         super(all_windows, self).__init__()
#         self.ui = Ui_PumpCalcWindow()   # Создать ui файл с шаблонным оформлением?
#         self.ui.setupUi(self)
#         #Как применить этот участок кода для всех окон?:
#         pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
#         self.ui.putImageHere.setPixmap(pixmap)
#         self.ui.labelCurrentUser.setText(user)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
        self.ui_main.putImageHere.setPixmap(pixmap)



    def showMainWindow(self):
        #self.ui.pushButton_chkConstValues.clicked.connect(self.close)
        self.ui_main.pushButtonChekConstValues.clicked.connect(self.showConstantWindow)
        #self.ui.pushButton_pumpCalc.clicked.connect(self.close)
        self.ui_main.pushButtonPumpCalc.clicked.connect(self.showPumpCalcWindow)
        #self.ui.pushButton_aboutProg.clicked.connect(self.close)
        self.ui_main.pushButtonAboutProg.clicked.connect(self.showAboutWindow)

        self.ui_main.pushButtonChiefTech.clicked.connect(self.changeUser)

    def showConstantWindow(self):
        self.ui = ConstantWindow()
        self.ui.show()
        self.ui.closeConstantWindow()

    def showAboutWindow(self):
        print(user)
        self.ui = AboutWindow()
        self.ui.show()
        self.ui.closeAboutWindow()

    def showPumpCalcWindow(self):
        self.ui = PumpCalcWindow()
        self.ui.show()
        self.ui.closePumpCalcWindow()

    def changeUser(self):

        global user
        global flag
        print('start')
        # print(self.ui.labelCurrentUser.text())
        if self.ui_main.labelCurrentUser.text() == 'Технолог': #Ломается тут
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
                self.ui_main.labelCurrentUser.setText('Главный технолог')
                flag = "Empty"
                # print(user)

            else:
                print(flag)
                print('smth went wrong when chek user flags')
                 # print(user)

        elif self.ui_main.labelCurrentUser.text() == 'Главный технолог':
            user = 'Технолог'
            self.ui_main.labelCurrentUser.setText('Технолог')
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
        #зачем здесь параметры ClssDialog, self; parent=none; parent?


        self.setWindowTitle("Авторизация")
        self.resize(508, 114)

        self.pushButtonCancel = QtWidgets.QPushButton(self)
        self.pushButtonCancel.setGeometry(QtCore.QRect(70, 80, 80, 25))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.pushButtonCancel.setText("Отмена")
        self.pushButtonCancel.clicked.connect(self.btnClosed)

        self.pushButtonOk = QtWidgets.QPushButton(self)
        self.pushButtonOk.setGeometry(QtCore.QRect(340, 80, 80, 25))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.pushButtonOk.setText("Ок")
        self.pushButtonOk.clicked.connect(self.btnOk)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 20, 451, 17))
        self.label.setObjectName("label")
        self.label.setText("Введите пароль, чтобы получить права Главного технолога")

        self.lineEditPassword = QtWidgets.QLineEdit(self)
        self.lineEditPassword.setGeometry(QtCore.QRect(70, 50, 351, 23))
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.lineEditPassword.setObjectName("lineEdit")

    '''This method describes what should happen if button Cancel is pressed'''
    def btnClosed(self):

        global flag
        flag = 'Canceled'
        self.close()

    '''This method describes what should happen if button OK is pressed'''
    def btnOk(self):

        global flag
        if self.lineEditPassword.text() == PASSWORD:
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

class ConstantWindow(QtWidgets.QMainWindow):
    ''' Need to:
    Implement a function to save and load data
    "Save Button"
    Validate inputs!
    How to create new item
    Deleting items?
    '''

    '''Design of constant window is created via QtDesigner and was transformed to .py file from .ui
    Method init initialize this class from the ConstantWindow.py module
    AND put an image-logo from .png file (why .qrc?) I GUES IT SHOULD BE IMPLEMENTED AS A STAND ALONE METHOD for re-using
    AND makes columns width expand in dependence of window width'''
    def __init__(self, parent=None):
        global MT_hidden

        super(ConstantWindow, self).__init__(parent)
        self.ui = Ui_CheckConstantWindow()
        self.ui.setupUi(self)

        '''Put a logo'''
        #self.put_a_logo()
        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':' #@staticmethod???
        self.ui.putImageHere.setPixmap(pixmap)
        self.ui.labelCurrentUser.setText(user)
        '''Expand columns' width'''
        self.expandColumnsWidth()
        '''UNCOMMENT THIS when releasing the program
        vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'''
        # if user != 'Главный технолог':
        #     self.disableTablesIfNotChiefTech()
        '''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
        self.ui.pushButtonInitTableMTHousing.clicked.connect(self.upload_xlsx_file)
        #self.ui.pushButtonHideMTHousing.clicked.connect(self.button_hide_clicked) #replaced with universal method ''buttonHide2Clicked''

        self.ui.pushButtonSaveChanges.clicked.connect(self.btnSaveChangesClicked)
        self.ui.pushButtonAddItem.clicked.connect(self.showAddNewItemWindow)
        self.calculateAndBlockUneditableMTHousingTableValues()
        self.ui.TestButton.clicked.connect(self.addNewItem)

        self.setupHideButtons()

    #def put_a_logo(self):

    def setupHideButtons(self):
        self.ui.pushButtonTPSLine.clicked.connect(self.hideAllMT, MT_hidden)
        self.ui.pushButtonEZLine.clicked.connect(self.hideAllEZLine, EZLine_hidden)
        self.ui.pushButtonREDA.clicked.connect(self.hideAllREDA, REDA_hidden)
        self.ui.pushButtonOther.clicked.connect(self.hideAllOther, Other_hidden)

        self.ui.pushButtonHideMTHousing.clicked.connect(
            lambda checked, btn_name='MTHousing': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideMTHB.clicked.connect(lambda checked, btn_name='MTHB': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideMTDif.clicked.connect(lambda checked, btn_name='MTDif': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideMTLDif.clicked.connect(
            lambda checked, btn_name='MTLDif': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideMTBearing.clicked.connect(
            lambda checked, btn_name='MTBearing': self.buttonHide2Clicked(btn_name))

        self.ui.pushButtonHideEZLineHousing.clicked.connect(
            lambda checked, btn_name='EZLineHousing': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideEZLineHB.clicked.connect(
            lambda checked, btn_name='EZLineHB': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideEZLineDif.clicked.connect(
            lambda checked, btn_name='EZLineDif': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideEZLineLDif.clicked.connect(
            lambda checked, btn_name='EZLineLDif': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideEZLineBearing.clicked.connect(
            lambda checked, btn_name='EZLineBearing': self.buttonHide2Clicked(btn_name))

        self.ui.pushButtonHideREDAHousing.clicked.connect(
            lambda checked, btn_name='REDAHousing': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideREDAHB.clicked.connect(
            lambda checked, btn_name='REDAHB': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideREDADif.clicked.connect(
            lambda checked, btn_name='REDADif': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideREDALDif.clicked.connect(
            lambda checked, btn_name='REDALDif': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideREDABearing.clicked.connect(
            lambda checked, btn_name='REDABearing': self.buttonHide2Clicked(btn_name))

        self.ui.pushButtonHideOtherHousing.clicked.connect(
            lambda checked, btn_name='OtherHousing': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideOtherHB.clicked.connect(
            lambda checked, btn_name='OtherHB': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideOtherDif.clicked.connect(
            lambda checked, btn_name='OtherDif': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideOtherLDif.clicked.connect(
            lambda checked, btn_name='OtherLDif': self.buttonHide2Clicked(btn_name))
        self.ui.pushButtonHideOtherBearing.clicked.connect(
            lambda checked, btn_name='OtherBearing': self.buttonHide2Clicked(btn_name))

    def expandColumnsWidth(self):
        self.ui.tableWidgetMTHousing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetMTDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetMTLDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetMTBearing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetMTHB.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.ui.tableWidgetEZLineHousing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetEZLineDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetEZLineLDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetEZLineBearing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetEZLineHB.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.ui.tableWidgetREDAHousing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetREDADif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetREDALDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetREDABearing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetREDAHB.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.ui.tableWidgetOtherHousing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetOtherDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetOtherLDif.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetOtherBearing.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidgetOtherHB.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def showAddNewItemWindow(self):
        self.ui_new = NewItemWindow(self) #NewItemWindow(self) - ссылка на self как раз позволяет прицепить дочерний класс к родительскому. Т.е. у NewItemWindow - родитель self (constant_window)
        self.ui_new.open()
        self.ui_new.closeNewItemWindow()

    '''This method performs calculation of MT housings working length and blocks calculated values for edit even for cheif technologist'''
    def calculateAndBlockUneditableMTHousingTableValues(self):
        rows = self.ui.tableWidgetMTHousing.rowCount()
        #print(rows)
        for row in range(rows):
            work_housing_len_nom = round(
                                        float(self.ui.tableWidgetMTHousing.item(row, 4).text())
                                        - MT5A_FL_HEAD_LEN
                                        - MT5A_FL_BASE_LEN
                                        , 3)
            #print(work_housing_len_nom)
            work_housing_len_max = round(
                                        float(self.ui.tableWidgetMTHousing.item(row, 4).text())
                                        + float(self.ui.tableWidgetMTHousing.item(row, 5).text())
                                        - (MT5A_FL_HEAD_LEN - MT5A_FL_HEAD_LEN_LOW_DEV)
                                        - (MT5A_FL_BASE_LEN - MT5A_FL_BASE_LEN_LOW_DEV)
                                        , 3)
            #print(work_housing_len_max)
            work_housing_len_min = round(
                                        float(self.ui.tableWidgetMTHousing.item(row, 4).text())
                                        - float(self.ui.tableWidgetMTHousing.item(row, 6).text())
                                        - (MT5A_FL_HEAD_LEN + MT5A_FL_HEAD_LEN_LOW_DEV)
                                        - (MT5A_FL_BASE_LEN + MT5A_FL_BASE_LEN_LOW_DEV)
                                        , 3)
            #print(work_housing_len_min)

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
    def disableTablesIfNotChiefTech(self):

        self.ui.tableWidgetMTHousing.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetMTHB.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetMTDif.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetMTLDif.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetMTBearing.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ui.tableWidgetEZLineHousing.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetEZLineHB.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetEZLineDif.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetEZLineLDif.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetEZLineBearing.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ui.tableWidgetREDAHousing.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetREDAHB.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetREDADif.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetREDALDif.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetREDABearing.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ui.tableWidgetOtherHousing.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetOtherHB.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetOtherDif.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetOtherLDif.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidgetOtherBearing.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ui.pushButtonAddItem.hide()
        self.ui.pushButtonSaveChanges.hide()

    '''This method allows to hide all data about MT equipment by clicking TPS-line nameline 
    I changed it from if-else statement, but this invoked a bug: when hide a single TabWidget and clicking TPS-line nameline twice,
    TabWidget becomes visible with button labeled "Unhide" 
    NEED TO FIX IT'''
    def hideAllMT(self):
        global MT_hidden

        self.ui.tableWidgetMTHousing.setVisible(MT_hidden)
        self.ui.tableWidgetMTHB.setVisible(MT_hidden)
        self.ui.tableWidgetMTDif.setVisible(MT_hidden)
        self.ui.tableWidgetMTLDif.setVisible(MT_hidden)
        self.ui.tableWidgetMTBearing.setVisible(MT_hidden)

        self.ui.pushButtonHideMTHousing.setVisible(MT_hidden)
        self.ui.labelMTHousing.setVisible(MT_hidden)
        self.ui.pushButtonInitTableMTHousing.setVisible(MT_hidden)

        self.ui.pushButtonHideMTHB.setVisible(MT_hidden)
        self.ui.labelMTHB.setVisible(MT_hidden)
        self.ui.pushButtonInitTableMTHB.setVisible(MT_hidden)

        self.ui.pushButtonHideMTDif.setVisible(MT_hidden)
        self.ui.labelMTDif.setVisible(MT_hidden)
        self.ui.pushButtonInitTableMTDif.setVisible(MT_hidden)

        self.ui.pushButtonHideMTLDif.setVisible(MT_hidden)
        self.ui.labelMTLDif.setVisible(MT_hidden)
        self.ui.pushButtonInitTableMTLDif.setVisible(MT_hidden)

        self.ui.pushButtonHideMTBearing.setVisible(MT_hidden)
        self.ui.labelMTBearing.setVisible(MT_hidden)
        self.ui.pushButtonInitTableMTBearing.setVisible(MT_hidden)

        MT_hidden = not MT_hidden

    def hideAllEZLine(self):
        global EZLine_hidden

        self.ui.tableWidgetEZLineHousing.setVisible(EZLine_hidden)
        self.ui.tableWidgetEZLineHB.setVisible(EZLine_hidden)
        self.ui.tableWidgetEZLineDif.setVisible(EZLine_hidden)
        self.ui.tableWidgetEZLineLDif.setVisible(EZLine_hidden)
        self.ui.tableWidgetEZLineBearing.setVisible(EZLine_hidden)

        self.ui.pushButtonHideEZLineHousing.setVisible(EZLine_hidden)
        self.ui.labelEZLineHousing.setVisible(EZLine_hidden)
        self.ui.pushButtonInitTableEZLineHousing.setVisible(EZLine_hidden)

        self.ui.pushButtonHideEZLineHB.setVisible(EZLine_hidden)
        self.ui.labelEZLineHB.setVisible(EZLine_hidden)
        self.ui.pushButtonInitTableEZLineHB.setVisible(EZLine_hidden)

        self.ui.pushButtonHideEZLineDif.setVisible(EZLine_hidden)
        self.ui.labelEZLineDif.setVisible(EZLine_hidden)
        self.ui.pushButtonInitTableEZLineDif.setVisible(EZLine_hidden)

        self.ui.pushButtonHideEZLineLDif.setVisible(EZLine_hidden)
        self.ui.labelEZLineLDif.setVisible(EZLine_hidden)
        self.ui.pushButtonInitTableEZLineLDif.setVisible(EZLine_hidden)

        self.ui.pushButtonHideEZLineBearing.setVisible(EZLine_hidden)
        self.ui.labelEZLineBearing.setVisible(EZLine_hidden)
        self.ui.pushButtonInitTableEZLineBearing.setVisible(EZLine_hidden)

        EZLine_hidden = not EZLine_hidden

    def hideAllREDA(self):
        global REDA_hidden

        self.ui.tableWidgetREDAHousing.setVisible(REDA_hidden)
        self.ui.tableWidgetREDAHB.setVisible(REDA_hidden)
        self.ui.tableWidgetREDADif.setVisible(REDA_hidden)
        self.ui.tableWidgetREDALDif.setVisible(REDA_hidden)
        self.ui.tableWidgetREDABearing.setVisible(REDA_hidden)

        self.ui.pushButtonHideREDAHousing.setVisible(REDA_hidden)
        self.ui.labelREDAHousing.setVisible(REDA_hidden)
        self.ui.pushButtonInitTableREDAHousing.setVisible(REDA_hidden)

        self.ui.pushButtonHideREDAHB.setVisible(REDA_hidden)
        self.ui.labelREDAHB.setVisible(REDA_hidden)
        self.ui.pushButtonInitTableREDAHB.setVisible(REDA_hidden)

        self.ui.pushButtonHideREDADif.setVisible(REDA_hidden)
        self.ui.labelREDADif.setVisible(REDA_hidden)
        self.ui.pushButtonInitTableREDADif.setVisible(REDA_hidden)

        self.ui.pushButtonHideREDALDif.setVisible(REDA_hidden)
        self.ui.labelREDALDif.setVisible(REDA_hidden)
        self.ui.pushButtonInitTableREDALDif.setVisible(REDA_hidden)

        self.ui.pushButtonHideREDABearing.setVisible(REDA_hidden)
        self.ui.labelREDABearing.setVisible(REDA_hidden)
        self.ui.pushButtonInitTableREDABearing.setVisible(REDA_hidden)

        REDA_hidden = not REDA_hidden

    def hideAllOther(self):
        global Other_hidden

        self.ui.tableWidgetOtherHousing.setVisible(Other_hidden)
        self.ui.tableWidgetOtherHB.setVisible(Other_hidden)
        self.ui.tableWidgetOtherDif.setVisible(Other_hidden)
        self.ui.tableWidgetOtherLDif.setVisible(Other_hidden)
        self.ui.tableWidgetOtherBearing.setVisible(Other_hidden)

        self.ui.pushButtonHideOtherHousing.setVisible(Other_hidden)
        self.ui.labelOtherHousing.setVisible(Other_hidden)
        self.ui.pushButtonInitTableOtherHousing.setVisible(Other_hidden)

        self.ui.pushButtonHideOtherHB.setVisible(Other_hidden)
        self.ui.labelOtherHB.setVisible(Other_hidden)
        self.ui.pushButtonInitTableOtherHB.setVisible(Other_hidden)

        self.ui.pushButtonHideOtherDif.setVisible(Other_hidden)
        self.ui.labelOtherDif.setVisible(Other_hidden)
        self.ui.pushButtonInitTableOtherDif.setVisible(Other_hidden)

        self.ui.pushButtonHideOtherLDif.setVisible(Other_hidden)
        self.ui.labelOtherLDif.setVisible(Other_hidden)
        self.ui.pushButtonInitTableOtherLDif.setVisible(Other_hidden)

        self.ui.pushButtonHideOtherBearing.setVisible(Other_hidden)
        self.ui.labelOtherBearing.setVisible(Other_hidden)
        self.ui.pushButtonInitTableOtherBearing.setVisible(Other_hidden)

        Other_hidden = not Other_hidden

    '''This method allows to hide Table widget of MT Housings by clicking Hide/Unhide button'''
    # def button_hide_clicked(self):
    #     if self.ui.pushButtonHideMTHousing.text() == 'Hide':
    #         self.ui.tableWidgetMTHousing.setVisible(False)
    #         self.ui.pushButtonHideMTHousing.setText('Unhide')
    #     else:
    #         self.ui.tableWidgetMTHousing.setVisible(True)
    #         self.ui.pushButtonHideMTHousing.setText('Hide')

    '''This method allows to hide any Table widget dependantly on clicked button Hide/Unhide 
    It is not safe to use eval() - needed to be replaced'''
    def buttonHide2Clicked(self, btn_name):
        if eval('self.ui.pushButtonHide'+btn_name+'.text()') == 'Hide':
            eval('self.ui.tableWidget'+btn_name+'.setVisible(False)')
            eval('self.ui.pushButtonHide'+btn_name+'.setText(\'Unhide\')')
        else:
            eval('self.ui.tableWidget'+btn_name+'.setVisible(True)')
            eval('self.ui.pushButtonHide'+btn_name+'.setText(\'Hide\')')

    def closeConstantWindow(self):
        self.ui.pushButtonClose.clicked.connect(self.close)
        #self.ui.pushButton_backToMainWindow.clicked.connect(self.showMainWindow)
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
        self.calculateAndBlockUneditableMTHousingTableValues()

    def btnSaveChangesClicked(self):
        '''This method should save all changes to the memory'''
        pass
    # def showMainWindow(self):
    #     self.ui = MainWindow()
    #     self.ui.show()
    #     self.ui.MainWindow()

    # def test_func(self):
    #     print('herer')
    #     x = self.ui.tableWidgetMTHousing.rowCount()
    #     print(x)
    def addNewItem(self, new_item_product_line, new_item_type, new_item_data=[]):
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #Как это реализовать? Через условия? Через eval? Через словари?
        #[MT, EZLine, REDA, Other]
        #[Housing, Dif, LDif, Bearing, HB]
        print(new_item_product_line, new_item_type)

        if new_item_product_line == 'MT':
            if new_item_type == 'Housing':
                pass
                #[combo1,line1,combo3,combo4/5, -, line2,line3, - - -]
                # row_position = self.ui.tableWidgetMTHousing.rowCount()
                # self.ui.tableWidgetMTHousing.insertRow(row_position)
                # self.ui_main.tableWidgetMTHousing.setItem(row_position, 0, QtWidgets.QTableWidgetItem(new_item_data[0]))
                # self.ui_main.tableWidgetMTHousing.setItem(row_position, 1, QtWidgets.QTableWidgetItem(new_item_data[1]))
                # self.ui_main.tableWidgetMTHousing.setItem(row_position, 2, QtWidgets.QTableWidgetItem(new_item_data[2]))
                # self.ui_main.tableWidgetMTHousing.setItem(row_position, 3, QtWidgets.QTableWidgetItem(new_item_data[3]))
                # self.ui_main.tableWidgetMTHousing.setItem(row_position, 4, QtWidgets.QTableWidgetItem(new_item_data[4]))

            elif new_item_type == 'Dif':
                pass

            elif new_item_type == 'LDif':
                pass

            elif new_item_type == 'Bearing':
                pass

            else: #head&base
                pass

        elif new_item_product_line == 'EZLine':
            if new_item_type == 'Housing':
                pass

            elif new_item_type == 'Dif':
                pass

            elif new_item_type == 'LDif':
                pass

            elif new_item_type == 'Bearing':
                pass

            else:  # head&base
                pass

        elif new_item_product_line == 'REDA':
            if new_item_type == 'Housing':
                pass

            elif new_item_type == 'Dif':
                pass

            elif new_item_type == 'LDif':
                pass

            elif new_item_type == 'Bearing':
                pass

            else:  # head&base
                pass

        elif new_item_product_line == 'Other':
            if new_item_type == 'Housing':
                pass

            elif new_item_type == 'Dif':
                pass

            elif new_item_type == 'LDif':
                pass

            elif new_item_type == 'Bearing':
                pass

            else:  # head&base
                pass
        '''Здесь нужно в зависимости от типа добавляемой детали - выбирать таблицу для добавления.'''
        # row_position = self.ui.tableWidgetMTHousing.rowCount()
        # self.ui.tableWidgetMTHousing.insertRow(row_position)
        # self.ui_main.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(new_item_data[0]))
        # self.ui_main.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(new_item_data[1]))
        # self.ui_main.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(new_item_data[2]))
        # self.ui_main.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(new_item_data[3]))
        # self.ui_main.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(new_item_data[4]))

'''Нужно добавть очистку данных при изменении типа деталей'''
class NewItemWindow(QtWidgets.QDialog):
    chosen_product_line = ''
    comboBoxItemType_activated = False
    def __init__(self, parent=None):
        super(NewItemWindow, self).__init__(parent)
        self.parent = parent
        #print(self.parent, parent)
        self.ui_new = Ui_DialogCreateNewItem()
        self.ui_new.setupUi(self)

        self.ui_new.labelItemType.hide()
        self.ui_new.comboBoxItemType.hide()

        self.ui_new.labelItemParameters.hide()


        self.hideAllParameters()
        self.ui_new.comboBoxProductLine.currentTextChanged.connect(self.checkProductLine)
        self.ui_new.comboBoxItemType.currentTextChanged.connect(self.checkItemType)

        #self.ui_new.pushButtonSave.clicked.connect(self.saveNewItem)
    '''Hides all lineEdits, comboBoxes and labels for new item parameters'''
    '''Как скрыть все элементы по нормальному?'''
    '''Запихнуть в контейнер?Написать функцию на строку из булевых значений?'''
    def hideAllParameters(self):
        self.ui_new.labelSeriesRus.hide()
        self.ui_new.comboBoxSeriesRus.hide()
        self.ui_new.labelSeriesEng.hide()
        self.ui_new.comboBoxSeriesEng.hide()
        self.ui_new.labelHorB.hide()
        self.ui_new.comboBoxHorB.hide()
        self.ui_new.labelStagSize.hide()
        self.ui_new.lineEditStagSize.hide()
        self.ui_new.labelCompression.hide()
        self.ui_new.lineEditCompression.hide()
        self.ui_new.labelCRFL.hide()
        self.ui_new.comboBoxCRFL.hide()

        self.ui_new.labelLengthCodeRus.hide()
        self.ui_new.comboBoxLengthCodeRus.hide()
        self.ui_new.labelLengthCodeEng.hide()
        self.ui_new.comboBoxLengthCodeEng.hide()

        self.ui_new.labelHeight.hide()
        self.ui_new.lineEditHeight.hide()

        self.ui_new.labelUpDev.hide()
        self.ui_new.lineEditUpDev.hide()
        self.ui_new.labelLowDev.hide()
        self.ui_new.lineEditLowDev.hide()

        self.ui_new.labelBearingImp.hide()
        self.ui_new.comboBoxBearingImp.hide()
        self.ui_new.labelBearingMod.hide()
        self.ui_new.lineEditBearingMod.hide()

    def closeNewItemWindow(self):
        self.ui_new.pushButtonCancel.clicked.connect(self.close)


    '''def saveNewItem(self):
        print('hi')
        new_item_product_line = self.ui_new.comboBoxProductLine.currentText()
        new_item_type = self.ui_new.comboBoxItemType.currentText()
        if new_item_type == 'Корпус':
            combo_box_data = [f'{item.currentText()}' for item in
                          self.ui_new.groupBoxHousing.findChildren(QtWidgets.QComboBox)]
            line_edit_data = [f'{item.text()}' for item in self.ui_new.groupBoxHousing.findChildren(QtWidgets.QLineEdit)]
            # output_data = [line_edit_data[-1], *combo_box_data[:], *line_edit_data[:2]]
            # print(output_data)
        elif new_item_type == 'Направляющий аппарат':
            combo_box_data = [f'{item.currentText()}' for item in
                          self.ui_new.groupBoxDif.findChildren(QtWidgets.QComboBox)]
            line_edit_data = [f'{item.text()}' for item in self.ui_new.groupBoxDif.findChildren(QtWidgets.QLineEdit)]
        elif new_item_type == 'Нижний направляющий аппарат':
            combo_box_data = [f'{item.currentText()}' for item in
                          self.ui_new.groupBoxLDif.findChildren(QtWidgets.QComboBox)]
            line_edit_data = [f'{item.text()}' for item in self.ui_new.groupBoxLDif.findChildren(QtWidgets.QLineEdit)]
        elif new_item_type == 'Подшипник':
            combo_box_data = [f'{item.currentText()}' for item in
                          self.ui_new.groupBoxBearing.findChildren(QtWidgets.QComboBox)]
            line_edit_data = [f'{item.text()}' for item in self.ui_new.groupBoxBearing.findChildren(QtWidgets.QLineEdit)]
        elif new_item_type == 'Концевая деталь':
            combo_box_data = [f'{item.currentText()}' for item in
                          self.ui_new.groupBoxHB.findChildren(QtWidgets.QComboBox)]
            line_edit_data = [f'{item.text()}' for item in self.ui_new.groupBoxHB.findChildren(QtWidgets.QLineEdit)]
        else:
            print('Unknown item type')

        #combo_box_data = [f'{item.currentText()}' for item in self.ui_new.groupBoxHousing.findChildren(QtWidgets.QComboBox)]
        # line_edit_data = [f'{item.text()}' for item in self.findChildren(QLineEdit)]
        #combo_box_data = self.ui_new.groupBoxHousing.findChildren(QtWidgets.QComboBox)
        print(combo_box_data,line_edit_data)
        #Нужно передать сюда chosen_item_type и chosen_product_line, чтобы на основании этого можно было добвить новую строку в табилцу
        new_item_type = 'chosen_item_type'
        new_item_product_type = 'Product_line'
        self.close()
        self.parent.addNewItem(new_item_product_type, new_item_type)'''

    '''This method changes color design of the NewItemWindow dependantly on chosen product line'''
    def changeWindowColor(self, chosen_product_line):
        #self.ui_new.DialogCreateNewItem.setStyleSheet("background-color: rgb(255, 220, 220);") Почему не работает?
        #print(self.checkProductLine.chosen_product_line) Почему не работает?
        if chosen_product_line == 'TPS-Line':
            label_style = str("background-color: rgb(255, 181, 181);\n"
                              "color: rgb(255, 0, 0);\n"
                                                  "font: 75 15pt \"MS Sans Serif\";")
            #self.ui_new.DialogCreateNewItem.setStyleSheet("background-color: rgb(255, 220, 220);")

        elif chosen_product_line == 'EZLine':
            label_style = str("background-color: rgb(255, 255, 110);\n"
                              "color: rgb(181, 181, 0);\n"
                                                  "font: 75 15pt \"MS Sans Serif\";")
            #self.ui_new.DialogCreateNewItem.setStyleSheet("background-color: rgb(255, 255, 220);")
        elif chosen_product_line == 'REDA':
            label_style = str("background-color: rgb(144, 144, 255);\n"
                              "color: rgb(0, 0, 255);\n"
                                                  "font: 75 15pt \"MS Sans Serif\";")
            #self.ui_new.DialogCreateNewItem.setStyleSheet("background-color: rgb(220, 220, 255);")

        elif chosen_product_line == 'другое':
            label_style = str("background-color: rgb(181, 255, 181);\n"
                              "color: rgb(0, 181, 0);\n"
                                                  "font: 75 15pt \"MS Sans Serif\";")
        elif chosen_product_line == '':
            label_style = str("background-color: rgb(181, 181, 181);\n"
                          "color: rgb(255, 255, 255);\n"
                          "font: 75 15pt \"MS Sans Serif\";")
            #self.ui_new.DialogCreateNewItem.setStyleSheet("background-color: rgb(220, 255, 220);")


        self.ui_new.labelProductLine.setStyleSheet(label_style)
        self.ui_new.labelItemType.setStyleSheet(label_style)
        self.ui_new.labelItemParameters.setStyleSheet(label_style)


    def checkProductLine(self):
        print(self.comboBoxItemType_activated)


        chosen_product_line = self.ui_new.comboBoxProductLine.currentText()
        self.changeWindowColor(chosen_product_line)
        if chosen_product_line == '':
            self.ui_new.labelItemType.hide()
            self.ui_new.comboBoxItemType.hide()
            self.ui_new.labelItemParameters.hide()
            self.hideAllParameters()
        else:
            self.chosen_product_line = chosen_product_line #for conditional branch in checkItemType
            self.ui_new.labelItemType.show()
            self.ui_new.comboBoxItemType.show()
            print(1234)
            '''This condition is written for not showing spare part specific labels/lineEdits and comboBoxes when changing 
            product line comboBox value when comboBoxItemType is not activated yet and for changing spare part specific 
            labels/lineEdits and comboBoxes when comboBoxItemType is activated'''
            if self.comboBoxItemType_activated == True:
                self.checkItemType()


    def checkItemType(self):
        self.comboBoxItemType_activated = True
        chosen_item_type = self.ui_new.comboBoxItemType.currentText()
        self.ui_new.labelItemParameters.show()
        #ДНФ, КНФ?
        self.ui_new.labelUpDev.show()
        self.ui_new.lineEditUpDev.show()
        self.ui_new.labelLowDev.show()
        self.ui_new.lineEditLowDev.show()

        '''скрывает-показывает нужные поля label/lineEdit/comboBox в зависимости от выбранной детали'''
        '''Переписать по нормальному!'''
        if chosen_item_type == 'Корпус':
            if self.chosen_product_line == 'REDA' or self.chosen_product_line == 'EZLine':
                self.ui_new.labelSeriesRus.hide()
                self.ui_new.comboBoxSeriesRus.hide()
                self.ui_new.labelSeriesEng.show()
                self.ui_new.comboBoxSeriesEng.show()

                self.ui_new.labelLengthCodeRus.hide()
                self.ui_new.comboBoxLengthCodeRus.hide()
                self.ui_new.labelLengthCodeEng.show()
                self.ui_new.comboBoxLengthCodeEng.show()
            else:
                self.ui_new.labelSeriesRus.show()
                self.ui_new.comboBoxSeriesRus.show()
                self.ui_new.labelSeriesEng.hide()
                self.ui_new.comboBoxSeriesEng.hide()

                self.ui_new.labelLengthCodeRus.show()
                self.ui_new.comboBoxLengthCodeRus.show()
                self.ui_new.labelLengthCodeEng.hide()
                self.ui_new.comboBoxLengthCodeEng.hide()

            self.ui_new.labelHorB.hide()
            self.ui_new.comboBoxHorB.hide()
            self.ui_new.labelStagSize.hide()
            self.ui_new.lineEditStagSize.hide()
            self.ui_new.labelCompression.hide()
            self.ui_new.lineEditCompression.hide()
            self.ui_new.labelCRFL.show()                        ##
            self.ui_new.comboBoxCRFL.show()                     ##
            self.ui_new.labelHeight.hide()
            self.ui_new.lineEditHeight.hide()
            self.ui_new.labelBearingImp.hide()
            self.ui_new.comboBoxBearingImp.hide()
            self.ui_new.labelBearingMod.hide()
            self.ui_new.lineEditBearingMod.hide()
        elif chosen_item_type == 'Направляющий аппарат':
            if self.chosen_product_line == 'REDA' or self.chosen_product_line == 'EZLine':
                self.ui_new.labelSeriesRus.hide()
                self.ui_new.comboBoxSeriesRus.hide()
                self.ui_new.labelSeriesEng.show()
                self.ui_new.comboBoxSeriesEng.show()
            else:
                self.ui_new.labelSeriesRus.show()
                self.ui_new.comboBoxSeriesRus.show()
                self.ui_new.labelSeriesEng.hide()
                self.ui_new.comboBoxSeriesEng.hide()

            self.ui_new.labelLengthCodeRus.hide()
            self.ui_new.comboBoxLengthCodeRus.hide()
            self.ui_new.labelHorB.hide()
            self.ui_new.comboBoxHorB.hide()
            self.ui_new.labelStagSize.show()##
            self.ui_new.lineEditStagSize.show()##
            self.ui_new.labelCompression.show()##
            self.ui_new.lineEditCompression.show()##
            self.ui_new.labelCRFL.show()  ##
            self.ui_new.comboBoxCRFL.show()  ##
            self.ui_new.labelHeight.show()##
            self.ui_new.lineEditHeight.show()##
            self.ui_new.labelBearingImp.hide()
            self.ui_new.comboBoxBearingImp.hide()
            self.ui_new.labelBearingMod.hide()
            self.ui_new.lineEditBearingMod.hide()
        elif chosen_item_type == 'Нижний направляющий аппарат':
            if self.chosen_product_line == 'REDA' or self.chosen_product_line == 'EZLine':
                self.ui_new.labelSeriesRus.hide()
                self.ui_new.comboBoxSeriesRus.hide()
                self.ui_new.labelSeriesEng.show()
                self.ui_new.comboBoxSeriesEng.show()
            else:
                self.ui_new.labelSeriesRus.show()
                self.ui_new.comboBoxSeriesRus.show()
                self.ui_new.labelSeriesEng.hide()
                self.ui_new.comboBoxSeriesEng.hide()

            self.ui_new.labelLengthCodeRus.hide()
            self.ui_new.comboBoxLengthCodeRus.hide()
            self.ui_new.labelHorB.hide()
            self.ui_new.comboBoxHorB.hide()
            self.ui_new.labelStagSize.show()##
            self.ui_new.lineEditStagSize.show()##
            self.ui_new.labelCompression.hide()
            self.ui_new.lineEditCompression.hide()
            self.ui_new.labelCRFL.hide()
            self.ui_new.comboBoxCRFL.hide()
            self.ui_new.labelHeight.show()##
            self.ui_new.lineEditHeight.show()##
            self.ui_new.labelBearingImp.hide()
            self.ui_new.comboBoxBearingImp.hide()
            self.ui_new.labelBearingMod.hide()
            self.ui_new.lineEditBearingMod.hide()
        elif chosen_item_type == 'Подшипник':
            if self.chosen_product_line == 'REDA' or self.chosen_product_line == 'EZLine':
                self.ui_new.labelSeriesRus.hide()
                self.ui_new.comboBoxSeriesRus.hide()
                self.ui_new.labelSeriesEng.show()
                self.ui_new.comboBoxSeriesEng.show()
            else:
                self.ui_new.labelSeriesRus.show()
                self.ui_new.comboBoxSeriesRus.show()
                self.ui_new.labelSeriesEng.hide()
                self.ui_new.comboBoxSeriesEng.hide()

            self.ui_new.labelLengthCodeRus.hide()
            self.ui_new.comboBoxLengthCodeRus.hide()
            self.ui_new.labelHorB.hide()
            self.ui_new.comboBoxHorB.hide()
            self.ui_new.labelStagSize.show()##
            self.ui_new.lineEditStagSize.show()##
            self.ui_new.labelCompression.hide()
            self.ui_new.lineEditCompression.hide()
            self.ui_new.labelCRFL.hide()
            self.ui_new.comboBoxCRFL.hide()
            self.ui_new.labelHeight.show()##
            self.ui_new.lineEditHeight.show()##
            self.ui_new.labelBearingImp.show()##
            self.ui_new.comboBoxBearingImp.show()##
            self.ui_new.labelBearingMod.show()##
            self.ui_new.lineEditBearingMod.show()##
        elif chosen_item_type == 'Концевая деталь':
            if self.chosen_product_line == 'REDA' or self.chosen_product_line == 'EZLine':
                self.ui_new.labelSeriesRus.hide()
                self.ui_new.comboBoxSeriesRus.hide()
                self.ui_new.labelSeriesEng.show()
                self.ui_new.comboBoxSeriesEng.show()
            else:
                self.ui_new.labelSeriesRus.show()
                self.ui_new.comboBoxSeriesRus.show()
                self.ui_new.labelSeriesEng.hide()
                self.ui_new.comboBoxSeriesEng.hide()

            self.ui_new.labelLengthCodeRus.hide()
            self.ui_new.comboBoxLengthCodeRus.hide()
            self.ui_new.labelHorB.show()##
            self.ui_new.comboBoxHorB.show()##
            self.ui_new.labelStagSize.hide()
            self.ui_new.lineEditStagSize.hide()
            self.ui_new.labelCompression.hide()
            self.ui_new.lineEditCompression.hide()
            self.ui_new.labelCRFL.show()##
            self.ui_new.comboBoxCRFL.show()##
            self.ui_new.labelHeight.show()##
            self.ui_new.lineEditHeight.show()##
            self.ui_new.labelBearingImp.hide()
            self.ui_new.comboBoxBearingImp.hide()
            self.ui_new.labelBearingMod.hide()
            self.ui_new.lineEditBearingMod.hide()
        elif chosen_item_type == '':
            self.hideAllParameters()
            self.ui_new.labelItemParameters.hide()


class AboutWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(AboutWindow, self).__init__()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)
        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
        self.ui.putImageHere.setPixmap(pixmap)
        self.ui.labelCurrentUser.setText(user)

    def closeAboutWindow(self):
        self.ui.pushButtonClose.clicked.connect(self.close)
        #self.ui.pushButton_backToMainWindow.clicked.connect(self.showMainWindow)

    # def showMainWindow(self):
    #     self.ui = MainWindow()
    #     self.ui.show()
    #     self.ui.showMainWindow()

class PumpCalcWindow(QtWidgets.QMainWindow):#QtWidgets.QMainWindow):

    def __init__(self):
        super(PumpCalcWindow, self).__init__()
        self.ui = Ui_PumpCalcWindow()
        self.ui.setupUi(self)

        pixmap = QPixmap(':/images/logo.png')  # resource path starts with ':'
        self.ui.putImageHere.setPixmap(pixmap)
        self.ui.labelCurrentUser.setText(user)

    def closePumpCalcWindow(self):
        self.ui.pushButtonClose.clicked.connect(self.close)




        #self.ui.pushButton_backToMainWindow.clicked.connect(self.showMainWindow)

    # def showMainWindow(self):
    #     self.ui = MainWindow()
    #     self.ui.show()
    #     self.ui.showMainWindow()



    # for item in xl:
    #     print(xl[item])


    # Load a sheet into a DataFrame by name: df1
    #df1 = xl.parse('Sheet1')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.showMainWindow()
    #w.back_to_main_window()
    sys.exit(app.exec_())