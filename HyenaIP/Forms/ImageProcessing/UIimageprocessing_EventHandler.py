import sys, os, cv2, numpy as np, shutil, uuid

from PyQt4 import QtGui, QtCore, Qt

from Classes.GlobalSettings import *
from Classes.VideoHandler import *

HomeFrame = 0
GlobalConfig = GlobalSettings()
ImageProcessingFrame = 0

def UIimageProcessing_LoadEvents(parent, Config):
    '''
    Connect events to controls and define behaviour in UI elements
    '''
    global HomeFrame
    HomeFrame = parent

    global GlobalConfig
    GlobalConfig = Config

    global ImageProcessingFrame
    ImageProcessingFrame = HomeFrame.GUI_Ui_ImageProcessing

    ImageProcessingFrame.actionClose_Module.triggered.connect(CloseWindow)
    ImageProcessingFrame.Btn_PreviewFilters.clicked.connect(PreviewSelectedFilters)
    LoadInitialMethods()

def LoadInitialMethods():
    Dir = GlobalConfig.PathDirectory
    selectedItems= GetItemsSelected()
    ImageProcessingFrame.ListPackages.clear()

    dirs = [d for d in os.listdir(str(Dir)) if os.path.isdir(os.path.join(str(Dir), d))]

    for name in dirs:
        Directory = str(Dir) + str("\\") + str(name)
        num_files = sum(os.path.isfile(os.path.join(Directory, f)) for f in os.listdir(Directory))
        NameItem = str(name) + " - (" + str(num_files) + ")"
        ImageProcessingFrame.ListPackages.addItem(QtGui.QListWidgetItem(NameItem))

    for i in selectedItems:
        ImageProcessingFrame.ListPackages.item(i).setSelected(True)

def CloseWindow():
    sys.exit(0)

def GetItemsSelected():
    items = ImageProcessingFrame.ListPackages.count()
    selectedItems=[]
    rangedList =range(items)
    rangedList.reverse()
    for i in rangedList:
        if ImageProcessingFrame.ListPackages.isItemSelected(ImageProcessingFrame.ListPackages.item(i))==True:
            selectedItems.append(i)
    return selectedItems

def PreviewSelectedFilters():
    print "PreviewSelectedFilters"

    img = GetPreviewImage()
    img = ColorShape_Resize(img)
    img = ColorShape_ChangeColor(img)
    img = Thresholding_Images(img)
    img = CannyEdges_Images(img)

def GetPreviewImage():
    img = 0
    Package = ""

    ItemsSelected = GetItemsSelected()
    for i in ItemsSelected:
        Package = str( ImageProcessingFrame.ListPackages.item(i).text() )            
    
    if(Package != ""):
        #Find the first file in packages
        Dir = GlobalConfig.PathDirectory + "\\" + Package.split(" - (")[0]

        Files = [d for d in os.listdir(str(Dir)) if not os.path.isdir(os.path.join(str(Dir), d))]

        FirstFile = ""
        for f in Files:
            if os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg', '.png', '.bmp'):
                FirstFile = str( Dir + "\\" + f )
                break

        #Load Original Image
        try:
            OriginalImage_CV2 = cv2.imread(FirstFile)
            OriginalImage_QPixmap = QtGui.QPixmap(FirstFile)

            ImageProcessingFrame.Lb_ImageOriginal.setPixmap(QtGui.QPixmap(OriginalImage_QPixmap))
            ImageProcessingFrame.Lb_ImageOriginal.setScaledContents(True)
        except:
            e = sys.exc_info() 

        #Apply filters
        FilteredImage = OriginalImage_CV2
        FilteredImage = ColorShape_Resize(FilteredImage)
        FilteredImage = ColorShape_ChangeColor(FilteredImage)
        FilteredImage = Thresholding_Images(FilteredImage)
        FilteredImage = CannyEdges_Images(FilteredImage)

        #Plot Final image
        height, width, byteValue = OriginalImage_CV2.shape
        byteValue = byteValue * width
        cv2.cvtColor(OriginalImage_CV2, cv2.COLOR_BGR2RGB, OriginalImage_CV2 )

        QImage = QtGui.QImage(OriginalImage_CV2, width, height, byteValue, QtGui.QImage.Format_RGB888)
        FilteredImage_QPixmap = QtGui.QPixmap.fromImage(QImage)

        ImageProcessingFrame.Lb_ImageFiltered.setPixmap(FilteredImage_QPixmap)
        ImageProcessingFrame.Lb_ImageFiltered.setScaledContents(True)
    else:
        img = 0
    return img

def ColorShape_Resize(img):
    return img

def ColorShape_ChangeColor(img):
    return img

def Thresholding_Images(img):
    return img

def CannyEdges_Images(img):
    return img