from PIL import Image, ImageQt
from io import BytesIO

import subprocess

class Foundation:
    @staticmethod
    def run(cmd):
        return subprocess.run(cmd, stdout = subprocess.PIPE).stdout

class ImageController(Foundation):
    @staticmethod
    def __convertImageQt(binary, imageType = "RGBA"):
        image_PIL = Image.open(BytesIO(binary))
        image_PIL_RGBA = image_PIL.convert(imageType)
        return ImageQt.ImageQt(image_PIL_RGBA)
    
    @staticmethod
    def readThumbnail(file):
        data = Foundation.run(["exiftool", "-ThumbnailImage", "-b", file])
        imageQt = ImageController.__convertImageQt(data)
        
        return imageQt
