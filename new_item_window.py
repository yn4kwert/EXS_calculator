# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wado9\PycharmProjects\EXS_calculator\new_item_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogCreateNewItem(object):
    def setupUi(self, DialogCreateNewItem):
        DialogCreateNewItem.setObjectName("DialogCreateNewItem")
        DialogCreateNewItem.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogCreateNewItem.resize(896, 667)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogCreateNewItem.sizePolicy().hasHeightForWidth())
        DialogCreateNewItem.setSizePolicy(sizePolicy)
        DialogCreateNewItem.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DialogCreateNewItem)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelProductLine = QtWidgets.QLabel(DialogCreateNewItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProductLine.sizePolicy().hasHeightForWidth())
        self.labelProductLine.setSizePolicy(sizePolicy)
        self.labelProductLine.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.labelProductLine.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductLine.setObjectName("labelProductLine")
        self.verticalLayout.addWidget(self.labelProductLine)
        self.comboBoxProductLine = QtWidgets.QComboBox(DialogCreateNewItem)
        self.comboBoxProductLine.setObjectName("comboBoxProductLine")
        self.comboBoxProductLine.addItem("")
        self.comboBoxProductLine.setItemText(0, "")
        self.comboBoxProductLine.addItem("")
        self.comboBoxProductLine.addItem("")
        self.comboBoxProductLine.addItem("")
        self.comboBoxProductLine.addItem("")
        self.verticalLayout.addWidget(self.comboBoxProductLine)
        self.labelItemType = QtWidgets.QLabel(DialogCreateNewItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelItemType.sizePolicy().hasHeightForWidth())
        self.labelItemType.setSizePolicy(sizePolicy)
        self.labelItemType.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.labelItemType.setAlignment(QtCore.Qt.AlignCenter)
        self.labelItemType.setObjectName("labelItemType")
        self.verticalLayout.addWidget(self.labelItemType)
        self.comboBoxItemType = QtWidgets.QComboBox(DialogCreateNewItem)
        self.comboBoxItemType.setObjectName("comboBoxItemType")
        self.comboBoxItemType.addItem("")
        self.comboBoxItemType.setItemText(0, "")
        self.comboBoxItemType.addItem("")
        self.comboBoxItemType.addItem("")
        self.comboBoxItemType.addItem("")
        self.comboBoxItemType.addItem("")
        self.comboBoxItemType.addItem("")
        self.verticalLayout.addWidget(self.comboBoxItemType)
        self.labelItemParameters = QtWidgets.QLabel(DialogCreateNewItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelItemParameters.sizePolicy().hasHeightForWidth())
        self.labelItemParameters.setSizePolicy(sizePolicy)
        self.labelItemParameters.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.labelItemParameters.setAlignment(QtCore.Qt.AlignCenter)
        self.labelItemParameters.setObjectName("labelItemParameters")
        self.verticalLayout.addWidget(self.labelItemParameters)
        self.formLayoutParameters = QtWidgets.QFormLayout()
        self.formLayoutParameters.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayoutParameters.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayoutParameters.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayoutParameters.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayoutParameters.setObjectName("formLayoutParameters")
        self.labelSeriesRus = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelSeriesRus.setObjectName("labelSeriesRus")
        self.formLayoutParameters.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelSeriesRus)
        self.comboBoxSeriesRus = QtWidgets.QComboBox(DialogCreateNewItem)
        self.comboBoxSeriesRus.setObjectName("comboBoxSeriesRus")
        self.comboBoxSeriesRus.addItem("")
        self.comboBoxSeriesRus.addItem("")
        self.comboBoxSeriesRus.addItem("")
        self.formLayoutParameters.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxSeriesRus)
        self.labelSeriesEng = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelSeriesEng.setObjectName("labelSeriesEng")
        self.formLayoutParameters.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelSeriesEng)
        self.comboBoxSeriesEng = QtWidgets.QComboBox(DialogCreateNewItem)
        self.comboBoxSeriesEng.setObjectName("comboBoxSeriesEng")
        self.comboBoxSeriesEng.addItem("")
        self.comboBoxSeriesEng.addItem("")
        self.comboBoxSeriesEng.addItem("")
        self.comboBoxSeriesEng.addItem("")
        self.comboBoxSeriesEng.addItem("")
        self.comboBoxSeriesEng.addItem("")
        self.formLayoutParameters.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxSeriesEng)
        self.labelHorB = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelHorB.setObjectName("labelHorB")
        self.formLayoutParameters.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelHorB)
        self.comboBoxHorB = QtWidgets.QComboBox(DialogCreateNewItem)
        self.comboBoxHorB.setObjectName("comboBoxHorB")
        self.comboBoxHorB.addItem("")
        self.comboBoxHorB.addItem("")
        self.formLayoutParameters.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBoxHorB)
        self.labelStagSize = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelStagSize.setObjectName("labelStagSize")
        self.formLayoutParameters.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelStagSize)
        self.lineEditStagSize = QtWidgets.QLineEdit(DialogCreateNewItem)
        self.lineEditStagSize.setObjectName("lineEditStagSize")
        self.formLayoutParameters.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditStagSize)
        self.labelLengthCodeRus = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelLengthCodeRus.setObjectName("labelLengthCodeRus")
        self.formLayoutParameters.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelLengthCodeRus)
        self.comboBoxLengthCodeRus = QtWidgets.QComboBox(DialogCreateNewItem)
        self.comboBoxLengthCodeRus.setObjectName("comboBoxLengthCodeRus")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.comboBoxLengthCodeRus.addItem("")
        self.formLayoutParameters.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBoxLengthCodeRus)
        self.labelLengthCodeEng = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelLengthCodeEng.setObjectName("labelLengthCodeEng")
        self.formLayoutParameters.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.labelLengthCodeEng)
        self.comboBoxLengthCodeEng = QtWidgets.QComboBox(DialogCreateNewItem)
        self.comboBoxLengthCodeEng.setObjectName("comboBoxLengthCodeEng")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.comboBoxLengthCodeEng.addItem("")
        self.formLayoutParameters.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.comboBoxLengthCodeEng)
        self.labelHeight = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelHeight.setObjectName("labelHeight")
        self.formLayoutParameters.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.labelHeight)
        self.lineEditHeight = QtWidgets.QLineEdit(DialogCreateNewItem)
        self.lineEditHeight.setObjectName("lineEditHeight")
        self.formLayoutParameters.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEditHeight)
        self.labelUpDev = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelUpDev.setObjectName("labelUpDev")
        self.formLayoutParameters.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.labelUpDev)
        self.lineEditUpDev = QtWidgets.QLineEdit(DialogCreateNewItem)
        self.lineEditUpDev.setObjectName("lineEditUpDev")
        self.formLayoutParameters.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEditUpDev)
        self.labelLowDev = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelLowDev.setObjectName("labelLowDev")
        self.formLayoutParameters.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.labelLowDev)
        self.lineEditLowDev = QtWidgets.QLineEdit(DialogCreateNewItem)
        self.lineEditLowDev.setObjectName("lineEditLowDev")
        self.formLayoutParameters.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEditLowDev)
        self.labelBearingImp = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelBearingImp.setObjectName("labelBearingImp")
        self.formLayoutParameters.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.labelBearingImp)
        self.comboBoxBearingImp = QtWidgets.QComboBox(DialogCreateNewItem)
        self.comboBoxBearingImp.setObjectName("comboBoxBearingImp")
        self.comboBoxBearingImp.addItem("")
        self.comboBoxBearingImp.addItem("")
        self.comboBoxBearingImp.addItem("")
        self.formLayoutParameters.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.comboBoxBearingImp)
        self.labelBearingMod = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelBearingMod.setObjectName("labelBearingMod")
        self.formLayoutParameters.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.labelBearingMod)
        self.lineEditBearingMod = QtWidgets.QLineEdit(DialogCreateNewItem)
        self.lineEditBearingMod.setObjectName("lineEditBearingMod")
        self.formLayoutParameters.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lineEditBearingMod)
        self.comboBoxCRFL = QtWidgets.QComboBox(DialogCreateNewItem)
        self.comboBoxCRFL.setObjectName("comboBoxCRFL")
        self.comboBoxCRFL.addItem("")
        self.comboBoxCRFL.addItem("")
        self.formLayoutParameters.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBoxCRFL)
        self.labelCRFL = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelCRFL.setObjectName("labelCRFL")
        self.formLayoutParameters.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelCRFL)
        self.labelCompression = QtWidgets.QLabel(DialogCreateNewItem)
        self.labelCompression.setObjectName("labelCompression")
        self.formLayoutParameters.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelCompression)
        self.lineEditCompression = QtWidgets.QLineEdit(DialogCreateNewItem)
        self.lineEditCompression.setObjectName("lineEditCompression")
        self.formLayoutParameters.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditCompression)
        self.verticalLayout.addLayout(self.formLayoutParameters)
        self.widget = QtWidgets.QWidget(DialogCreateNewItem)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonSave = QtWidgets.QPushButton(DialogCreateNewItem)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogCreateNewItem)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DialogCreateNewItem)
        QtCore.QMetaObject.connectSlotsByName(DialogCreateNewItem)

    def retranslateUi(self, DialogCreateNewItem):
        _translate = QtCore.QCoreApplication.translate
        DialogCreateNewItem.setWindowTitle(_translate("DialogCreateNewItem", "Добавление новой детали"))
        self.labelProductLine.setText(_translate("DialogCreateNewItem", "Выберите линейку оборудования:"))
        self.comboBoxProductLine.setItemText(1, _translate("DialogCreateNewItem", "TPS-Line"))
        self.comboBoxProductLine.setItemText(2, _translate("DialogCreateNewItem", "EZLine"))
        self.comboBoxProductLine.setItemText(3, _translate("DialogCreateNewItem", "REDA"))
        self.comboBoxProductLine.setItemText(4, _translate("DialogCreateNewItem", "другое"))
        self.labelItemType.setText(_translate("DialogCreateNewItem", "Выберите тип детали:"))
        self.comboBoxItemType.setItemText(1, _translate("DialogCreateNewItem", "Корпус"))
        self.comboBoxItemType.setItemText(2, _translate("DialogCreateNewItem", "Направляющий аппарат"))
        self.comboBoxItemType.setItemText(3, _translate("DialogCreateNewItem", "Нижний направляющий аппарат"))
        self.comboBoxItemType.setItemText(4, _translate("DialogCreateNewItem", "Подшипник"))
        self.comboBoxItemType.setItemText(5, _translate("DialogCreateNewItem", "Концевая деталь"))
        self.labelItemParameters.setText(_translate("DialogCreateNewItem", "Укажите параметры детали:"))
        self.labelSeriesRus.setText(_translate("DialogCreateNewItem", "Серия"))
        self.comboBoxSeriesRus.setItemText(0, _translate("DialogCreateNewItem", "2A"))
        self.comboBoxSeriesRus.setItemText(1, _translate("DialogCreateNewItem", "5"))
        self.comboBoxSeriesRus.setItemText(2, _translate("DialogCreateNewItem", "5A"))
        self.labelSeriesEng.setText(_translate("DialogCreateNewItem", "Серия, eng"))
        self.comboBoxSeriesEng.setItemText(0, _translate("DialogCreateNewItem", "A"))
        self.comboBoxSeriesEng.setItemText(1, _translate("DialogCreateNewItem", "D"))
        self.comboBoxSeriesEng.setItemText(2, _translate("DialogCreateNewItem", "G"))
        self.comboBoxSeriesEng.setItemText(3, _translate("DialogCreateNewItem", "H"))
        self.comboBoxSeriesEng.setItemText(4, _translate("DialogCreateNewItem", "J"))
        self.comboBoxSeriesEng.setItemText(5, _translate("DialogCreateNewItem", "S"))
        self.labelHorB.setText(_translate("DialogCreateNewItem", "Тип концевой детали"))
        self.comboBoxHorB.setItemText(0, _translate("DialogCreateNewItem", "Голова"))
        self.comboBoxHorB.setItemText(1, _translate("DialogCreateNewItem", "Основание"))
        self.labelStagSize.setText(_translate("DialogCreateNewItem", "Типоразмер ступени"))
        self.labelLengthCodeRus.setText(_translate("DialogCreateNewItem", "Шифр длины, м"))
        self.comboBoxLengthCodeRus.setItemText(0, _translate("DialogCreateNewItem", "0.5"))
        self.comboBoxLengthCodeRus.setItemText(1, _translate("DialogCreateNewItem", "1"))
        self.comboBoxLengthCodeRus.setItemText(2, _translate("DialogCreateNewItem", "1.5"))
        self.comboBoxLengthCodeRus.setItemText(3, _translate("DialogCreateNewItem", "2"))
        self.comboBoxLengthCodeRus.setItemText(4, _translate("DialogCreateNewItem", "2.5"))
        self.comboBoxLengthCodeRus.setItemText(5, _translate("DialogCreateNewItem", "3"))
        self.comboBoxLengthCodeRus.setItemText(6, _translate("DialogCreateNewItem", "3.5"))
        self.comboBoxLengthCodeRus.setItemText(7, _translate("DialogCreateNewItem", "4"))
        self.comboBoxLengthCodeRus.setItemText(8, _translate("DialogCreateNewItem", "4.5"))
        self.comboBoxLengthCodeRus.setItemText(9, _translate("DialogCreateNewItem", "5"))
        self.comboBoxLengthCodeRus.setItemText(10, _translate("DialogCreateNewItem", "5.5"))
        self.comboBoxLengthCodeRus.setItemText(11, _translate("DialogCreateNewItem", "6"))
        self.comboBoxLengthCodeRus.setItemText(12, _translate("DialogCreateNewItem", "6.5"))
        self.comboBoxLengthCodeRus.setItemText(13, _translate("DialogCreateNewItem", "7"))
        self.comboBoxLengthCodeRus.setItemText(14, _translate("DialogCreateNewItem", "7.5"))
        self.comboBoxLengthCodeRus.setItemText(15, _translate("DialogCreateNewItem", "8"))
        self.comboBoxLengthCodeRus.setItemText(16, _translate("DialogCreateNewItem", "8.5"))
        self.comboBoxLengthCodeRus.setItemText(17, _translate("DialogCreateNewItem", "9"))
        self.comboBoxLengthCodeRus.setItemText(18, _translate("DialogCreateNewItem", "9.5"))
        self.comboBoxLengthCodeRus.setItemText(19, _translate("DialogCreateNewItem", "10"))
        self.labelLengthCodeEng.setText(_translate("DialogCreateNewItem", "Шифр длины, #"))
        self.comboBoxLengthCodeEng.setItemText(0, _translate("DialogCreateNewItem", "#10"))
        self.comboBoxLengthCodeEng.setItemText(1, _translate("DialogCreateNewItem", "#20"))
        self.comboBoxLengthCodeEng.setItemText(2, _translate("DialogCreateNewItem", "#30"))
        self.comboBoxLengthCodeEng.setItemText(3, _translate("DialogCreateNewItem", "#40"))
        self.comboBoxLengthCodeEng.setItemText(4, _translate("DialogCreateNewItem", "#50"))
        self.comboBoxLengthCodeEng.setItemText(5, _translate("DialogCreateNewItem", "#60"))
        self.comboBoxLengthCodeEng.setItemText(6, _translate("DialogCreateNewItem", "#70"))
        self.comboBoxLengthCodeEng.setItemText(7, _translate("DialogCreateNewItem", "#80"))
        self.comboBoxLengthCodeEng.setItemText(8, _translate("DialogCreateNewItem", "#90"))
        self.comboBoxLengthCodeEng.setItemText(9, _translate("DialogCreateNewItem", "#100"))
        self.comboBoxLengthCodeEng.setItemText(10, _translate("DialogCreateNewItem", "#110"))
        self.comboBoxLengthCodeEng.setItemText(11, _translate("DialogCreateNewItem", "#120"))
        self.comboBoxLengthCodeEng.setItemText(12, _translate("DialogCreateNewItem", "#130"))
        self.comboBoxLengthCodeEng.setItemText(13, _translate("DialogCreateNewItem", "#140"))
        self.comboBoxLengthCodeEng.setItemText(14, _translate("DialogCreateNewItem", "#150"))
        self.comboBoxLengthCodeEng.setItemText(15, _translate("DialogCreateNewItem", "#160"))
        self.labelHeight.setText(_translate("DialogCreateNewItem", "Высота, мм"))
        self.labelUpDev.setText(_translate("DialogCreateNewItem", "Допуск вверх, мм"))
        self.labelLowDev.setText(_translate("DialogCreateNewItem", "Допуск вниз, мм"))
        self.labelBearingImp.setText(_translate("DialogCreateNewItem", "Колесо ПП"))
        self.comboBoxBearingImp.setItemText(0, _translate("DialogCreateNewItem", "Отсутствует"))
        self.comboBoxBearingImp.setItemText(1, _translate("DialogCreateNewItem", "Короткое"))
        self.comboBoxBearingImp.setItemText(2, _translate("DialogCreateNewItem", "Обычное"))
        self.labelBearingMod.setText(_translate("DialogCreateNewItem", "Модификация ПП"))
        self.comboBoxCRFL.setItemText(0, _translate("DialogCreateNewItem", "CR"))
        self.comboBoxCRFL.setItemText(1, _translate("DialogCreateNewItem", "FL"))
        self.labelCRFL.setText(_translate("DialogCreateNewItem", "CR/FL"))
        self.labelCompression.setText(_translate("DialogCreateNewItem", "Компрессия на ступень, мкм"))
        self.pushButtonSave.setText(_translate("DialogCreateNewItem", "Сохранить"))
        self.pushButtonCancel.setText(_translate("DialogCreateNewItem", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogCreateNewItem = QtWidgets.QDialog()
    ui = Ui_DialogCreateNewItem()
    ui.setupUi(DialogCreateNewItem)
    DialogCreateNewItem.show()
    sys.exit(app.exec_())
