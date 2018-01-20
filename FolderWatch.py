import os
import re

class FolderWatch:
    @staticmethod
    def getFileList(path, targetType = None):
        if not os.path.exists(path):
            print("Directory \"" + path + "\" is not exist.\n")
            return []

        fileList = os.listdir(path)
            
        return fileList
