import sys, os, cv2, numpy as np, shutil, uuid
from matplotlib.image import imsave as imsave
from matplotlib import image as image
import matplotlib.pyplot as plt
from matplotlib.backends import qt_compat
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if use_pyside:
    from PySide.QtCore import *
    from PySide.QtGui import *
else:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

from PyQt4 import QtGui, QtCore, Qt

from Classes.GlobalSettings import *
from Classes.VideoHandler import *
from Classes.ErrorHandler import *
from Classes.Utils import *

HomeFrame = 0
GlobalConfig = GlobalSettings()
ImageProcessingFrame = 0

def LoadMatPlotLib_canvas():
    '''
    Load matplotlib objects into the widget
    '''
    try:
        #Original Image
        ImageProcessingFrame.fig_Original = Figure((11.0, 9.0), dpi=50)
        ImageProcessingFrame.canvas_Original = FigureCanvas(ImageProcessingFrame.fig_Original)
        ImageProcessingFrame.canvas_Original.setParent(ImageProcessingFrame.Lb_ImageOriginal)
        ImageProcessingFrame.canvas_Original.setFocus()

        ImageProcessingFrame.mpl_toolbar_Original = NavigationToolbar(ImageProcessingFrame.canvas_Original, ImageProcessingFrame.Lb_ImageOriginal)

        ImageProcessingFrame.fig_Original.clear()
        ImageProcessingFrame.axes_Original = ImageProcessingFrame.fig_Original.add_subplot(111)
        ImageProcessingFrame.axes_Original.plot(ImageProcessingFrame.Lb_ImageOriginal.x(), ImageProcessingFrame.Lb_ImageOriginal.y(), 'ro')
        ImageProcessingFrame.canvas_Original.draw()

        #Filtered Image
        ImageProcessingFrame.fig_Filtered = Figure((11.0, 9.0), dpi=50)
        ImageProcessingFrame.canvas_Filtered = FigureCanvas(ImageProcessingFrame.fig_Filtered)
        ImageProcessingFrame.canvas_Filtered.setParent(ImageProcessingFrame.Lb_ImageFiltered)
        ImageProcessingFrame.canvas_Filtered.setFocus()

        ImageProcessingFrame.mpl_toolbar_Filtered = NavigationToolbar(ImageProcessingFrame.canvas_Filtered, ImageProcessingFrame.Lb_ImageFiltered)

        ImageProcessingFrame.fig_Filtered.clear()
        ImageProcessingFrame.axes_Filtered = ImageProcessingFrame.fig_Filtered.add_subplot(111)
        ImageProcessingFrame.axes_Filtered.plot(ImageProcessingFrame.Lb_ImageFiltered.x(), ImageProcessingFrame.Lb_ImageFiltered.y(), 'ro')
        ImageProcessingFrame.canvas_Filtered.draw()
    except:
        showErrorMessage("Error in LoadMatPlotLib_canvas()", sys.exc_info() );

