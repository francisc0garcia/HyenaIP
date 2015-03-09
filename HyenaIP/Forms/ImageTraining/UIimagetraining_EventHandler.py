import sys, os, cv2, numpy as np, shutil, uuid, pickle

from sklearn import cross_validation as cross_validation
from sklearn.metrics import confusion_matrix
#from sklearn.metrics import roc_curve, auc, precision_score
#from sklearn.base import BaseEstimator

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
from Classes.ErrorHandler import *

HomeFrame = 0
GlobalConfig = GlobalSettings()
ImageTrainingFrame = 0
model = {}

def LoadMatPlotLib_canvas():
    try:

        #MeanFace Image
        ImageTrainingFrame.fig_MeanFace = Figure((13.0, 5.0), dpi=50)
        ImageTrainingFrame.canvas_MeanFace = FigureCanvas(ImageTrainingFrame.fig_MeanFace)
        ImageTrainingFrame.canvas_MeanFace.setParent(ImageTrainingFrame.Lb_MeanFace)
        ImageTrainingFrame.canvas_MeanFace.setFocus()

        ImageTrainingFrame.mpl_toolbar_MeanFace = NavigationToolbar(ImageTrainingFrame.canvas_MeanFace, ImageTrainingFrame.Lb_MeanFace)

        ImageTrainingFrame.fig_MeanFace.clear()
        ImageTrainingFrame.axes_MeanFace = ImageTrainingFrame.fig_MeanFace.add_subplot(111)
        ImageTrainingFrame.axes_MeanFace.plot(ImageTrainingFrame.Lb_MeanFace.x(), ImageTrainingFrame.Lb_MeanFace.y(), 'ro')
        ImageTrainingFrame.canvas_MeanFace.draw()

        #EigenFace Image
        ImageTrainingFrame.fig_EigenFace = Figure((5.8, 5.0), dpi=50)
        ImageTrainingFrame.canvas_EigenFace = FigureCanvas(ImageTrainingFrame.fig_EigenFace)
        ImageTrainingFrame.canvas_EigenFace.setParent(ImageTrainingFrame.Lb_EigenFace)
        ImageTrainingFrame.canvas_EigenFace.setFocus()

        ImageTrainingFrame.mpl_toolbar_EigenFace = NavigationToolbar(ImageTrainingFrame.canvas_EigenFace, ImageTrainingFrame.Lb_EigenFace)

        ImageTrainingFrame.fig_EigenFace.clear()
        ImageTrainingFrame.axes_EigenFace = ImageTrainingFrame.fig_EigenFace.add_subplot(111)
        ImageTrainingFrame.axes_EigenFace.plot(ImageTrainingFrame.Lb_EigenFace.x(), ImageTrainingFrame.Lb_EigenFace.y(), 'ro')
        ImageTrainingFrame.canvas_EigenFace.draw()

        #EigenFace 2 Image
        ImageTrainingFrame.fig_EigenFace_2 = Figure((5.8, 5.0), dpi=50)
        ImageTrainingFrame.canvas_EigenFace_2 = FigureCanvas(ImageTrainingFrame.fig_EigenFace_2)
        ImageTrainingFrame.canvas_EigenFace_2.setParent(ImageTrainingFrame.Lb_EigenFace_2)
        ImageTrainingFrame.canvas_EigenFace_2.setFocus()

        ImageTrainingFrame.mpl_toolbar_EigenFace_2 = NavigationToolbar(ImageTrainingFrame.canvas_EigenFace_2, ImageTrainingFrame.Lb_EigenFace_2)

        ImageTrainingFrame.fig_EigenFace_2.clear()
        ImageTrainingFrame.axes_EigenFace_2 = ImageTrainingFrame.fig_EigenFace_2.add_subplot(111)
        ImageTrainingFrame.axes_EigenFace_2.plot(ImageTrainingFrame.Lb_EigenFace_2.x(), ImageTrainingFrame.Lb_EigenFace_2.y(), 'ro')
        ImageTrainingFrame.canvas_EigenFace_2.draw()

        #EigenFace 3 Image
        ImageTrainingFrame.fig_EigenFace_3 = Figure((5.8, 5.0), dpi=50)
        ImageTrainingFrame.canvas_EigenFace_3 = FigureCanvas(ImageTrainingFrame.fig_EigenFace_3)
        ImageTrainingFrame.canvas_EigenFace_3.setParent(ImageTrainingFrame.Lb_EigenFace_3)
        ImageTrainingFrame.canvas_EigenFace_3.setFocus()

        ImageTrainingFrame.mpl_toolbar_EigenFace_3 = NavigationToolbar(ImageTrainingFrame.canvas_EigenFace_3, ImageTrainingFrame.Lb_EigenFace_3)

        ImageTrainingFrame.fig_EigenFace_3.clear()
        ImageTrainingFrame.axes_EigenFace_3 = ImageTrainingFrame.fig_EigenFace_3.add_subplot(111)
        ImageTrainingFrame.axes_EigenFace_3.plot(ImageTrainingFrame.Lb_EigenFace_3.x(), ImageTrainingFrame.Lb_EigenFace_3.y(), 'ro')
        ImageTrainingFrame.canvas_EigenFace_3.draw()

        #Confusion Matrix Image
        ImageTrainingFrame.fig_ConfusionMatrix = Figure((9.0, 11.0), dpi=50)
        ImageTrainingFrame.canvas_ConfusionMatrix = FigureCanvas(ImageTrainingFrame.fig_ConfusionMatrix)
        ImageTrainingFrame.canvas_ConfusionMatrix.setParent(ImageTrainingFrame.Lb_ConfusionMatrix)
        ImageTrainingFrame.canvas_ConfusionMatrix.setFocus()

        ImageTrainingFrame.mpl_toolbar_ConfusionMatrix = NavigationToolbar(ImageTrainingFrame.canvas_ConfusionMatrix, ImageTrainingFrame.Lb_ConfusionMatrix)

        ImageTrainingFrame.fig_ConfusionMatrix.clear()
        ImageTrainingFrame.axes_ConfusionMatrix = ImageTrainingFrame.fig_ConfusionMatrix.add_subplot(111)
        ImageTrainingFrame.axes_ConfusionMatrix.plot(ImageTrainingFrame.Lb_ConfusionMatrix.x(), ImageTrainingFrame.Lb_ConfusionMatrix.y(), 'ro')
        ImageTrainingFrame.canvas_ConfusionMatrix.draw()
    except:
        showErrorMessage("Error in LoadMatPlotLib_canvas()", sys.exc_info() );
    
