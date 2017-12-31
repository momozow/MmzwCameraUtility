import os
import re

class FolderWatch:
    def __deleteFileNotTargetTypeFromList(self, list, targetFileType):
        indexesOfNotTargetFile = self.__searchFileNotTargetType(list, targetFileType)
        
        # delete file not target type from list
        for i in indexesOfNotTargetFile:
            del list[i]

        return list

    def __searchFileNotTargetType(self, list, targetFileType):
        indexes = []
        
        for i in range(len(list)):
            searched = re.search(".(" + targetFileType.upper() + "|" + targetFileType.lower() + ")$", list[i])

            if not searched:
                indexes.append(i)

        return indexes
        

    def getFileList(self, path, fileType = None):
        if not os.path.exists(path):
            print("Directory \"" + path + "\" is not exist.\n")
            return []

        list = os.listdir(path)

        if fileType is not None:
            list = self.__deleteFileNotTargetTypeFromList(list, fileType)
            
        return list

