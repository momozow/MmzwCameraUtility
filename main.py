#! /opt/local/bin/python3
# -*- coding: utf-8 -*-

import sys
import folderWatch
from PyQt5 import QtWidgets

workSpace = "/Volumes/Workspace"
targetType = ["PEF", "jpg"]

folderWatch = folderWatch.FolderWatch()

list = folderWatch.getFileList(path = workSpace, targetType = targetType)

if list is not None:
    for file in list:
        print(file)

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
    
#     window = QtWidgets.QWidget()
#     window.show()
    
#     sys.exit(app.exec_())
