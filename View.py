from ImageController import ImageController
from PyQt5 import (QtWidgets, QtGui)

class View(QtWidgets.QWidget):
    @staticmethod
    def createApp(argv):
        return QtWidgets.QApplication(argv)

    def __init__(self):
        super().__init__()

        self.__imageLabel = QtWidgets.QLabel()
        self.__workSpaceLabel = QtWidgets.QLabel()
        self.__listWidget = QtWidgets.QListWidget()
        
        self.__layout()
        self.__setSlot()
        
    def __layout(self):
        self.__listWidget.resize(120, 240)
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.__imageLabel)
        vbox.addWidget(self.__workSpaceLabel)
        vbox.addWidget(self.__listWidget)
        
        self.setLayout(vbox)

    def __setSlot(self):
        self.__listWidget.currentItemChanged.connect(self.__getAndShowPreviewOfCurrentItem)
        
    def __getAndShowPreviewOfCurrentItem(self, current, previous):
        if current is not None:
            imageQt = ImageController.readThumbnail(self.__workSpaceLabel.text() + current.text())
            self.__showImage(imageQt)

    def setWorkSpace(self, workSpace):
        self.__workSpaceLabel.setText(workSpace)
            
    def __showImage(self, imageqt):
        pixmap = QtGui.QPixmap.fromImage(imageqt)
        
        self.__imageLabel.setPixmap(pixmap)

    def showList(self, fileList):
        for fileName in fileList:
            item = QtWidgets.QListWidgetItem()
            item.setText(fileName)
            
            self.__listWidget.addItem(item)
