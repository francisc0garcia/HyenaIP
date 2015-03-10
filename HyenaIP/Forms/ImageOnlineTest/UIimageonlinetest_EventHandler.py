import sys, os, cv2, numpy as np, shutil, uuid, pickle

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
from Classes.Utils import *
from Classes.ErrorHandler import *

HomeFrame = 0
GlobalConfig = GlobalSettings()
ImageOnlineTest = 0

IsCameraRecorded = False
CameraFrameActual = {}

model = {}
ClassesModel = {}

def loadMatPlotLib():
    '''
    Load matplotlib objects into the widget
    '''
    try:
        #detectedFace  Image
        ImageOnlineTest.fig_detectedFace = Figure((7.5, 8), dpi=50)
        ImageOnlineTest.canvas_detectedFace = FigureCanvas(ImageOnlineTest.fig_detectedFace)
        ImageOnlineTest.canvas_detectedFace.setParent(ImageOnlineTest.Lb_detectedFace)
        ImageOnlineTest.canvas_detectedFace.setFocus()

        ImageOnlineTest.mpl_toolbar_detectedFace = NavigationToolbar(ImageOnlineTest.canvas_detectedFace, ImageOnlineTest.Lb_detectedFace)

        ImageOnlineTest.fig_detectedFace.clear()
        ImageOnlineTest.axes_detectedFace = ImageOnlineTest.fig_detectedFace.add_subplot(111)
        ImageOnlineTest.axes_detectedFace.plot(ImageOnlineTest.Lb_detectedFace.x(), ImageOnlineTest.Lb_detectedFace.y(), 'ro')
        ImageOnlineTest.canvas_detectedFace.draw()
    except:
        showErrorMessage("Error in loadMatPlotLib()", sys.exc_info() );

def ShowLic():
    '''
    Show license information
    '''
    ShowLicense();

def CloseWindow():
    sys.exit(0);

def UIimageOnlineTest_LoadEvents(parent, Config):
    '''
    Load initial variables for the module
    '''
    try:
        global HomeFrame
        HomeFrame = parent

        global GlobalConfig
        GlobalConfig = Config

        global ImageOnlineTest
        ImageOnlineTest = HomeFrame.GUI_Ui_ImageOnlineTest
        ImageOnlineTest.video = False

        ImageOnlineTest.Btn_Start.clicked.connect(Turn_Camera)
        ImageOnlineTest.actionClose_Module.triggered.connect(CloseWindow)
        ImageOnlineTest.actionLicense.triggered.connect(ShowLic)
    
        PathDir = str(GlobalConfig.PathDirectory)

        # load model previously saved in training module (format .model)
        global model
        Files = [d for d in os.listdir(str(PathDir)) if not os.path.isdir(os.path.join(str(PathDir), d))]
        ModelDetected = False

        FileModel = ""
        for f in Files:
            if os.path.splitext(f)[1].lower() in ('.model'):
                if( "FisherFaceRecognizer" in f ):
                    model = cv2.createFisherFaceRecognizer()
                    FileModel = f
                    ModelDetected = True
                if( "LBPHFaceRecognizer" in f ):
                    model = cv2.createLBPHFaceRecognizer()
                    FileModel = f
                    ModelDetected = True
                if( "EigenFaceRecognizer" in f ):
                    model = cv2.createEigenFaceRecognizer()
                    FileModel = f
                    ModelDetected = True
            
        if(ModelDetected):
            modelPath = PathDir + "\\" + FileModel
            model.load(modelPath)
        
            global ClassesModel
            ClassesModelFile = PathDir + "\\ClassesModel.p"
            if(os.path.isfile(ClassesModelFile)) :
                ClassesModel = pickle.load( open( ClassesModelFile, "rb" ) )

        loadMatPlotLib()

    except:
        showErrorMessage("Error in UIimageOnlineTest_LoadEvents() Verify the directory path selected! ", sys.exc_info() );

def Turn_Camera():
    '''
    Handle for camera actions
    '''
    try:
        if(IsCameraRecorded):
            StopVideo()
        else:
            ConnectDevice()
    except:
        showErrorMessage("Error in Turn_Camera()", sys.exc_info() );

def ConnectDevice():
    '''
    Use OpenCV for connect to camera device
    '''
    try:
        if not (ImageOnlineTest.video):
            ImageOnlineTest.video = VideoHandler()
        ImageOnlineTest._timer = QtCore.QTimer(HomeFrame)
        ImageOnlineTest._timer.timeout.connect(play)
        ImageOnlineTest._timer.start(5)
    except:
        showErrorMessage("Error in ConnectDevice()", sys.exc_info() );

def play():
    '''
    Event for recover images from the Camera
    '''
    try:
        ImageOnlineTest.video.captureNextFrame()

        global CameraFrameActual
        CameraFrameActual = ImageOnlineTest.video.currentFrame
        
        CropImage = False
        [ImageOnlineTest.video.currentFrame, CropImage, IsDetected] = detect(CameraFrameActual, cascade_fn="Media\haarcascades\haarcascade_frontalface_alt2.xml")

        #cv2.cvtColor(OriginalImage_CV2, cv2.COLOR_BGR2RGB, OriginalImage_CV2 )

        if(IsDetected):
            ImageOnlineTest.axes_detectedFace.imshow(CropImage)
            ImageOnlineTest.canvas_detectedFace.draw()

            [Y_pred, Y_conf] = PredictFace(CropImage)
            #ImageOnlineTest.Pt_Results.clear()
            ClassName = str(ClassesModel[Y_pred])
            #testDes = "Class: " + ClassName +  " Number: " +  str(Y_pred) + " Confidence level: " +  str(Y_conf)
            #ImageOnlineTest.Pt_Results.appendPlainText(testDes)
            LabText = ClassName
            ImageOnlineTest.LbPredictedFace.setText(ClassName);

        ImageOnlineTest.Lb_cameraInput.setPixmap(ImageOnlineTest.video.convertFrame())
        ImageOnlineTest.Lb_cameraInput.setScaledContents(True)

        global IsCameraRecorded
        IsCameraRecorded = True
        ImageOnlineTest.Btn_Start.setText("Turn OFF camera");
    except TypeError:
        print "No frame: " + str(sys.exc_info()[1])

def StopVideo():
    try:
        ImageOnlineTest._timer.stop()
        ImageOnlineTest.video.StopVideo()
        global IsCameraRecorded
        IsCameraRecorded = False
        ImageOnlineTest.Btn_Start.setText("Turn ON camera");
    except:
        showErrorMessage("Error in StopVideo()", sys.exc_info() );

def PredictFace(img):
    '''
    Predict a face which was founded in the image img
    '''
    img = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY)
    global model
    img = cv2.resize(img, (200, 200))
    [Y_pred_temp, Y_confidence_temp] = model.predict(np.asarray(img, dtype=np.uint8))

    return Y_pred_temp, Y_confidence_temp