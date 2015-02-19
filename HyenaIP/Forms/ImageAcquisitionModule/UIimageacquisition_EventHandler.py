import sys
import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, Qt

from Classes.VideoHandler import *

ImageAcquisitionFrame = 0
parentFrame = 0

def UIimageacquisition_LoadEvents(parent):
    '''
    Connect events to controls and define behaviour in UI elements
    '''
    global ImageAcquisitionFrame
    ImageAcquisitionFrame = parent.GUI_UIimageacquisition

    global parentFrame
    parentFrame = parent

    def CloseWindow():
        sys.exit(0)

    def SelectExistingFile():
        filename = QtGui.QFileDialog.getOpenFileName(
                parentFrame, 'Open File', '', 'Images (*.png *.xpm *.jpg)')

    def ConnectDevice():
        ImageAcquisitionFrame.video = VideoHandler()
        ImageAcquisitionFrame._timer = QtCore.QTimer(parentFrame)
        ImageAcquisitionFrame._timer.timeout.connect(play)
        ImageAcquisitionFrame._timer.start(27)

    def play():
        try:
            ImageAcquisitionFrame.video.captureNextFrame()
            ImageAcquisitionFrame.LabelImage.setPixmap(ImageAcquisitionFrame.video.convertFrame())
            ImageAcquisitionFrame.LabelImage.setScaledContents(True)
        except TypeError:
            print "No frame"

    ImageAcquisitionFrame.actionClose_Module.triggered.connect(CloseWindow)
    ImageAcquisitionFrame.BtnSelectImages.clicked.connect(SelectExistingFile)
    ImageAcquisitionFrame.BtnConnectDevice.clicked.connect(ConnectDevice)