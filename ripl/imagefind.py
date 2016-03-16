"""
Take a python object and turn it into json.

World's simplest interpreter.
"""
from numpy.random import randint

class ImageFind:

    def __init__(self):

        self.folders = set()
        self.images = []

        self.exts = ['gif', 'png', 'jpg']

    def add_folder(self, folder):
        """ Add a folder scan images there """
        if folder in self.folders:
            return

        self.folders.add(folder)
        
        for subfolder, junk, filenames in os.walk(folder):
            for filename in filenames:
                name, ext = os.path.split(filename)
                if ext in self.exts:
                    self.images.append(
                        os.path.join(subfolder, filename))
                
        

    def interpret(self, msg):
        """ Try and find the image file 

        some magic here would be good.

        FIXME move elsewhere and make so everyone can use.

        interpreter that finds things?
        """
        for gallery in msg.get('galleries', []):
            self.add_folder(gallery)
            
        image_file = msg['image']
        if not image_file: return

        return self.find_image(image_file)

    def find_image(self, image_file):
        
        matches = []
        partials = []
        for image in self.images:
            if image.endswith(image_file):
                matches.append(image)
                continue

            if image_file in image:
                partials.append(image)

        if matches:
            return matches[randint(len(matches))]

        if partials:
            return partials[randint(len(partials))]
                
        return None


x = ImageFind()

interpret = x.interpret
