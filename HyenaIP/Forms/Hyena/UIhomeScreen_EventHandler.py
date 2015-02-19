import sys
from PyQt4 import QtGui, QtCore, Qt
from Forms.ImageAcquisitionModule.UIimageacquisition import *
from Forms.ImageAcquisitionModule.UIimageacquisition_EventHandler import *

HomeFrame = 0
GlobalConfig = GlobalSettings()

class GUI_UIimageacquisition(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.GUI_UIimageacquisition =  Ui_ImageAcquisition()
        self.GUI_UIimageacquisition.setupUi(self)
        self.update()

        UIimageacquisition_LoadEvents(self, GlobalConfig)


def Ui_HomeScreen_LoadEvents(parent):
    '''
    Connect events to controls and define behaviour in UI elements
    '''
    global HomeFrame
    HomeFrame = parent

    '''
    Defiine event
    '''
    def on_BtnImageDAQ_clicked():
        HomeFrame.w = GUI_UIimageacquisition()
        HomeFrame.w.show()

    def on_BtnCreateLoad_clicked():
        ShowFileDialog()

    '''
    Connect controls to events
    '''
    HomeFrame.ui.BtnCreateLoad.clicked.connect(on_BtnCreateLoad_clicked)
    HomeFrame.ui.BtnImageDAQ.clicked.connect(on_BtnImageDAQ_clicked)
    HomeFrame.ui.actionExit.triggered.connect(CloseWindow)

def CloseWindow():
    sys.exit(0)
    
def ShowFileDialog():
    PathDirectory = QtGui.QFileDialog.getExistingDirectory(HomeFrame, 'Select directory', '/home')
    HomeFrame.ui.TextEditDirectoryPath.clear()
    HomeFrame.ui.TextEditDirectoryPath.insert(PathDirectory)

    global GlobalConfig
    GlobalConfig.PathDirectory = PathDirectory

