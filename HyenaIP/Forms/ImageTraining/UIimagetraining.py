# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/3DCV_projects/HyenaIP/HyenaIP/Forms/ImageTraining/imagetraining.ui'
#
# Created: Wed Feb 25 17:38:08 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ImageTraining(object):
    def setupUi(self, ImageTraining):
        ImageTraining.setObjectName(_fromUtf8("ImageTraining"))
        ImageTraining.resize(1024, 720)
        ImageTraining.setMinimumSize(QtCore.QSize(1024, 720))
        ImageTraining.setMaximumSize(QtCore.QSize(1024, 720))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        ImageTraining.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Media/Images/HyenaLogo.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ImageTraining.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(ImageTraining)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1001, 631))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 311, 431))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 150, 101, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.Hs_TrainTestSize = QtGui.QSlider(self.groupBox)
        self.Hs_TrainTestSize.setGeometry(QtCore.QRect(10, 180, 281, 31))
        self.Hs_TrainTestSize.setProperty("value", 60)
        self.Hs_TrainTestSize.setOrientation(QtCore.Qt.Horizontal)
        self.Hs_TrainTestSize.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.Hs_TrainTestSize.setTickInterval(10)
        self.Hs_TrainTestSize.setObjectName(_fromUtf8("Hs_TrainTestSize"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 230, 101, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Hs_Kfold = QtGui.QSlider(self.groupBox)
        self.Hs_Kfold.setGeometry(QtCore.QRect(10, 260, 281, 31))
        self.Hs_Kfold.setMaximum(10)
        self.Hs_Kfold.setProperty("value", 3)
        self.Hs_Kfold.setOrientation(QtCore.Qt.Horizontal)
        self.Hs_Kfold.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.Hs_Kfold.setTickInterval(1)
        self.Hs_Kfold.setObjectName(_fromUtf8("Hs_Kfold"))
        self.Btn_Train = QtGui.QPushButton(self.groupBox)
        self.Btn_Train.setGeometry(QtCore.QRect(10, 320, 281, 41))
        self.Btn_Train.setObjectName(_fromUtf8("Btn_Train"))
        self.Rb_EigenRec = QtGui.QRadioButton(self.groupBox)
        self.Rb_EigenRec.setGeometry(QtCore.QRect(10, 90, 231, 20))
        self.Rb_EigenRec.setObjectName(_fromUtf8("Rb_EigenRec"))
        self.Rb_FisherRec = QtGui.QRadioButton(self.groupBox)
        self.Rb_FisherRec.setGeometry(QtCore.QRect(10, 30, 231, 20))
        self.Rb_FisherRec.setChecked(True)
        self.Rb_FisherRec.setObjectName(_fromUtf8("Rb_FisherRec"))
        self.Rb_LBPHRec = QtGui.QRadioButton(self.groupBox)
        self.Rb_LBPHRec.setGeometry(QtCore.QRect(10, 60, 231, 20))
        self.Rb_LBPHRec.setObjectName(_fromUtf8("Rb_LBPHRec"))
        self.Pb_Progress = QtGui.QProgressBar(self.groupBox)
        self.Pb_Progress.setGeometry(QtCore.QRect(10, 380, 281, 31))
        self.Pb_Progress.setProperty("value", 24)
        self.Pb_Progress.setTextVisible(False)
        self.Pb_Progress.setObjectName(_fromUtf8("Pb_Progress"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 10, 640, 280))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.Lb_MeanFace = QtGui.QLabel(self.groupBox_2)
        self.Lb_MeanFace.setGeometry(QtCore.QRect(10, 20, 621, 251))
        self.Lb_MeanFace.setText(_fromUtf8(""))
        self.Lb_MeanFace.setPixmap(QtGui.QPixmap(_fromUtf8("../../Media/Images/HyenaLogo.gif")))
        self.Lb_MeanFace.setAlignment(QtCore.Qt.AlignCenter)
        self.Lb_MeanFace.setObjectName(_fromUtf8("Lb_MeanFace"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(340, 300, 640, 280))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.Lb_EigenFace = QtGui.QLabel(self.groupBox_3)
        self.Lb_EigenFace.setGeometry(QtCore.QRect(10, 20, 621, 251))
        self.Lb_EigenFace.setText(_fromUtf8(""))
        self.Lb_EigenFace.setPixmap(QtGui.QPixmap(_fromUtf8("../../Media/Images/HyenaLogo.gif")))
        self.Lb_EigenFace.setAlignment(QtCore.Qt.AlignCenter)
        self.Lb_EigenFace.setObjectName(_fromUtf8("Lb_EigenFace"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 480, 580))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.Lb_ConfusionMatrix = QtGui.QLabel(self.groupBox_4)
        self.Lb_ConfusionMatrix.setGeometry(QtCore.QRect(10, 20, 461, 551))
        self.Lb_ConfusionMatrix.setText(_fromUtf8(""))
        self.Lb_ConfusionMatrix.setPixmap(QtGui.QPixmap(_fromUtf8("../../Media/Images/HyenaLogo.gif")))
        self.Lb_ConfusionMatrix.setAlignment(QtCore.Qt.AlignCenter)
        self.Lb_ConfusionMatrix.setObjectName(_fromUtf8("Lb_ConfusionMatrix"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(510, 10, 480, 580))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.Lb_ROCcurves = QtGui.QLabel(self.groupBox_5)
        self.Lb_ROCcurves.setGeometry(QtCore.QRect(10, 20, 461, 551))
        self.Lb_ROCcurves.setText(_fromUtf8(""))
        self.Lb_ROCcurves.setPixmap(QtGui.QPixmap(_fromUtf8("../../Media/Images/HyenaLogo.gif")))
        self.Lb_ROCcurves.setAlignment(QtCore.Qt.AlignCenter)
        self.Lb_ROCcurves.setObjectName(_fromUtf8("Lb_ROCcurves"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        ImageTraining.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(ImageTraining)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        ImageTraining.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(ImageTraining)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        ImageTraining.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(ImageTraining)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        ImageTraining.setStatusBar(self.statusBar)
        self.actionClose_Module = QtGui.QAction(ImageTraining)
        self.actionClose_Module.setObjectName(_fromUtf8("actionClose_Module"))
        self.actionLicense = QtGui.QAction(ImageTraining)
        self.actionLicense.setObjectName(_fromUtf8("actionLicense"))
        self.menuFile.addAction(self.actionClose_Module)
        self.menuAbout.addAction(self.actionLicense)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(ImageTraining)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ImageTraining)

    def retranslateUi(self, ImageTraining):
        ImageTraining.setWindowTitle(_translate("ImageTraining", "Hyena - Image Training", None))
        self.groupBox.setTitle(_translate("ImageTraining", "Parameters", None))
        self.label.setText(_translate("ImageTraining", "Train/test size", None))
        self.label_2.setText(_translate("ImageTraining", "K-fold number", None))
        self.Btn_Train.setText(_translate("ImageTraining", "Train model", None))
        self.Rb_EigenRec.setText(_translate("ImageTraining", "Eigen Face Recognizer", None))
        self.Rb_FisherRec.setText(_translate("ImageTraining", "Fisher Face Recognizer", None))
        self.Rb_LBPHRec.setText(_translate("ImageTraining", "LBPH Face Recognizer", None))
        self.groupBox_2.setTitle(_translate("ImageTraining", "Mean face image", None))
        self.groupBox_3.setTitle(_translate("ImageTraining", "Eigen face image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ImageTraining", "Training options", None))
        self.groupBox_4.setTitle(_translate("ImageTraining", "Confusion matrix", None))
        self.groupBox_5.setTitle(_translate("ImageTraining", "ROC curves", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ImageTraining", "Validation results", None))
        self.menuFile.setTitle(_translate("ImageTraining", "File", None))
        self.menuAbout.setTitle(_translate("ImageTraining", "About", None))
        self.actionClose_Module.setText(_translate("ImageTraining", "Close Module", None))
        self.actionLicense.setText(_translate("ImageTraining", "License", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ImageTraining = QtGui.QMainWindow()
    ui = Ui_ImageTraining()
    ui.setupUi(ImageTraining)
    ImageTraining.show()
    sys.exit(app.exec_())

