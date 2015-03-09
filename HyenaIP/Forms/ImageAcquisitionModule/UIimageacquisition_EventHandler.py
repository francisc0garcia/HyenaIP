import sys, os, cv2, numpy as np, shutil, uuid

from PyQt4 import QtGui, QtCore, Qt

from Classes.GlobalSettings import *
from Classes.VideoHandler import *
from Classes.ErrorHandler import *

HomeFrame = 0
GlobalConfig = GlobalSettings()
ImageAcquisitionFrame = 0
IsCameraRecorded = False

CameraFrameActual = {}

def UIimageacquisition_LoadEvents(parent, Config):
    '''
    Connect events to controls and define behaviour in UI elements
    '''

    try:
        global HomeFrame
        HomeFrame = parent

        global GlobalConfig
        GlobalConfig = Config

        global ImageAcquisitionFrame
        ImageAcquisitionFrame = HomeFrame.GUI_Ui_ImageAcquisition
        ImageAcquisitionFrame.video = False

        ImageAcquisitionFrame.actionClose_Module.triggered.connect(CloseWindow)
        ImageAcquisitionFrame.BtnSelectImages.clicked.connect(SelectExistingFile)
        ImageAcquisitionFrame.BtnConnectDevice.clicked.connect(Turn_Camera)
        ImageAcquisitionFrame.BtnAddNewPackage.clicked.connect(CreateNewPackage)
        ImageAcquisitionFrame.BtnRemovePackage.clicked.connect(RemovePackageSelected)
        ImageAcquisitionFrame.BtnTakePhoto.clicked.connect(TakePhoto)
        LoadInitialMethods()
    except:
        showErrorMessage("Error in UIimageacquisition_LoadEvents()", sys.exc_info() );

def LoadInitialMethods():
    '''
    Load List of folders from GlobalConfig.PathDirectory
    '''
    try:
        Dir = GlobalConfig.PathDirectory
        selectedItems= GetItemsSelected()
        ImageAcquisitionFrame.ListPackages.clear()

        dirs = [d for d in os.listdir(str(Dir)) if os.path.isdir(os.path.join(str(Dir), d))]

        for name in dirs:
            Directory = str(Dir) + str("\\") + str(name)
            num_files = sum(os.path.isfile(os.path.join(Directory, f)) for f in os.listdir(Directory))
            NameItem = str(name) + " - (" + str(num_files) + ")"
            ImageAcquisitionFrame.ListPackages.addItem(QtGui.QListWidgetItem(NameItem))

        for i in selectedItems:
            ImageAcquisitionFrame.ListPackages.item(i).setSelected(True)
    except:
        showErrorMessage("Error in LoadInitialMethods() Verify the directory path selected! ", sys.exc_info() );

def CloseWindow():
    try:
        sys.exit(0)
    except:
        showErrorMessage("Error in CloseWindow()", sys.exc_info() );
        raise

def GetItemsSelected():
    selectedItems=[]

    try:
        items = ImageAcquisitionFrame.ListPackages.count()
        rangedList =range(items)
        rangedList.reverse()
        for i in rangedList:
            if ImageAcquisitionFrame.ListPackages.isItemSelected(ImageAcquisitionFrame.ListPackages.item(i))==True:
                selectedItems.append(i)
    except:
        showErrorMessage("Error in GetItemsSelected()", sys.exc_info() );
        
    return selectedItems

def SelectExistingFile():
    try:
        Dir = GlobalConfig.PathDirectory

        items = ImageAcquisitionFrame.ListPackages.count()
        selectedItems= GetItemsSelected()

        files = QtGui.QFileDialog.getOpenFileNames(
                HomeFrame, 'Open File', '', 'Images (*.png *.bmp *.jpg)')

        for i in selectedItems:
            Directory = Dir + str("\\") + str(ImageAcquisitionFrame.ListPackages.item(i).text()) + str("\\")
        
            for OriginalPath in files:
                OriginalName, fileExtension = os.path.splitext(str(OriginalPath))
                NewName = str(Directory.split(" - (")[0]) + str("\\") + str(uuid.uuid4()).split('-')[0] + fileExtension 
                if not os.path.isfile(NewName) :
                    shutil.copy2(OriginalPath, NewName)
        LoadInitialMethods()
    except:
        showErrorMessage("Error in SelectExistingFile()", sys.exc_info() );

def Turn_Camera():
    try:
        if(IsCameraRecorded):
            StopVideo()
        else:
            ConnectDevice()
    except:
        showErrorMessage("Error in Turn_Camera()", sys.exc_info() );

def ConnectDevice():
    try:
        if not (ImageAcquisitionFrame.video):
            ImageAcquisitionFrame.video = VideoHandler()
        ImageAcquisitionFrame._timer = QtCore.QTimer(HomeFrame)
        ImageAcquisitionFrame._timer.timeout.connect(play)
        ImageAcquisitionFrame._timer.start(27)
    except:
        showErrorMessage("Error in ConnectDevice()", sys.exc_info() );

def play():
    try:
        ImageAcquisitionFrame.video.captureNextFrame()
        global CameraFrameActual
        CameraFrameActual = ImageAcquisitionFrame.video.convertFrame()
        ImageAcquisitionFrame.LabelImage.setPixmap(CameraFrameActual)
        ImageAcquisitionFrame.LabelImage.setScaledContents(True)

        global IsCameraRecorded
        IsCameraRecorded = True
        ImageAcquisitionFrame.BtnConnectDevice.setText("Turn OFF camera");
    except TypeError:
        print "No frame"

def StopVideo():
    try:
        ImageAcquisitionFrame._timer.stop()
        ImageAcquisitionFrame.video.StopVideo()
        global IsCameraRecorded
        IsCameraRecorded = False
        ImageAcquisitionFrame.BtnConnectDevice.setText("Turn ON camera");
    except:
        showErrorMessage("Error in ConnectDevice()", sys.exc_info() );

def CreateNewPackage():
    try:
        Dir = GlobalConfig.PathDirectory
        Name = ImageAcquisitionFrame.LineNameNewPackage.text()
        NewDirectory = Dir + str("\\") + Name
        if not os.path.exists( NewDirectory ):
            os.makedirs(str(NewDirectory))
            ImageAcquisitionFrame.LineNameNewPackage.clear()
        LoadInitialMethods()
    except:
        showErrorMessage("Error in CreateNewPackage()", sys.exc_info() );

def RemovePackageSelected():
    try:
        Dir = GlobalConfig.PathDirectory
        selectedItems= GetItemsSelected()
        for i in selectedItems:
            name = ImageAcquisitionFrame.ListPackages.item(i).text()
            NewDirectory = str(Dir) + str("\\") + name.split(" - (")[0]
            if os.path.exists( NewDirectory ):
                shutil.rmtree(str(NewDirectory))
        LoadInitialMethods()
    except:
        showErrorMessage("Error in RemovePackageSelected()", sys.exc_info() );

def TakePhoto():
    try:
        Dir = GlobalConfig.PathDirectory
        Ext = ".jpg"
        Name = str(uuid.uuid4()).split('-')[0]
    
        selectedItems= GetItemsSelected()

        for i in selectedItems:
            SubDir = ImageAcquisitionFrame.ListPackages.item(i).text().split(" - (")[0]
            NewName = Dir + "\\" +  str(SubDir)+ "\\" + Name + Ext
            if not os.path.isfile(NewName) :
                CameraFrameActual.save(NewName)    
        LoadInitialMethods()
    except:
        showErrorMessage("Error in TakePhoto()", sys.exc_info() );