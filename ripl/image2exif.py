
from PIL import Image, ExifTags

class Im2Exif:

    def interpret(self, msg, who=None):

        im = Image.open(msg)

        exif = im._getexif()

        result = {}
        for key, value in exif.items():
            result[ExifTags.TAGS.get(key, key)] = value

        return result
    
