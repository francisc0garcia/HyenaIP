import os, sys, cv2, numpy as np, uuid
from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4.QtCore import *

def normalize(X, low, high, dtype=None):
    """Normalizes a given array in X to a value between low and high."""
    X = np.asarray(X)
    minX, maxX = np.min(X), np.max(X)
    # normalize to [0...1].    
    X = X - float(minX)
    X = X / float((maxX - minX))
    # scale to [low...high].
    X = X * (high-low)
    X = X + low
    if dtype is None:
        return np.asarray(X)
    return np.asarray(X, dtype=dtype)


def read_images(path, sz=None):
    indexFile = 0
    c = 0
    X, Y, Labels, Classes = [], [], [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            Classes.append(subdirname)
            for filename in os.listdir(subject_path):
                if os.path.splitext(filename)[1].lower() in ('.jpg', '.jpeg', '.png', '.bmp'):
                    try:
                        im = cv2.imread(os.path.join(subject_path, filename), cv2.COLOR_BGR2RGB)
                        #cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

                        #Crop the face in the image
                        CropImage = False
                        [imTemp, CropImage, IsDetected] = detect(im, cascade_fn="Media\haarcascades\haarcascade_frontalface_alt2.xml")

                        if(IsDetected):
                            im = CropImage

                        if(len(im) <= 0):
                            print "Bad image: " + str(os.path.join(subject_path, filename))

                        im = cv2.cvtColor( im , cv2.COLOR_BGR2GRAY)

                        #cv2.imwrite("C:\\Users\\Pach0-PC\\Desktop\\Test\\ImageReading\\" +  str(indexFile) + ".jpg", im )
                        #indexFile = indexFile + 1

                        # resize to given size (if given)
                        if (sz is not None):
                            im = cv2.resize(im, sz)
                        X.append(np.asarray(im, dtype=np.uint8))
                        Y.append(c)
                        Labels.append(subdirname)
                    except IOError, (errno, strerror):
                        print "I/O error({0}): {1}".format(errno, strerror)
                    except:
                        print "Unexpected error:", sys.exc_info()[0]
                        raise
            c = c+1
    return [X, Y, Labels, Classes]

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


def ShowLicense():
    msgBox = QMessageBox();

    strLicense = 'Licensed under MIT license  http://en.wikipedia.org/wiki/MIT_License \n\n Francisco J. Garcia R 2015'
    msgBox.setText("Hyena - image processing and training                           ");
    msgBox.setInformativeText(strLicense);
    msgBox.setStandardButtons(QMessageBox.Ok);
    msgBox.setDefaultButton(QMessageBox.Ok);
    msgBox.setIcon(QMessageBox.Information);
    msgBox.setWindowTitle("Hyena");

    ret = msgBox.exec_();

def GetItemsSelected(ListPack):
    '''
    Return list of selected items in List
    '''
    selectedItems=[]

    try:
        items = ListPack.count()
        rangedList =range(items)
        rangedList.reverse()
        for i in rangedList:
            if ListPack.isItemSelected(ListPack.item(i))==True:
                selectedItems.append(i)
    except:
        showErrorMessage("Error in GetItemsSelected()", sys.exc_info() );
        
    return selectedItems