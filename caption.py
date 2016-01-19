"""
Create slides for a slideshow

TODO: would be nice if it did not give eog focus.
"""
import os
import time

from PIL import Image, ImageDraw

class SlideShow:

    def __init__(self):

        self.pos = 0
        self.cache = 'show'

    def interpret(self, msg):
        """ Load input """

        with open(self.cache + '/slides.txt', 'w') as logfile:
            for ix, item in enumerate(msg):
                image = self.prepare_image(item)
                filename = self.cache_image(image, ix)
                print('%s,%d' % (filename, item.get('time', 0)), file=logfile)

    def prepare_image(self, slide):

        image = slide.get('image')
        caption = slide.get('caption')

        if caption is None:
            # use image name, without the suffic
            caption = os.path.splitext(image)[0]

            # convert _ to ' '
            caption = caption.replace('_', ' ')
 
        # create image
        image_file = self.create_image(image, caption)

        return image_file

    def create_image(self, image_file, caption):
        """ Create an image with a caption """
        suffix = 'png'
        if image_file:
            img = Image.open(image_file)
        else:
            img = Image.new('RGB', (600, 400))

        image = self.add_caption(img, caption)

        return image


    def cache_image(self, image, ix):

        name = "%s/slide%d.png" % (self.cache, ix)
        
        with open(name, 'w') as slide:
            image.save(name)

        return name


    def add_caption(self, image, caption):
        """ Add a caption to the image """

        width, height = image.size
        draw = ImageDraw.Draw(image)

        draw.text((int(width/10), int(height/20)), caption)

        return image


        



    
