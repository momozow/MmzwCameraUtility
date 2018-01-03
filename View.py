from ImageController import ImageController
from PyQt5 import (QtWidgets, QtWebEngineWidgets, QtGui, QtCore)
import os

class Filter(QtCore.QObject):
    def eventFilter(self, widget, event):
        if event.type() == 51:
            print('SPC')

        return False

class View(QtWidgets.QWidget):
    @staticmethod
    def createApp(argv):
        return QtWidgets.QApplication(argv)

    def __init__(self, execPath):
        super().__init__()

        self.__imageLabel = QtWidgets.QLabel()
        self.__workSpaceLabel = QtWidgets.QLineEdit()
        self.__listWidget = QtWidgets.QListWidget()
        self.__webView = QtWebEngineWidgets.QWebEngineView()

        self.__webView.installEventFilter(Filter(self))
        self.__webView.load(QtCore.QUrl("file://" + execPath + "/map.html"))

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
            thumbnail = ImageController.readThumbnail(self.__workSpaceLabel.text() + current.text())

            if thumbnail is not None:
                self.__showImage(thumbnail)

    def __showImage(self, imageqt):
        pixmap = QtGui.QPixmap.fromImage(imageqt)
        
        self.__imageLabel.setPixmap(pixmap)

    def setWorkSpace(self, workSpace):
        self.__workSpaceLabel.setText(workSpace)

    def getWorkSpace(self):
        return self.__workSpaceLabel.text()
            
    def showList(self, fileList):
        for fileName in fileList:
            item = QtWidgets.QListWidgetItem()
            item.setText(fileName)
            
            self.__listWidget.addItem(item)

    def getLatLonFromMap(self):
        self.__webView.page().runJavaScript("latitude", print)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.getLatLonFromMap()
