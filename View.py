from PyQt5 import (QtWidgets, QtGui)

class View(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
    def showImage(self, imageqt):
        pixmap = QtGui.QPixmap.fromImage(imageqt)

        lbl = QtWidgets.QLabel(self)
        lbl.setPixmap(pixmap)
