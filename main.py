#! /opt/local/bin/python3
# -*- coding: utf-8 -*-

import sys
from folderWatch import FolderWatch
from ImageController import ImageController
from View import View
from PyQt5 import (QtWidgets, QtGui)

workSpace = "/Volumes/Workspace/"
targetType = ["PEF", "jpg", "svg"]

if __name__ == '__main__':
    app = View.createApp(sys.argv)
    
    view = View()
    view.setWorkSpace(workSpace)

    folderWatch = FolderWatch()
    fileList = folderWatch.getFileList(path = view.getWorkSpace(), targetType = targetType)

    view.showList(fileList)
    view.show()
    
    sys.exit(app.exec_())