def UIimageProcessing_LoadEvents(parent, Config):
    '''
    Connect events to controls and define behaviour in UI elements
    '''
    try:
        global HomeFrame
        HomeFrame = parent

        global GlobalConfig
        GlobalConfig = Config

        global ImageProcessingFrame
        ImageProcessingFrame = HomeFrame.GUI_Ui_ImageProcessing

        ImageProcessingFrame.actionClose_Module.triggered.connect(CloseWindow)
        ImageProcessingFrame.actionLicense.triggered.connect(ShowLic)
        ImageProcessingFrame.BtnRunAndAddNewPackage.clicked.connect(ProcessNewPackage)

        ImageProcessingFrame.ListPackages.itemSelectionChanged.connect(UpdatePreview)
        ImageProcessingFrame.Cb_EnableColorShape.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_Laplacian.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_Smooth.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_Sobel_X.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_Sobel_Y.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_Erosion.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_Dilation.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_MorphologicalGradient.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_EnableThresholding.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_BINARY.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_BINARY_INV.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_TRUNC.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_TOZERO.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_TOZERO_INV.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_ADAP_MEAN.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_ADAP_GAUSSIAN.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_OTSU.clicked.connect(UpdatePreview)
        ImageProcessingFrame.Cb_EnableCannyEdges.clicked.connect(UpdatePreview)
    
        ImageProcessingFrame.Sl_Smooth.sliderReleased.connect(UpdatePreview)
        ImageProcessingFrame.Sl_Sobel_X.sliderReleased.connect(UpdatePreview)
        ImageProcessingFrame.Sl_Sobel_Y.sliderReleased.connect(UpdatePreview)
        ImageProcessingFrame.Sl_Erosion.sliderReleased.connect(UpdatePreview)
        ImageProcessingFrame.Sl_Dilation.sliderReleased.connect(UpdatePreview)
        ImageProcessingFrame.Sl_MorphologicalGradient.sliderReleased.connect(UpdatePreview)
        ImageProcessingFrame.Hs_LevelThreshold.sliderReleased.connect(UpdatePreview)
        ImageProcessingFrame.Hs_CannyThreshold.sliderReleased.connect(UpdatePreview)
        ImageProcessingFrame.Hs_CannyLinks.sliderReleased.connect(UpdatePreview)

        LoadMatPlotLib_canvas()
        LoadInitialMethods()
        ImageProcessingFrame.ListPackages.item(0).setSelected(True)
    except:
        showErrorMessage("Error in UIimageProcessing_LoadEvents()", sys.exc_info() );

def ShowLic():
    '''
    Show license information
    '''
    ShowLicense();

def UpdatePreview():
    GetPreviewImage()

def LoadInitialMethods():
    '''
    Load intial variables for the module
    '''
    try:
        Dir = GlobalConfig.PathDirectory
        selectedItems= GetItemsSelected(ImageProcessingFrame.ListPackages)
        ImageProcessingFrame.ListPackages.clear()

        dirs = [d for d in os.listdir(str(Dir)) if os.path.isdir(os.path.join(str(Dir), d))]

        for name in dirs:
            Directory = str(Dir) + str("\\") + str(name)
            num_files = sum(os.path.isfile(os.path.join(Directory, f)) for f in os.listdir(Directory))
            NameItem = str(name) + " - (" + str(num_files) + ")"
            ImageProcessingFrame.ListPackages.addItem(QtGui.QListWidgetItem(NameItem))

        for i in selectedItems:
            ImageProcessingFrame.ListPackages.item(i).setSelected(True)
    except:
        showErrorMessage("Error in LoadInitialMethods() Verify the directory path selected! ", sys.exc_info() );

def CloseWindow():
    sys.exit(0)

def PreviewSelectedFilters():
    GetPreviewImage()

def GetPreviewImage():
    '''
    Refresh the preview image, based on the filters selected
    '''
    img = 0
    Package = ""

    try:
        ItemsSelected = GetItemsSelected(ImageProcessingFrame.ListPackages)
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
            OriginalImage_CV2 = cv2.imread(FirstFile)
            cv2.cvtColor(OriginalImage_CV2, cv2.COLOR_BGR2RGB, OriginalImage_CV2 )

            ImageProcessingFrame.axes_Original.imshow(OriginalImage_CV2)
            ImageProcessingFrame.canvas_Original.draw()

            OriginalImage_CV2 = cv2.cvtColor(OriginalImage_CV2, cv2.COLOR_BGR2GRAY)
 
            #Apply filters
            FilteredImage = OriginalImage_CV2
            FilteredImage = ColorShape_Resize(FilteredImage)
            FilteredImage = ColorShape_ChangeColor(FilteredImage)
            FilteredImage = Thresholding_Images(FilteredImage)
            FilteredImage = CannyEdges_Images(FilteredImage)

            #Plot filtered image
            ImageProcessingFrame.axes_Filtered.imshow(FilteredImage, cmap = 'gray')
            ImageProcessingFrame.canvas_Filtered.draw()
        else:
            img = 0
    except:
        showErrorMessage("Error in GetPreviewImage()", sys.exc_info() );

    return img

