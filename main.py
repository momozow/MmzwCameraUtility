#! /opt/local/bin/python3
# -*- coding: utf-8 -*-

import sys
import folderWatch
from PyQt5 import QtWidgets

list = folderWatch.getFileList(path = "/Volumes/Workspace", fileType = "PEF")

if list is not None:
    for file in list:
        print(file)

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
    
#     window = QtWidgets.QWidget()
#     window.show()
    
#     sys.exit(app.exec_())
