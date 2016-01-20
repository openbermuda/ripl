"""
Create slides for a slideshow

TODO: would be nice if it did not give eog focus.
"""
import os

from PIL import Image, ImageDraw, ImageFont

FONT = '/usr/share/fonts/TTF/Vera.ttf'
FONTSIZE = 36
WIDTH = 1024
HEIGHT = 768

class SlideShow:

    def __init__(self):

        self.pos = 0
        self.cache = 'show'
        self.font = ImageFont.truetype(FONT, FONTSIZE)

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
            width, height = img.size
            ratio = width/WIDTH
            img = img.resize((int(width // ratio),
                              int(height // ratio)),
                             Image.ANTIALIAS)
        else:
            img = Image.new('RGB', (WIDTH, HEIGHT), (255,255,255))

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

        draw.font = self.font

        draw.font = self.font
        draw.text((width // 10, height//20), caption, fill=(0,0,0))

        return image


        



    
