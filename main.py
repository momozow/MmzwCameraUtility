#! /opt/local/bin/python3
# -*- coding: utf-8 -*-

import sys
from folderWatch import FolderWatch
from ImageController import ImageController
from View import View
from PyQt5 import (QtWidgets, QtGui)

workSpace = "/Volumes/Workspace/"
targetType = ["PEF", "jpg"]

folderWatch = FolderWatch()
fileList = folderWatch.getFileList(path = workSpace, targetType = targetType)

if __name__ == '__main__':
    app = View.createApp(sys.argv)
    
    view = View()
    view.setWorkSpace(workSpace)

    view.showList(fileList)
    view.show()
    
    sys.exit(app.exec_())
