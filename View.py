from PyQt5 import (QtWidgets, QtGui)

class View(QtWidgets.QWidget):
    @staticmethod
    def createApp(argv):
        return QtWidgets.QApplication(argv)

    def __init__(self):
        super().__init__()

        self.__imageLabel = QtWidgets.QLabel()
        self.__listWidget = QtWidgets.QListWidget()
        
        self.__layout()
        
    def __layout(self):
        self.__listWidget.resize(120, 240)
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.__imageLabel)
        vbox.addWidget(self.__listWidget)
        
        self.setLayout(vbox)
       
    def showImage(self, imageqt):
        pixmap = QtGui.QPixmap.fromImage(imageqt)
        
        self.__imageLabel.setPixmap(pixmap)

    def showList(self, fileList):
        for fileName in fileList:
            item = QtWidgets.QListWidgetItem()
            item.setText(fileName)
            
            self.__listWidget.addItem(item)
