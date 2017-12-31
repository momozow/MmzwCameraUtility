#! /opt/local/bin/python3
# -*- coding: utf-8 -*-

import sys
from folderWatch import FolderWatch
from ImageController import ImageController
from View import View
from PyQt5 import (QtWidgets, QtGui)

workSpace = "/Volumes/Workspace"
targetType = ["PEF", "jpg"]

folderWatch = FolderWatch()

list = folderWatch.getFileList(path = workSpace, targetType = targetType)

if list is not None:
    for file in list:
        print(file)

imageController = ImageController()
imageqt = imageController.readThumbnail(workSpace + "/image.PEF")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    view = View()
    view.showImage(imageqt)

    view.show()
    
    sys.exit(app.exec_())