def UIimageTraining_LoadEvents(parent, Config):
    try:
        global HomeFrame
        HomeFrame = parent

        global GlobalConfig
        GlobalConfig = Config

        global ImageTrainingFrame
        ImageTrainingFrame = HomeFrame.GUI_Ui_ImageTraining

        ImageTrainingFrame.Btn_Train.clicked.connect(TrainModel)

        LoadMatPlotLib_canvas()
        LoadSavedModel()
    except:
        showErrorMessage("Error in UIimageTraining_LoadEvents()", sys.exc_info() );

def LoadSavedModel():
    try:
        PathDir = str(GlobalConfig.PathDirectory)

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

            if not ("LBPHFaceRecognizer" in FileModel):
                mean = model.getMat("mean")
                 # We'll save the mean, by first normalizing it:
                mean_norm = normalize(mean, 0, 255, dtype=np.uint8)
                mean_resized = mean_norm.reshape(200,200)

                ImageTrainingFrame.axes_MeanFace.imshow(mean_resized, cmap="gray")
                ImageTrainingFrame.canvas_MeanFace.draw()

                eigenvectors = model.getMat("eigenvectors")

                # Turn the first (at most) 16 eigenvectors into grayscale 
                # images. You could also use cv::normalize here, but sticking
                # to NumPy is much easier for now. 
                # Note: eigenvectors are stored by column:
                for i in xrange(3):
                    eigenvector_i = eigenvectors[:,i].reshape(200,200)
                    eigenvector_i_norm = normalize(eigenvector_i, 0, 255, dtype=np.uint8)
                    eigenvector_i_colormap = cv2.applyColorMap(eigenvector_i_norm, cv2.COLORMAP_JET)
                    if(i == 0):
                        ImageTrainingFrame.axes_EigenFace.imshow(eigenvector_i_colormap)
                        ImageTrainingFrame.canvas_EigenFace.draw()
                    if(i == 1):
                        ImageTrainingFrame.axes_EigenFace_2.imshow(eigenvector_i_colormap)
                        ImageTrainingFrame.canvas_EigenFace_2.draw()
                    if(i == 2):
                        ImageTrainingFrame.axes_EigenFace_3.imshow(eigenvector_i_colormap)
                        ImageTrainingFrame.canvas_EigenFace_3.draw()
    except:
        showErrorMessage("Error in LoadSavedModel() Verify the directory path selected! ", sys.exc_info() );



