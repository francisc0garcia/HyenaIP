import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4.QtCore import *

def showErrorMessage(strMessage, ErrorObj):  
    msgBox = QMessageBox();
    strDetails = str(ErrorObj[0]) + "\n\n" + str(ErrorObj[1]) + "\n\n" + str(ErrorObj[2]) + "\n\n";
    
    print strMessage
    print strDetails

    msgBox.setText("Hyena - image processing and training                           ");
    msgBox.setInformativeText(strMessage);
    msgBox.setStandardButtons(QMessageBox.Ok);
    msgBox.setDefaultButton(QMessageBox.Ok);
    msgBox.setDetailedText(strDetails);
    msgBox.setIcon(QMessageBox.Warning);
    msgBox.setWindowTitle("Hyena");

    ret = msgBox.exec_();
