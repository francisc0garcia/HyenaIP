import sys
from PyQt4 import QtGui, QtCore, Qt

from Forms.ImageAcquisitionModule.UIimageacquisition import *
from Forms.ImageAcquisitionModule.UIimageacquisition_EventHandler import *

from Forms.ImageProcessing.UIimageprocessing import *
from Forms.ImageProcessing.UIimageprocessing_EventHandler import *

from Forms.ImageTraining.UIimagetraining import *
from Forms.ImageTraining.UIimagetraining_EventHandler import *

from Forms.ImageOnlineTest.UIimageonlinetest import *
from Forms.ImageOnlineTest.UIimageonlinetest_EventHandler import *

from Classes.ErrorHandler import *
from Classes.Utils import *

HomeFrame = 0
GlobalConfig = GlobalSettings()

class GUI_Ui_ImageAcquisition(QtGui.QMainWindow):
    '''
    Define an interface for load module: Ui_ImageAcquisition module
    '''
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.GUI_Ui_ImageAcquisition =  Ui_ImageAcquisition()
        self.GUI_Ui_ImageAcquisition.setupUi(self)
        self.update()

        UIimageacquisition_LoadEvents(self, GlobalConfig)

class GUI_Ui_ImageProcessing(QtGui.QMainWindow):
    '''
    Define an interface for load module: Ui_ImageProcessing 
    '''
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.GUI_Ui_ImageProcessing =  Ui_ImageProcessing()
        self.GUI_Ui_ImageProcessing.setupUi(self)
        self.update()

        UIimageProcessing_LoadEvents(self, GlobalConfig)

class GUI_Ui_ImageTraining(QtGui.QMainWindow):
    '''
    Define an interface for load module: Ui_ImageTraining 
    '''
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.GUI_Ui_ImageTraining =  Ui_ImageTraining()
        self.GUI_Ui_ImageTraining.setupUi(self)
        self.update()

        UIimageTraining_LoadEvents(self, GlobalConfig)

class GUI_Ui_ImageOnlineTest(QtGui.QMainWindow):
    '''
    Define an interface for load module: Ui_ImageOnlineTest 
    '''
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.GUI_Ui_ImageOnlineTest =  Ui_ImageOnlineTest()
        self.GUI_Ui_ImageOnlineTest.setupUi(self)
        self.update()

        UIimageOnlineTest_LoadEvents(self, GlobalConfig)
        
def Ui_HomeScreen_LoadEvents(parent):
    '''
    Connect events to controls and define behaviour in UI elements
    '''
    try:
        global HomeFrame
        HomeFrame = parent

        '''
        Defiine event
        '''
        def on_BtnImageDAQ_clicked():
            HomeFrame.w = GUI_Ui_ImageAcquisition()
            HomeFrame.w.show()

        def on_BtnImageProcessing_Clicked():
            HomeFrame.IP = GUI_Ui_ImageProcessing()
            HomeFrame.IP.show()

        def on_BtnTraining_clicked():
            HomeFrame.IT = GUI_Ui_ImageTraining()
            HomeFrame.IT.show()

        def on_BtnTestError_clicked():
            HomeFrame.IOT = GUI_Ui_ImageOnlineTest()
            HomeFrame.IOT.show()

        def on_BtnCreateLoad_clicked():
            ShowFileDialog()

        '''
        Connect controls to events
        '''
        HomeFrame.ui.BtnCreateLoad.clicked.connect(on_BtnCreateLoad_clicked)
        HomeFrame.ui.BtnImageDAQ.clicked.connect(on_BtnImageDAQ_clicked)
        HomeFrame.ui.BtnImageProcessing.clicked.connect(on_BtnImageProcessing_Clicked)
        HomeFrame.ui.BtnTraining.clicked.connect(on_BtnTraining_clicked)
        HomeFrame.ui.BtnTestError.clicked.connect(on_BtnTestError_clicked)
        HomeFrame.ui.actionExit.triggered.connect(CloseWindow)
        HomeFrame.ui.actionLicense.triggered.connect(ShowLic)

        HomeFrame.ui.BtnExportToQuickCOG.clicked.connect(Export_QuickCOG)
    except:
        showErrorMessage("Error in Ui_HomeScreen_LoadEvents", sys.exc_info() );

def ShowLic():
    '''
    Show license information
    '''
    ShowLicense();

def CloseWindow():
    '''
    Close application
    '''
    sys.exit(0)
      
def ShowFileDialog():
    '''
    Allows select the path for the main directory of the project.
    In this directory will be save all settings and future results
    '''
    try:
        PathDirectory = QtGui.QFileDialog.getExistingDirectory(HomeFrame, 'Select directory', '/home')

        if(PathDirectory != ""):
            HomeFrame.ui.TextEditDirectoryPath.clear()
            HomeFrame.ui.TextEditDirectoryPath.insert(PathDirectory)

            global GlobalConfig
            GlobalConfig.PathDirectory = PathDirectory
    except:
        showErrorMessage("Error in Method ShowFileDialog()", sys.exc_info() );

def Export_QuickCOG():
    Dir = GlobalConfig.PathDirectory
    ExportProjectToQuickCog(str(Dir))