# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/3DCV_projects/HyenaIP/HyenaIP/Forms/ImageAcquisitionModule/imageacquisition.ui'
#
# Created: Thu Feb 19 19:34:51 2015
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

class Ui_ImageAcquisition(object):
    def setupUi(self, ImageAcquisition):
        ImageAcquisition.setObjectName(_fromUtf8("ImageAcquisition"))
        ImageAcquisition.resize(1024, 720)
        ImageAcquisition.setMinimumSize(QtCore.QSize(1024, 720))
        ImageAcquisition.setMaximumSize(QtCore.QSize(1024, 720))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        ImageAcquisition.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Media/Images/HyenaLogo.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ImageAcquisition.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(ImageAcquisition)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.ListPackages = QtGui.QListWidget(self.centralWidget)
        self.ListPackages.setGeometry(QtCore.QRect(10, 80, 311, 411))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ListPackages.setFont(font)
        self.ListPackages.setObjectName(_fromUtf8("ListPackages"))
        item = QtGui.QListWidgetItem()
        self.ListPackages.addItem(item)
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(330, 10, 681, 81))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.BtnSelectImages = QtGui.QPushButton(self.groupBox)
        self.BtnSelectImages.setGeometry(QtCore.QRect(380, 20, 291, 50))
        self.BtnSelectImages.setObjectName(_fromUtf8("BtnSelectImages"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 110, 681, 521))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(180, 40, 491, 471))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.LabelImage = QtGui.QLabel(self.groupBox_3)
        self.LabelImage.setGeometry(QtCore.QRect(10, 10, 471, 451))
        self.LabelImage.setAutoFillBackground(False)
        self.LabelImage.setText(_fromUtf8(""))
        self.LabelImage.setPixmap(QtGui.QPixmap(_fromUtf8("Media/Images/HyenaLogo.gif")))
        self.LabelImage.setScaledContents(False)
        self.LabelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelImage.setWordWrap(False)
        self.LabelImage.setObjectName(_fromUtf8("LabelImage"))
        self.BtnConnectDevice = QtGui.QPushButton(self.groupBox_2)
        self.BtnConnectDevice.setGeometry(QtCore.QRect(10, 40, 151, 50))
        self.BtnConnectDevice.setObjectName(_fromUtf8("BtnConnectDevice"))
        self.BtnTakePhoto = QtGui.QPushButton(self.groupBox_2)
        self.BtnTakePhoto.setGeometry(QtCore.QRect(10, 460, 151, 50))
        self.BtnTakePhoto.setObjectName(_fromUtf8("BtnTakePhoto"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 301, 61))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 500, 311, 131))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.LineNameNewPackage = QtGui.QLineEdit(self.groupBox_4)
        self.LineNameNewPackage.setGeometry(QtCore.QRect(70, 30, 231, 31))
        self.LineNameNewPackage.setText(_fromUtf8(""))
        self.LineNameNewPackage.setObjectName(_fromUtf8("LineNameNewPackage"))
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 71, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.BtnAddNewPackage = QtGui.QPushButton(self.groupBox_4)
        self.BtnAddNewPackage.setGeometry(QtCore.QRect(240, 70, 61, 50))
        self.BtnAddNewPackage.setObjectName(_fromUtf8("BtnAddNewPackage"))
        self.BtnRemovePackage = QtGui.QPushButton(self.groupBox_4)
        self.BtnRemovePackage.setGeometry(QtCore.QRect(10, 70, 181, 50))
        self.BtnRemovePackage.setObjectName(_fromUtf8("BtnRemovePackage"))
        ImageAcquisition.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(ImageAcquisition)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 31))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        ImageAcquisition.setMenuBar(self.menuBar)
        self.ImageAcquisitionModule = QtGui.QToolBar(ImageAcquisition)
        self.ImageAcquisitionModule.setMinimumSize(QtCore.QSize(1024, 0))
        self.ImageAcquisitionModule.setObjectName(_fromUtf8("ImageAcquisitionModule"))
        ImageAcquisition.addToolBar(QtCore.Qt.TopToolBarArea, self.ImageAcquisitionModule)
        self.statusBar = QtGui.QStatusBar(ImageAcquisition)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        ImageAcquisition.setStatusBar(self.statusBar)
        self.actionClose_Module = QtGui.QAction(ImageAcquisition)
        self.actionClose_Module.setObjectName(_fromUtf8("actionClose_Module"))
        self.actionLicence = QtGui.QAction(ImageAcquisition)
        self.actionLicence.setObjectName(_fromUtf8("actionLicence"))
        self.menuFile.addAction(self.actionClose_Module)
        self.menuAbout.addAction(self.actionLicence)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(ImageAcquisition)
        QtCore.QMetaObject.connectSlotsByName(ImageAcquisition)

    def retranslateUi(self, ImageAcquisition):
        ImageAcquisition.setWindowTitle(_translate("ImageAcquisition", "Hyena - Image Acquisition Module", None))
        self.ListPackages.setSortingEnabled(True)
        __sortingEnabled = self.ListPackages.isSortingEnabled()
        self.ListPackages.setSortingEnabled(False)
        item = self.ListPackages.item(0)
        item.setText(_translate("ImageAcquisition", "No packages found", None))
        self.ListPackages.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("ImageAcquisition", "Add images from the existing files", None))
        self.BtnSelectImages.setText(_translate("ImageAcquisition", "Select images", None))
        self.groupBox_2.setTitle(_translate("ImageAcquisition", "Add images from Camera devices", None))
        self.BtnConnectDevice.setText(_translate("ImageAcquisition", "Turn On Camera", None))
        self.BtnTakePhoto.setText(_translate("ImageAcquisition", "Take Photo", None))
        self.label_4.setText(_translate("ImageAcquisition", "<html><head/><body><p><span style=\" font-weight:600;\">Packages available</span></p><p>Select the package for add images:</p></body></html>", None))
        self.groupBox_4.setTitle(_translate("ImageAcquisition", "Create new package", None))
        self.label_2.setText(_translate("ImageAcquisition", "Name:", None))
        self.BtnAddNewPackage.setText(_translate("ImageAcquisition", "Add", None))
        self.BtnRemovePackage.setText(_translate("ImageAcquisition", "Remove selected", None))
        self.menuFile.setTitle(_translate("ImageAcquisition", "File", None))
        self.menuAbout.setTitle(_translate("ImageAcquisition", "About", None))
        self.actionClose_Module.setText(_translate("ImageAcquisition", "Close Module", None))
        self.actionLicence.setText(_translate("ImageAcquisition", "Licence", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ImageAcquisition = QtGui.QMainWindow()
    ui = Ui_ImageAcquisition()
    ui.setupUi(ImageAcquisition)
    ImageAcquisition.show()
    sys.exit(app.exec_())

