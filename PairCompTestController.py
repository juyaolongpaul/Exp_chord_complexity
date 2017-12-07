import sys
import time
from libAudioPlayer import Player
import PairCompTestView
import PairCompTestModel
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Dialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.resize(500, 200)
        grid = QGridLayout()

        grid.addWidget(QLabel("McGill ID:", parent=self), 0, 0, 1, 1)
        self.leName = QLineEdit(parent=self)
        grid.addWidget(self.leName, 0, 1, 1, 1)
        grid.addWidget(QLabel("Age:", parent=self), 1, 0, 1, 1)
        self.age = QLineEdit(parent=self)
        grid.addWidget(self.age, 1, 1, 1, 1)
        grid.addWidget(QLabel("Estimate years of formal musical training:", parent=self), 2, 0, 1, 1)
        self.year = QLineEdit(parent=self)
        grid.addWidget(self.year, 2, 1, 1, 1)
        grid.addWidget(QLabel("Do you have absolute pitch? (Y/N)", parent=self), 3, 0, 1, 1)
        self.pitch = QLineEdit(parent=self)
        grid.addWidget(self.pitch, 3, 1, 1, 1)

        buttonBox = QDialogButtonBox(parent=self)
        buttonBox.setOrientation(Qt.Horizontal)

        buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        layout = QVBoxLayout()
        layout.addLayout(grid)
        spacerItem = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def name(self):
        return self.leName.text(), self.age.text(), self.year.text(), self.pitch.text()


class ExpController(QWidget, PairCompTestView.Ui_Form):
    """ 
    Controller of the Mos test experiment.
    Controller is the MVC's controller.
    """

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.player = Player()
        dirName = QFileDialog.getExistingDirectory(self, "Open Experiment Directory", QString())
        qDebug(dirName)
        self.m_model = PairCompTestModel.ExpModel(str(dirName))  # this is a model
        self.stimSeq = self.m_model.getExpSeq()
        self.stimCounter = 0
        # mapping with the GUI components
        self.btnNext.clicked.connect(self.setNext)
        #self.btnRef_3.clicked.connect(self.playRef)
        # self.btnRef.setEnabled(False)
        self.btnRef.clicked.connect(self.playRef)
        #self.btnRef_2.clicked.connect(self.playRef_3)
        dialog = Dialog(parent=self)
        if dialog.exec_():
            self.m_model.testerName, self.m_model.testerAge, self.m_model.testerYears, self.m_model.testerPitch = dialog.name()
    def closeEvent(self, event):
        del self.player
        event.accept()

    def playRef(self):
        self.player.playFile(self.stimSeq[self.stimCounter][-1])

    def playRef_2(self):
        self.player.playFile(self.stimSeq[self.stimCounter][0])

    def playRef_3(self):
        self.player.playFile(self.stimSeq[self.stimCounter][1])
        # def playExp(self):
        #self.player.playTwoFile(self.stimSeq[self.stimCounter][0], self.stimSeq[self.stimCounter][1])

    def getScore(self):
        return (self.sldScore.value())

    def setNext(self):
        self.player.stopPlay()
        
        qscore = self.getScore() 
        if qscore == -1000:
            msgBox = QMessageBox()
            msgBox.setText("Please give score")
            msgBox.exec_()
            return
        self.m_model.setScore([(self.stimSeq[self.stimCounter][0], self.stimSeq[self.stimCounter][1]), qscore])

        if self.stimCounter == len(self.stimSeq) - 1:
            QMessageBox.information(self, 'Information', 'Experiments ended, thanks!')
            self.m_model.writeResult()
        self.stimCounter += 1

        qDebug("stimCounter: " + str(self.stimCounter))
        #self.lbProg.setText("%d/%d. Please wait 5s after clicking 'Next'" % (self.stimCounter + 1, len(self.stimSeq)))
        time.sleep(5)  # let the user wait for 5s
        self.lbProg.setText("%d/%d." % (self.stimCounter + 1, len(self.stimSeq)))
        #QMessageBox.information(self, 'Please wait', 'Please wait 10s')
        '''msgBox = QMessageBox()
        msgBox.setText("Please wait 10s")
        timer =QTimer()
        timer.singleShot(10000, msgBox, SLOT('close'))


        msgBox.exec_()
        #time.sleep(10)
        msgBox = QMessageBox()
        msgBox.setText("Time is up, you can rate and proceed!")
        timer = QTimer()
        timer.singleShot(10000, msgBox.Abort)
        msgBox.exec_()'''
    def giveScore(self):
        pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ExpObject = ExpController()
    ExpObject.show()
    sys.exit(app.exec_())
