# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\PycharmProjects\MUMT615\exp_chord_complexity\PairCompTestView.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(499, 473)
        self.btnRef = QtGui.QPushButton(Form)
        self.btnRef.setGeometry(QtCore.QRect(160, 40, 171, 131))
        self.btnRef.setObjectName(_fromUtf8("btnRef"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 170, 451, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 440, 491, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 450, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 180, 41, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.sldScore = QtGui.QSlider(Form)
        self.sldScore.setGeometry(QtCore.QRect(20, 210, 441, 31))
        self.sldScore.setMinimum(1)
        self.sldScore.setMaximum(7)
        self.sldScore.setOrientation(QtCore.Qt.Horizontal)
        self.sldScore.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.sldScore.setObjectName(_fromUtf8("sldScore"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 270, 341, 151))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 451, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btnNext = QtGui.QPushButton(Form)
        self.btnNext.setGeometry(QtCore.QRect(370, 300, 101, 111))
        self.btnNext.setObjectName(_fromUtf8("btnNext"))
        self.lbProg = QtGui.QLabel(Form)
        self.lbProg.setGeometry(QtCore.QRect(90, 450, 101, 21))
        self.lbProg.setText(_fromUtf8(""))
        self.lbProg.setObjectName(_fromUtf8("lbProg"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btnRef.setText(_translate("Form", "Chord", None))
        self.label_3.setText(_translate("Form", "Progress：", None))
        self.label.setText(_translate("Form", "Rating：", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>Instructions:</p><p>???</p></body></html>", None))
        self.label_4.setText(_translate("Form", "1                2                 3                4                5                6               7", None))
        self.btnNext.setText(_translate("Form", "Next", None))