def ColorShape_Resize(img):
    '''
    Resize images if the user specified a new size
    '''
    try:
        if(ImageProcessingFrame.Cb_EnableColorShape.isChecked() ):
            Width = ImageProcessingFrame.Sb_Height.value()
            Height = ImageProcessingFrame.Sb_Height.value()

            if( Width > 0 and Height > 0):
                img = cv2.resize(img,(Width, Height), interpolation = cv2.INTER_CUBIC)
                #img = img.resize((Width,Height), image.NEAREST)
                #img = np.asarray(TempImg)
    except:
        showErrorMessage("Error in ColorShape_Resize()", sys.exc_info() );
    return img

def ColorShape_ChangeColor(img):
    '''
    Apply color filters in the image
    '''
    try:
        if(ImageProcessingFrame.Cb_EnableColorShape.isChecked() ):

            Laplacian = ImageProcessingFrame.Cb_Laplacian.isChecked()
            Smooth = ImageProcessingFrame.Cb_Smooth.isChecked()
            Sobel_X = ImageProcessingFrame.Cb_Sobel_X.isChecked()
            Sobel_Y = ImageProcessingFrame.Cb_Sobel_Y.isChecked()
            Erosion = ImageProcessingFrame.Cb_Erosion.isChecked()
            Dilation = ImageProcessingFrame.Cb_Dilation.isChecked()
            MorphologicalGradient = ImageProcessingFrame.Cb_MorphologicalGradient.isChecked()

            Sl_Smooth = ImageProcessingFrame.Sl_Smooth.value()
            Sl_Sobel_X = ImageProcessingFrame.Sl_Sobel_X.value()
            Sl_Sobel_Y = ImageProcessingFrame.Sl_Sobel_Y.value()
            Sl_Erosion = ImageProcessingFrame.Sl_Erosion.value()
            Sl_Dilation = ImageProcessingFrame.Sl_Dilation.value()
            Sl_MorphologicalGradient = ImageProcessingFrame.Sl_MorphologicalGradient.value()

            if(Laplacian):
                img = cv2.Laplacian(img, cv2.CV_64F)
            if(Smooth):
                img = cv2.blur(img, (Sl_Smooth,Sl_Smooth) ) 
            if(Sobel_X):
                if(Sl_Sobel_X % 2 == 0):
                    Sl_Sobel_X = Sl_Sobel_X -1
                img = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=Sl_Sobel_X)
            if(Sobel_Y):
                if(Sl_Sobel_Y % 2 == 0):
                    Sl_Sobel_Y = Sl_Sobel_Y -1
                img = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=Sl_Sobel_Y)
            if(Erosion):
                kernel = np.ones((Sl_Erosion, Sl_Erosion),np.uint8)
                img = cv2.erode(img, kernel, iterations = Sl_Erosion)
            if(Dilation):
                kernel = np.ones((Sl_Dilation, Sl_Dilation),np.uint8)
                img = cv2.dilate(img, kernel, iterations = 1)
            if(MorphologicalGradient):
                kernel = np.ones((Sl_MorphologicalGradient,Sl_MorphologicalGradient),np.uint8)
                img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    except:
        showErrorMessage("Error in ColorShape_ChangeColor()", sys.exc_info() );
    return img

