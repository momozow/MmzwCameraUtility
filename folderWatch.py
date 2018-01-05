import os
import re

class FolderWatch:
    @staticmethod
    def __extractTargetTypeFileFromList(list, targetFileType):
        indexesOfTargetFile = []
        for fileType in targetFileType:
            indexesOfTargetFile.extend(FolderWatch.__searchTargetType(list, fileType))

        targetTypeFileList = []
        # extract file target type from list
        for i in indexesOfTargetFile:
            targetTypeFileList.append(list[i])

        return targetTypeFileList

    @staticmethod
    def __searchTargetType(list, targetFileType):
        indexes = []
        
        for i in range(len(list)):
            searched = re.search(".(" + targetFileType.upper() + "|" + targetFileType.lower() + ")$", list[i])

            if searched:
                indexes.append(i)

        return indexes
        
    @staticmethod
    def getFileList(path, targetType = None):
        if not os.path.exists(path):
            print("Directory \"" + path + "\" is not exist.\n")
            return []

        list = os.listdir(path)

        if targetType is not None:
            list = FolderWatch.__extractTargetTypeFileFromList(list, targetType)
            
        return list