def TrainModel():
    try:
        Rb_FisherRec = ImageTrainingFrame.Rb_FisherRec.isChecked()
        Rb_LBPHRec = ImageTrainingFrame.Rb_LBPHRec.isChecked()
        Rb_EigenRec = ImageTrainingFrame.Rb_EigenRec.isChecked()

        Hs_TrainTestSize = ImageTrainingFrame.Hs_TrainTestSize.value()
        #Hs_Kfold = ImageTrainingFrame.Hs_Kfold.value()

        if( (Rb_FisherRec or Rb_LBPHRec or Rb_EigenRec) and Hs_TrainTestSize > 0  ):
            print "TrainModel"
            PathDir = str(GlobalConfig.PathDirectory)

            #[X, Y, Labels, Classes] = read_images(PathDir)
            [X, Y, Labels, Classes] = read_images(PathDir, sz=(200, 200))

            # Convert labels to 32bit integers. This is a workaround for 64bit machines,
            # because the labels will truncated else. This will be fixed in code as 
            # soon as possible, so Python users don't need to know about this.
            # Thanks to Leo Dirac for reporting:
            Y = np.asarray(Y, dtype=np.int32)

            TestModel = ""
            #define model for training
            if( Rb_FisherRec ):
                model = cv2.createFisherFaceRecognizer()
                TestModel = "FisherFaceRecognizer"
            if( Rb_LBPHRec ):
                model = cv2.createLBPHFaceRecognizer()
                TestModel = "LBPHFaceRecognizer"
            if( Rb_EigenRec ):
                model = cv2.createEigenFaceRecognizer()
                TestModel = "EigenFaceRecognizer"

            [X_train, X_test, Y_train, Y_test] = SplitDataSet(X, Y, Hs_TrainTestSize )

            model.train(np.asarray(X_train), np.asarray(Y_train))

            #Save Model
            NameModelSave = PathDir + "\\Model_" + str(TestModel) + ".model"
            model.save(NameModelSave)

            #save classes
            NameClassesModelFile = PathDir + "\\ClassesModel.p"
            pickle.dump( Classes, open( NameClassesModelFile, "wb" ) )

            #Test 
            Y_pred = []
            Y_confidence = []

            maxItems = len(X_test)
            for i in range(0, maxItems):
                X_test[i] = cv2.resize(X_test[i], (200, 200))
                [Y_pred_temp, Y_confidence_temp] = model.predict(np.asarray(X_test[i], dtype=np.uint8))
                Y_pred.append(Y_pred_temp)
                Y_confidence.append(Y_confidence_temp)

                if( Y_pred_temp != Y_test[i]):
                    print "Diference--> Predict: " + str(Y_pred_temp) + " real: " + str(Y_test[i]) 

        

            # Compute confusion matrix
            cm = confusion_matrix(Y_test, Y_pred)

            print(cm)

            #Plot confusion matrix
            ImageTrainingFrame.fig_ConfusionMatrix.clear()
            ImageTrainingFrame.axes_ConfusionMatrix = ImageTrainingFrame.fig_ConfusionMatrix.add_subplot(111)
            ImageTrainingFrame.axes_ConfusionMatrix.plot(ImageTrainingFrame.Lb_ConfusionMatrix.x(), ImageTrainingFrame.Lb_ConfusionMatrix.y(), 'ro')
            cax = ImageTrainingFrame.axes_ConfusionMatrix.matshow(cm)
            ImageTrainingFrame.fig_ConfusionMatrix.colorbar(cax, orientation='vertical')
            ImageTrainingFrame.canvas_ConfusionMatrix.draw()

            from sklearn.metrics import classification_report
            report = classification_report(Y_test, Y_pred, target_names=Classes)
            print report

            ImageTrainingFrame.Pt_Report.appendPlainText(report)

            if not (Rb_LBPHRec):
                mean = model.getMat("mean")
                 # We'll save the mean, by first normalizing it:
                mean_norm = normalize(mean, 0, 255, dtype=np.uint8)
                mean_resized = mean_norm.reshape(X[0].shape)

                ImageTrainingFrame.axes_MeanFace.imshow(mean_resized, cmap="gray")
                ImageTrainingFrame.canvas_MeanFace.draw()

                eigenvectors = model.getMat("eigenvectors")

                # Turn the first (at most) 16 eigenvectors into grayscale 
                # images. You could also use cv::normalize here, but sticking
                # to NumPy is much easier for now. 
                # Note: eigenvectors are stored by column:
                for i in xrange(len(np.unique(Y))-1):
                    eigenvector_i = eigenvectors[:,i].reshape(X[0].shape)
                    eigenvector_i_norm = normalize(eigenvector_i, 0, 255, dtype=np.uint8)
                    eigenvector_i_colormap = cv2.applyColorMap(eigenvector_i_norm, cv2.COLORMAP_JET)
                    if(i == 0):
                        ImageTrainingFrame.axes_EigenFace.imshow(eigenvector_i_colormap)
                        ImageTrainingFrame.canvas_EigenFace.draw()
                    if(i == 1):
                        ImageTrainingFrame.axes_EigenFace_2.imshow(eigenvector_i_colormap)
                        ImageTrainingFrame.canvas_EigenFace_2.draw()
                    if(i == 2):
                        ImageTrainingFrame.axes_EigenFace_3.imshow(eigenvector_i_colormap)
                        ImageTrainingFrame.canvas_EigenFace_3.draw()
    except:
        showErrorMessage("Error in TrainModel()", sys.exc_info() );
                
def SplitDataSet(X, Y, TrainSetSize):
    test_size = 1 - (float(TrainSetSize) / 100)

    #Split
    X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=test_size, random_state=42)

    return X_train, X_test, Y_train, Y_test