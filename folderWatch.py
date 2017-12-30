import os
import re

def getFileList(*, path, fileType = None):
    if not os.path.exists(path):
        print("Directory \"" + path + "\" is not exist.\n")
        return []
    
    list = os.listdir(path)

    if fileType is not None:
        indexOfNotTargetFileType = []

        # search file not target type
        for i in range(len(list)):
            searched = re.search(".(" + fileType.upper() + "|" + fileType.lower() + ")$", list[i])
            if searched:
                indexOfNotTargetFileType.append(i)

        # delete file not target type from list
        for i in indexOfNotTargetFileType:
            del list[i]
        
    return list