def Thresholding_Images(img):
    '''
    Apply Thresholding filters over the images
    '''
    try:
        if(ImageProcessingFrame.Cb_EnableThresholding.isChecked()):
            Hs_LevelThreshold = ImageProcessingFrame.Hs_LevelThreshold.value()

            Cb_BINARY = ImageProcessingFrame.Cb_BINARY.isChecked()
            Cb_BINARY_INV = ImageProcessingFrame.Cb_BINARY_INV.isChecked()
            Cb_TRUNC = ImageProcessingFrame.Cb_TRUNC.isChecked()
            Cb_TOZERO = ImageProcessingFrame.Cb_TOZERO.isChecked()
            Cb_TOZERO_INV = ImageProcessingFrame.Cb_TOZERO_INV.isChecked()
            Cb_ADAP_MEAN = ImageProcessingFrame.Cb_ADAP_MEAN.isChecked()
            Cb_ADAP_GAUSSIAN = ImageProcessingFrame.Cb_ADAP_GAUSSIAN.isChecked()
            Cb_OTSU = ImageProcessingFrame.Cb_OTSU.isChecked()

            img = img.astype(np.uint8)

            if(Cb_BINARY):
                ret, img = cv2.threshold(img, Hs_LevelThreshold, 255,cv2.THRESH_BINARY)
            if(Cb_BINARY_INV):
                ret,img = cv2.threshold(img, Hs_LevelThreshold, 255,cv2.THRESH_BINARY_INV)
            if(Cb_TRUNC):
                ret,img = cv2.threshold(img, Hs_LevelThreshold, 255,cv2.THRESH_TRUNC)
            if(Cb_TOZERO):
                ret,img = cv2.threshold(img, Hs_LevelThreshold, 255,cv2.THRESH_TOZERO)
            if(Cb_TOZERO_INV):
                ret,img = cv2.threshold(img, Hs_LevelThreshold, 255,cv2.THRESH_TOZERO_INV)
            if(Cb_ADAP_MEAN):
                img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
            if(Cb_ADAP_GAUSSIAN):
                img = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
            if(Cb_OTSU):
                ret2,img = cv2.threshold(img,Hs_LevelThreshold,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    except:
        showErrorMessage("Error in Thresholding_Images()", sys.exc_info() );
    return img

def CannyEdges_Images(img):
    '''
    Apply canny edge detector over the images
    '''
    try:
        if(ImageProcessingFrame.Cb_EnableCannyEdges.isChecked()):
            Hs_CannyThreshold = ImageProcessingFrame.Hs_CannyThreshold.value()
            Hs_CannyLinks = ImageProcessingFrame.Hs_CannyLinks.value()

            img = cv2.Canny(img,Hs_CannyThreshold,Hs_CannyLinks)
    except:
        showErrorMessage("Error in CannyEdges_Images()", sys.exc_info() );
    return img

def ProcessNewPackage():
    '''
    Create a new package (folder) with the procesed images:
    Apply filters over the original images and save the results into a new folder
    '''
    try:
        img = 0
        Package = ""

        ItemsSelected = GetItemsSelected(ImageProcessingFrame.ListPackages)
        for i in ItemsSelected:
            Package = str( ImageProcessingFrame.ListPackages.item(i).text() )            
    
        if(Package != ""):
            #Find the first file in packages
            Dir = GlobalConfig.PathDirectory + "\\" + Package.split(" - (")[0]
            NameNewPackage = ImageProcessingFrame.LineNameNewPackage.text()
            if(NameNewPackage != ""):
                #Get all image to process
                Files = [d for d in os.listdir(str(Dir)) if not os.path.isdir(os.path.join(str(Dir), d))]

                OriginalDirectory = GlobalConfig.PathDirectory
                DestFolder = OriginalDirectory + "\\" + NameNewPackage 
                #Create folder
                if not os.path.exists( DestFolder ):
                    os.makedirs(str(DestFolder))

                ImageProcessingFrame.progressBar.setMaximum(len(Files))

                FirstFile = ""
                IndexFile = 0
                for f in Files:
                    if os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg', '.png', '.bmp'):
                        FirstFile = str( Dir + "\\" + f )
                    
                        #read Image
                        OriginalImage_CV2 = cv2.imread(FirstFile)
                        OriginalImage_CV2 = cv2.cvtColor(OriginalImage_CV2, cv2.COLOR_BGR2GRAY)
                    
                        #Apply filters
                        FilteredImage = OriginalImage_CV2
                        FilteredImage = ColorShape_Resize(FilteredImage)
                        FilteredImage = ColorShape_ChangeColor(FilteredImage)
                        FilteredImage = Thresholding_Images(FilteredImage)
                        FilteredImage = CannyEdges_Images(FilteredImage)
                    
                        #Save image
                    
                        #get random name
                        NewNameFile = str(uuid.uuid4()).split('-')[0]
                        NewFile = str( DestFolder + '\\' + NewNameFile + '.jpg' )
                        imsave(NewFile, FilteredImage,  cmap='gray')

                        ImageProcessingFrame.progressBar.setValue(IndexFile)
                        IndexFile = IndexFile + 1

                ImageProcessingFrame.progressBar.setValue(0)
                LoadInitialMethods()
        else:
            img = 0
    except:
        showErrorMessage("Error in ProcessNewPackage()", sys.exc_info() );