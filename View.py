from ImageController import ImageController
from PyQt5 import (QtWidgets, QtWebEngineWidgets, QtGui, QtCore)
import os

class Filter(QtCore.QObject):
    def eventFilter(self, widget, event):
        if event.type() == QtCore.QEvent.KeyRelease:
            if event.key() == QtCore.Qt.Key_Space:
                widget.preprocessImplantGPSTag()
                return True

        return False

class ImageLavel(QtWidgets.QLabel):
    def showImage(self, imageqt):
        pixmap = QtGui.QPixmap.fromImage(imageqt)
        self.setPixmap(pixmap)

class WorkSpaceLabel(QtWidgets.QLineEdit):
    def __init__(self, workSpacePath):
        super().__init__()
        self.setWorkSpace(workSpacePath)
    
    def setWorkSpace(self, workSpacePath):
        self.setText(workSpacePath)

    def getWorkSpace(self):
        return self.text()

class View(QtWidgets.QWidget):
    @staticmethod
    def createApp(argv):
        return QtWidgets.QApplication(argv)

    def __init__(self, execPath, workSpacePath):
        super().__init__()

        self.__imageLabel = ImageLavel()
        self.__workSpaceLabel = WorkSpaceLabel(workSpacePath)
        self.__listWidget = QtWidgets.QListWidget()
        self.__webView = QtWebEngineWidgets.QWebEngineView()
        self.__webView.load(QtCore.QUrl("file://" + execPath + "/map.html"))

        self.installEventFilter(Filter(self))

        self.__layout()
        self.__setSlot()
        
    def __layout(self):
        self.__listWidget.resize(120, 240)
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.__imageLabel)
        vbox.addWidget(self.__workSpaceLabel)
        vbox.addWidget(self.__listWidget)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addWidget(self.__webView)

        self.setLayout(hbox)

    def __setSlot(self):
        self.__listWidget.currentItemChanged.connect(self.__getAndShowPreviewOfCurrentItem)
        
    def __getAndShowPreviewOfCurrentItem(self, current, previous):
        if current is not None:
            thumbnail = ImageController.readThumbnail(self.__workSpaceLabel.getWorkSpace() + current.text())

            if thumbnail is not None:
                self.__imageLabel.showImage(thumbnail)

    def getWorkSpace(self):
        return self.__workSpaceLabel.getWorkSpace()
        
    def showList(self, fileList):
        for fileName in fileList:
            item = QtWidgets.QListWidgetItem()
            item.setText(fileName)
            
            self.__listWidget.addItem(item)

    def preprocessImplantGPSTag(self):
        self.__webView.page().runJavaScript("latitude", self.__implantGPSTag)
        
    def __implantGPSTag(self, latitude):
        print(self.__workSpaceLabel.getWorkSpace())
        print(latitude)        
