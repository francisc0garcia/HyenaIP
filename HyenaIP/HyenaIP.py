import sys
from PyQt4 import QtGui, QtCore, Qt

from Forms.Hyena.UIhomescreen import *
from Forms.Hyena.UIhomeScreen_EventHandler import *

from Forms.ImageAcquisitionModule.UIimageacquisition import *


class GUI_UIimageacquisition(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.w =  Ui_ImageAcquisition()
        self.w.update()

class Gui_UIhomescreen(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui =  Ui_HomeScreen()
        self.ui.setupUi(self)
        self.update()

        LoadEvents(self)



def main():
    app = QtGui.QApplication(sys.argv)
    ex = Gui_UIhomescreen()
    ex.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()