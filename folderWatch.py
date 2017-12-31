import os
import re

class FolderWatch:
    def __extractTargetTypeFileFromList(self, list, targetFileType):
        indexesOfTargetFile = []
        for fileType in targetFileType:
            indexesOfTargetFile.extend(self.__searchTargetType(list, fileType))

        targetTypeFileList = []
        # extract file target type from list
        for i in indexesOfTargetFile:
            targetTypeFileList.append(list[i])

        return targetTypeFileList

    def __searchTargetType(self, list, targetFileType):
        indexes = []
        
        for i in range(len(list)):
            searched = re.search(".(" + targetFileType.upper() + "|" + targetFileType.lower() + ")$", list[i])

            if searched:
                indexes.append(i)

        return indexes
        

    def getFileList(self, path, targetType = None):
        if not os.path.exists(path):
            print("Directory \"" + path + "\" is not exist.\n")
            return []

        list = os.listdir(path)

        if targetType is not None:
            list = self.__extractTargetTypeFileFromList(list, targetType)
            
        return list

