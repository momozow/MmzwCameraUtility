from PIL import Image, ImageQt
from io import BytesIO

import subprocess

class Foundation:
    def run(self, cmd):
        return subprocess.run(cmd, stdout = subprocess.PIPE).stdout

class ImageController(Foundation):
    def __convertImageQt(self, binary, imageType = "RGBA"):
        image_PIL = Image.open(BytesIO(binary))
        image_PIL_RGBA = image_PIL.convert(imageType)
        return ImageQt.ImageQt(image_PIL_RGBA)
    
    def readThumbnail(self, file):
        data = super().run(["exiftool", "-ThumbnailImage", "-b", file])
        imageQt = self.__convertImageQt(data)
        
        return imageQt
