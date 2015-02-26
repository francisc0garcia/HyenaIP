# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/3DCV_projects/HyenaIP/HyenaIP/Forms/ImageOnlineTest/imageonlinetest.ui'
#
# Created: Thu Feb 26 10:29:25 2015
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

class Ui_ImageOnlineTest(object):
    def setupUi(self, ImageOnlineTest):
        ImageOnlineTest.setObjectName(_fromUtf8("ImageOnlineTest"))
        ImageOnlineTest.resize(1024, 720)
        ImageOnlineTest.setMinimumSize(QtCore.QSize(1024, 720))
        ImageOnlineTest.setMaximumSize(QtCore.QSize(1024, 720))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        ImageOnlineTest.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Media/Images/HyenaLogo.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ImageOnlineTest.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(ImageOnlineTest)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 571, 631))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.Lb_cameraInput = QtGui.QLabel(self.groupBox)
        self.Lb_cameraInput.setGeometry(QtCore.QRect(10, 20, 551, 601))
        self.Lb_cameraInput.setText(_fromUtf8(""))
        self.Lb_cameraInput.setPixmap(QtGui.QPixmap(_fromUtf8("../../Media/Images/HyenaLogo.gif")))
        self.Lb_cameraInput.setAlignment(QtCore.Qt.AlignCenter)
        self.Lb_cameraInput.setObjectName(_fromUtf8("Lb_cameraInput"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(600, 10, 411, 631))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.Btn_Start = QtGui.QPushButton(self.groupBox_2)
        self.Btn_Start.setGeometry(QtCore.QRect(20, 40, 381, 41))
        self.Btn_Start.setObjectName(_fromUtf8("Btn_Start"))
        self.Pt_Results = QtGui.QPlainTextEdit(self.groupBox_2)
        self.Pt_Results.setGeometry(QtCore.QRect(20, 100, 381, 521))
        self.Pt_Results.setObjectName(_fromUtf8("Pt_Results"))
        ImageOnlineTest.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(ImageOnlineTest)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        ImageOnlineTest.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(ImageOnlineTest)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        ImageOnlineTest.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(ImageOnlineTest)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        ImageOnlineTest.setStatusBar(self.statusBar)
        self.actionClose_Module = QtGui.QAction(ImageOnlineTest)
        self.actionClose_Module.setObjectName(_fromUtf8("actionClose_Module"))
        self.actionLicense = QtGui.QAction(ImageOnlineTest)
        self.actionLicense.setObjectName(_fromUtf8("actionLicense"))
        self.menuFile.addAction(self.actionClose_Module)
        self.menuAbout.addAction(self.actionLicense)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(ImageOnlineTest)
        QtCore.QMetaObject.connectSlotsByName(ImageOnlineTest)

    def retranslateUi(self, ImageOnlineTest):
        ImageOnlineTest.setWindowTitle(_translate("ImageOnlineTest", "Hyena - Image Online Test", None))
        self.groupBox.setTitle(_translate("ImageOnlineTest", "Camera input", None))
        self.groupBox_2.setTitle(_translate("ImageOnlineTest", "Results", None))
        self.Btn_Start.setText(_translate("ImageOnlineTest", "Start online test", None))
        self.menuFile.setTitle(_translate("ImageOnlineTest", "File", None))
        self.menuAbout.setTitle(_translate("ImageOnlineTest", "About", None))
        self.actionClose_Module.setText(_translate("ImageOnlineTest", "Close Module", None))
        self.actionLicense.setText(_translate("ImageOnlineTest", "License", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ImageOnlineTest = QtGui.QMainWindow()
    ui = Ui_ImageOnlineTest()
    ui.setupUi(ImageOnlineTest)
    ImageOnlineTest.show()
    sys.exit(app.exec_())

