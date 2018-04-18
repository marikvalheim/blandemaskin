# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstgui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myfirstgui(object):
    def setupUi(self, myfirstgui):
        myfirstgui.setObjectName("myfirstgui")
        myfirstgui.resize(583, 286)
        self.buttonBox = QtWidgets.QDialogButtonBox(myfirstgui)
        self.buttonBox.setGeometry(QtCore.QRect(-300, 260, 381, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.Vatn = QtWidgets.QDial(myfirstgui)
        self.Vatn.setGeometry(QtCore.QRect(200, 10, 171, 171))
        self.Vatn.setMaximum(100)
        self.Vatn.setNotchesVisible(True)
        self.Vatn.setObjectName("Vatn")
        self.Number_Vodka = QtWidgets.QLCDNumber(myfirstgui)
        self.Number_Vodka.setGeometry(QtCore.QRect(80, 190, 51, 41))
        self.Number_Vodka.setDigitCount(3)
        self.Number_Vodka.setObjectName("Number_Vodka")
        self.Saft = QtWidgets.QDial(myfirstgui)
        self.Saft.setGeometry(QtCore.QRect(370, 10, 201, 171))
        self.Saft.setMaximum(100)
        self.Saft.setNotchesVisible(True)
        self.Saft.setObjectName("Saft")
        self.Vodka = QtWidgets.QDial(myfirstgui)
        self.Vodka.setGeometry(QtCore.QRect(20, 10, 181, 171))
        self.Vodka.setMaximum(100)
        self.Vodka.setNotchesVisible(True)
        self.Vodka.setObjectName("Vodka")
        self.pushButton_1 = QtWidgets.QPushButton(myfirstgui)
        self.pushButton_1.setGeometry(QtCore.QRect(500, 240, 75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.Number_Vatn = QtWidgets.QLCDNumber(myfirstgui)
        self.Number_Vatn.setGeometry(QtCore.QRect(250, 190, 51, 41))
        self.Number_Vatn.setDigitCount(3)
        self.Number_Vatn.setObjectName("Number_Vatn")
        self.Number_Saft = QtWidgets.QLCDNumber(myfirstgui)
        self.Number_Saft.setGeometry(QtCore.QRect(440, 180, 51, 41))
        self.Number_Saft.setDigitCount(3)
        self.Number_Saft.setObjectName("Number_Saft")
        self.label_Vodka = QtWidgets.QLabel(myfirstgui)
        self.label_Vodka.setGeometry(QtCore.QRect(90, 90, 47, 13))
        self.label_Vodka.setObjectName("label_Vodka")
        self.label_Vatn = QtWidgets.QLabel(myfirstgui)
        self.label_Vatn.setGeometry(QtCore.QRect(260, 80, 47, 13))
        self.label_Vatn.setObjectName("label_Vatn")
        self.label_Saft = QtWidgets.QLabel(myfirstgui)
        self.label_Saft.setGeometry(QtCore.QRect(440, 90, 47, 13))
        self.label_Saft.setObjectName("label_Saft")

        self.retranslateUi(myfirstgui)
        self.buttonBox.accepted.connect(myfirstgui.accept)
        self.buttonBox.rejected.connect(myfirstgui.reject)
        QtCore.QMetaObject.connectSlotsByName(myfirstgui)

    def retranslateUi(self, myfirstgui):
        _translate = QtCore.QCoreApplication.translate
        myfirstgui.setWindowTitle(_translate("myfirstgui", "My First Gui!"))
        self.pushButton_1.setText(_translate("myfirstgui", "MIX"))
        self.label_Vodka.setText(_translate("myfirstgui", "Vodka"))
        self.label_Vatn.setText(_translate("myfirstgui", "Vatn"))
        self.label_Saft.setText(_translate("myfirstgui", "Saft"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myfirstgui = QtWidgets.QDialog()
    ui = Ui_myfirstgui()
    ui.setupUi(myfirstgui)
    myfirstgui.show()
    sys.exit(app.exec_())

