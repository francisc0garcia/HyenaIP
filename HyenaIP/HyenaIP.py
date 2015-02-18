import sys
import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, Qt
from Forms import *
from Forms.Hyena.UIhomescreen import *

class Gui(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui =  Ui_HomeScreen()
        self.ui.setupUi(self)
        self.update()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Gui()
    ex.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()