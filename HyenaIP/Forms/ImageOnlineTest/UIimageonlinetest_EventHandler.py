import sys, os, cv2, numpy as np, shutil, uuid

from Classes.GlobalSettings import *
from Classes.VideoHandler import *
from Classes.Utils import *

HomeFrame = 0
GlobalConfig = GlobalSettings()
ImageOnlineTest = 0

def UIimageOnlineTest_LoadEvents(parent, Config):
    print "UIimageOnlineTest_LoadEvents"
    
    global HomeFrame
    HomeFrame = parent

    global GlobalConfig
    GlobalConfig = Config

    global ImageTrainingFrame
    ImageOnlineTest = HomeFrame.GUI_Ui_ImageOnlineTest