#! /opt/local/bin/python3
# -*- coding: utf-8 -*-

import sys, os
from FolderWatch import FolderWatch
from ImageController import ImageController
from View import View

workSpace = "/Volumes/Workspace/"
targetType = ["PEF", "jpg", "svg"]

if __name__ == '__main__':
    sys.argv.append("--disable-web-security")
    
    app = View.createApp(sys.argv)
    
    view = View(os.path.dirname(os.path.abspath(__file__)), workSpace)

    fileList = FolderWatch.getFileList(path = view.getWorkSpace(), targetType = targetType)

    view.showList(fileList)
    view.show()
    
    sys.exit(app.exec_())
