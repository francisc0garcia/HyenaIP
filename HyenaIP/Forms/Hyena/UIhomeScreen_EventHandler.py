import sys
from PyQt4 import QtGui, QtCore, Qt
from Forms.ImageAcquisitionModule.UIimageacquisition import *
from Forms.ImageAcquisitionModule.UIimageacquisition_EventHandler import *

ParentUI = 0

class GUI_UIimageacquisition(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.GUI_UIimageacquisition =  Ui_ImageAcquisition()
        self.GUI_UIimageacquisition.setupUi(self)
        self.update()

        UIimageacquisition_LoadEvents(self)


def LoadEvents(parent):
    '''
    Connect events to controls and define behaviour in UI elements
    '''
    global ParentUI
    ParentUI = parent

    '''
    Defiine event
    '''
    def on_BtnImageDAQ_clicked():
        ParentUI.w = GUI_UIimageacquisition()
        ParentUI.w.show()

    def on_BtnCreateLoad_clicked():
        ShowFileDialog()

    '''
    Connect controls to events
    '''
    ParentUI.ui.BtnCreateLoad.clicked.connect(on_BtnCreateLoad_clicked)
    ParentUI.ui.BtnImageDAQ.clicked.connect(on_BtnImageDAQ_clicked)
    ParentUI.ui.actionExit.triggered.connect(CloseWindow)

def CloseWindow():
    sys.exit(0)
    
def ShowFileDialog():
    fname = QtGui.QFileDialog.getExistingDirectory(ParentUI, 'Open File', '/home')
    ParentUI.ui.TextEditDirectoryPath.appendPlainText(fname)

