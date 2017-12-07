# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/yaolongju/PycharmProjects/Exp_chord_complexity/PairCompTestView.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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
        self.btnRef.setGeometry(QtCore.QRect(160, 0, 171, 131))
        self.btnRef.setObjectName(_fromUtf8("btnRef"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 130, 451, 16))
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
        self.label.setGeometry(QtCore.QRect(20, 150, 41, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.sldScore = QtGui.QSlider(Form)
        self.sldScore.setGeometry(QtCore.QRect(20, 180, 441, 31))
        self.sldScore.setMinimum(1)
        self.sldScore.setMaximum(7)
        self.sldScore.setOrientation(QtCore.Qt.Horizontal)
        self.sldScore.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.sldScore.setObjectName(_fromUtf8("sldScore"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 230, 341, 191))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 451, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btnNext = QtGui.QPushButton(Form)
        self.btnNext.setGeometry(QtCore.QRect(370, 300, 101, 111))
        self.btnNext.setObjectName(_fromUtf8("btnNext"))
        self.lbProg = QtGui.QLabel(Form)
        self.lbProg.setGeometry(QtCore.QRect(80, 450, 261, 21))
        self.lbProg.setText(_fromUtf8(""))
        self.lbProg.setObjectName(_fromUtf8("lbProg"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btnRef.setText(_translate("Form", "Chord", None))
        self.label_3.setText(_translate("Form", "Progress：", None))
        self.label.setText(_translate("Form", "Rating：", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>Instructions:</p><p><span style=\" font-family:\'SF Optimized,system-ui,-apple-system,BlinkMacSystemFont,.SFNSText-Regular,sans-serif\'; font-size:10pt; color:#000000; background-color:#f1f0f0;\">This experiment contains 150 audio examples of chords. You will hear each chord only once. After listening to each chord, you will give your rating, based on how “complex” you think the chord is, by using the sliding scale: 1 = least complex; 7 = most complex.</span></p><p><span style=\" font-family:\'SF Optimized,system-ui,-apple-system,BlinkMacSystemFont,.SFNSText-Regular,sans-serif\'; font-size:10pt; color:#000000; background-color:#f1f0f0;\">To begin the experiment, press the button labeled “Chord.” To record your response, drag the slider to your chosen complexity rating (1-7), and click the “Next” button. The program will pause for 5 seconds. After 5 seconds or when the “Progress” number increases by one, you may proceed. Press “Chord” again to listen to the next example.</span><br/></p></body></html>", None))
        self.label_4.setText(_translate("Form", "1                  2                   3                  4                  5                 6                7", None))
        self.btnNext.setText(_translate("Form", "Next", None))

