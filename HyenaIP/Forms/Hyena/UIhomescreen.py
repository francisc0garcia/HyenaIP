# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/3DCV_projects/HyenaIP/HyenaIP/Forms/Hyena/homescreen.ui'
#
# Created: Tue Mar 10 17:35:24 2015
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

class Ui_HomeScreen(object):
    def setupUi(self, HomeScreen):
        HomeScreen.setObjectName(_fromUtf8("HomeScreen"))
        HomeScreen.resize(800, 520)
        HomeScreen.setMinimumSize(QtCore.QSize(800, 520))
        HomeScreen.setMaximumSize(QtCore.QSize(800, 520))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        HomeScreen.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/Media/Images/HyenaLogo.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HomeScreen.setWindowIcon(icon)
        HomeScreen.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralWidget = QtGui.QWidget(HomeScreen)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 110, 781, 321))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 760, 220))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.BtnCreateLoad = QtGui.QPushButton(self.tab)
        self.BtnCreateLoad.setGeometry(QtCore.QRect(430, 170, 330, 50))
        self.BtnCreateLoad.setObjectName(_fromUtf8("BtnCreateLoad"))
        self.TextEditDirectoryPath = QtGui.QLineEdit(self.tab)
        self.TextEditDirectoryPath.setGeometry(QtCore.QRect(10, 230, 751, 41))
        self.TextEditDirectoryPath.setObjectName(_fromUtf8("TextEditDirectoryPath"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.BtnImageDAQ = QtGui.QPushButton(self.tab_3)
        self.BtnImageDAQ.setGeometry(QtCore.QRect(430, 220, 330, 50))
        self.BtnImageDAQ.setObjectName(_fromUtf8("BtnImageDAQ"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 760, 220))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.BtnImageProcessing = QtGui.QPushButton(self.tab_2)
        self.BtnImageProcessing.setGeometry(QtCore.QRect(430, 220, 330, 50))
        self.BtnImageProcessing.setObjectName(_fromUtf8("BtnImageProcessing"))
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 760, 220))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.BtnTraining = QtGui.QPushButton(self.tab_4)
        self.BtnTraining.setGeometry(QtCore.QRect(430, 220, 330, 50))
        self.BtnTraining.setObjectName(_fromUtf8("BtnTraining"))
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 760, 220))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.BtnTestError = QtGui.QPushButton(self.tab_5)
        self.BtnTestError.setGeometry(QtCore.QRect(430, 220, 330, 50))
        self.BtnTestError.setObjectName(_fromUtf8("BtnTestError"))
        self.label_8 = QtGui.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 760, 220))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.groupBox = QtGui.QGroupBox(self.tab_6)
        self.groupBox.setGeometry(QtCore.QRect(10, 9, 751, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 441, 61))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.BtnExportToQuickCOG = QtGui.QPushButton(self.groupBox)
        self.BtnExportToQuickCOG.setGeometry(QtCore.QRect(512, 60, 231, 41))
        self.BtnExportToQuickCOG.setObjectName(_fromUtf8("BtnExportToQuickCOG"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(80, 0, 441, 101))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(620, 10, 171, 91))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 61, 91))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("/Media/Images/HyenaLogo.gif")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        HomeScreen.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(HomeScreen)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        HomeScreen.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(HomeScreen)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        HomeScreen.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(HomeScreen)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        HomeScreen.setStatusBar(self.statusBar)
        self.actionExit = QtGui.QAction(HomeScreen)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionLicense = QtGui.QAction(HomeScreen)
        self.actionLicense.setObjectName(_fromUtf8("actionLicense"))
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionLicense)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(HomeScreen)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HomeScreen)
        HomeScreen.setTabOrder(self.tabWidget, self.BtnCreateLoad)

    def retranslateUi(self, HomeScreen):
        HomeScreen.setWindowTitle(_translate("HomeScreen", "Hyena", None))
        self.label_2.setText(_translate("HomeScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Project Module</span></p><p><br/><span style=\" font-style:italic;\">Welcome to Hyena!</span></p><p>The first step is define a specific folder as working directory, in which application</p><p>will save the images as well as will perform the training and test process.</p><p><br/>Please select a folder for the project:<br/><br/><br/><br/><br/></p></body></html>", None))
        self.BtnCreateLoad.setText(_translate("HomeScreen", "Select working directory", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("HomeScreen", "Project", None))
        self.BtnImageDAQ.setText(_translate("HomeScreen", "Launch Image Acquisition module", None))
        self.label_4.setText(_translate("HomeScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Image acquisition module</span></p><p><br/>This module allows you get and store images for future training or classification processes.</p><p>It is possible get image in real time from the camera or select images from the disk.</p><p><br/></p><p><br/></p><p><br/></p><p><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("HomeScreen", "1. Acquisition", None))
        self.BtnImageProcessing.setText(_translate("HomeScreen", "Launch Image Processing module", None))
        self.label_6.setText(_translate("HomeScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Image Processing Module</span></p><p><br/></p><p>This module allows you perform different processing task in images such as filtering,</p><p>thresholding, canny detector, gaussian and laplace filters, in order to prepare </p><p>the images for futures process of training and identification.</p><p><br/></p><p><br/></p><p><br/></p><p><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("HomeScreen", "2. Processing", None))
        self.BtnTraining.setText(_translate("HomeScreen", "Launch Training module", None))
        self.label_7.setText(_translate("HomeScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Image training module</span></p><p><br/></p><p>This module allow you train algorithms for learning features of images, based on</p><p>FaceRecognizer class in OpenCV, in order to complete recognition or detection tasks.</p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("HomeScreen", "3. Training", None))
        self.BtnTestError.setText(_translate("HomeScreen", "Launch Online test module", None))
        self.label_8.setText(_translate("HomeScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Online Test of Models</span></p><p><br/></p><p>This module allows you test in real time the models which was trained in the Training module,</p><p>it is necessary to train the packages before the Online test.</p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("HomeScreen", "4. Online Test of models ", None))
        self.groupBox.setTitle(_translate("HomeScreen", "QuickCog", None))
        self.label_9.setText(_translate("HomeScreen", "<html><head/><body><p>This option allow you export the images files to QuickCog </p><p>Dataset content (format .ews)  and Class information (format .NIF)</p></body></html>", None))
        self.BtnExportToQuickCOG.setText(_translate("HomeScreen", "Export Dataset to QuickCog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("HomeScreen", "5. Export", None))
        self.label.setText(_translate("HomeScreen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Hyena</span></p><p><span style=\" font-size:7pt; color:#535353;\">Acquisition, processing, training and testing process </span></p><p><span style=\" font-size:7pt; color:#535353;\">of images with python and OpenCV.</span></p></body></html>", None))
        self.label_3.setText(_translate("HomeScreen", "<html><head/><body><p align=\"right\"><span style=\" font-size:7pt;\">Developed by</span></p><p align=\"right\"><span style=\" font-size:7pt; font-weight:600;\">Francisco J Garcia R</span></p><p align=\"right\"><span style=\" font-size:7pt; font-weight:600;\">2015</span></p></body></html>", None))
        self.menuFile.setTitle(_translate("HomeScreen", "File", None))
        self.menuAbout.setTitle(_translate("HomeScreen", "About", None))
        self.actionExit.setText(_translate("HomeScreen", "Exit", None))
        self.actionLicense.setText(_translate("HomeScreen", "License", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HomeScreen = QtGui.QMainWindow()
    ui = Ui_HomeScreen()
    ui.setupUi(HomeScreen)
    HomeScreen.show()
    sys.exit(app.exec_())

