import sys, os, cv2, numpy as np, shutil, uuid

from matplotlib.image import imsave as imsave
from matplotlib import image as image
import matplotlib.pyplot as plt
from matplotlib.backends import qt4_compat
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

use_pyside = qt4_compat.QT_API == qt4_compat.QT_API_PYSIDE
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

HomeFrame = 0
GlobalConfig = GlobalSettings()
ImageOnlineTest = 0

IsCameraRecorded = False
CameraFrameActual = {}

model = {}

def loadMatPlotLib():
    #detectedFace  Image
    ImageOnlineTest.fig_detectedFace = Figure((7.5, 7), dpi=50)
    ImageOnlineTest.canvas_detectedFace = FigureCanvas(ImageOnlineTest.fig_detectedFace)
    ImageOnlineTest.canvas_detectedFace.setParent(ImageOnlineTest.Lb_detectedFace)
    ImageOnlineTest.canvas_detectedFace.setFocus()

    ImageOnlineTest.mpl_toolbar_detectedFace = NavigationToolbar(ImageOnlineTest.canvas_detectedFace, ImageOnlineTest.Lb_detectedFace)

    ImageOnlineTest.fig_detectedFace.clear()
    ImageOnlineTest.axes_detectedFace = ImageOnlineTest.fig_detectedFace.add_subplot(111)
    ImageOnlineTest.axes_detectedFace.plot(ImageOnlineTest.Lb_detectedFace.x(), ImageOnlineTest.Lb_detectedFace.y(), 'ro')
    ImageOnlineTest.canvas_detectedFace.draw()

def UIimageOnlineTest_LoadEvents(parent, Config):
    print "UIimageOnlineTest_LoadEvents"
    
    global HomeFrame
    HomeFrame = parent

    global GlobalConfig
    GlobalConfig = Config

    global ImageOnlineTest
    ImageOnlineTest = HomeFrame.GUI_Ui_ImageOnlineTest
    ImageOnlineTest.video = False

    ImageOnlineTest.Btn_Start.clicked.connect(Turn_Camera)
    
    PathDir = str(GlobalConfig.PathDirectory)

    global model
    model = cv2.createFisherFaceRecognizer()
    modelPath = "C:\Users\Pach0-PC\Desktop\Test\Model_FisherFaceRecognizer.yml"
    model.load(modelPath)

    loadMatPlotLib()

def Turn_Camera():
    if(IsCameraRecorded):
        StopVideo()
    else:
        ConnectDevice()

def ConnectDevice():
    if not (ImageOnlineTest.video):
        ImageOnlineTest.video = VideoHandler()
    ImageOnlineTest._timer = QtCore.QTimer(HomeFrame)
    ImageOnlineTest._timer.timeout.connect(play)
    ImageOnlineTest._timer.start(27)

def play():
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
            ImageOnlineTest.Pt_Results.clear()
            testDes = "Class prediction: " +  str(Y_pred) + " Confidence level: " +  str(Y_conf)
            ImageOnlineTest.Pt_Results.appendPlainText(testDes)

        ImageOnlineTest.Lb_cameraInput.setPixmap(ImageOnlineTest.video.convertFrame())
        ImageOnlineTest.Lb_cameraInput.setScaledContents(True)

        global IsCameraRecorded
        IsCameraRecorded = True
        ImageOnlineTest.Btn_Start.setText("Turn OFF camera");
    except TypeError:
        print "No frame: " + str(sys.exc_info()[1])

def StopVideo():
    ImageOnlineTest._timer.stop()
    ImageOnlineTest.video.StopVideo()
    global IsCameraRecorded
    IsCameraRecorded = False
    ImageOnlineTest.Btn_Start.setText("Turn ON camera");

def imgCrop(image, cropBox, boxScale=1):
    # Crop a PIL image with the provided box [x(left), y(upper), w(width), h(height)]

    # Calculate scale factors
    xDelta=max(cropBox[2]*(boxScale-1),0)
    yDelta=max(cropBox[3]*(boxScale-1),0)

    # Convert cv box to PIL box [left, upper, right, lower]
    PIL_box=[cropBox[0]-xDelta, cropBox[1]-yDelta, cropBox[0]+cropBox[2]+xDelta, cropBox[1]+cropBox[3]+yDelta]

    Y1 = cropBox[1]+cropBox[3]+yDelta
    Y2 = cropBox[1]-yDelta
    X1 = cropBox[0]+cropBox[2]+xDelta
    X2 = cropBox[0]-xDelta
    return image[Y2:Y1, X2:X1 ]

def detect(img, cascade_fn='haarcascade_frontalface_alt2.xml',
       scaleFactor=1.3, minNeighbors=4, minSize=(20, 20),
       flags=cv2.cv.CV_HAAR_SCALE_IMAGE):
    
    face_cascade = cv2.CascadeClassifier(cascade_fn)
    gray = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, 
                                          minSize=minSize, flags=flags)

    boxScale = 1
    croppedImage = {}
    faceTemp = {}
    IsDetected = False

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        faceTemp[0] = x
        faceTemp[1] = y
        faceTemp[2] = w
        faceTemp[3] = h
        croppedImage=imgCrop(img, faceTemp, boxScale=boxScale)
        IsDetected = True

    OriginalImage = img
    CutImage = croppedImage

    return OriginalImage, CutImage, IsDetected

def PredictFace(img):
    img = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY)
    global model
    img = cv2.resize(img, (200, 200))
    [Y_pred_temp, Y_confidence_temp] = model.predict(np.asarray(img, dtype=np.uint8))
    return Y_pred_temp, Y_confidence_temp