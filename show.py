"""
Simple slide shower using eog.

TODO: would be nice if it did not give eog focus.
"""
import os
import time

from PIL import Image, ImageDraw

class SlideShow:

    def __init__(self):

        self.slides = []
        self.pos = 0
        self.wait = 5

    def interpret(self, msg):
        """ Create a slide show """
        
        for item in msg:
            self.slides.append(item)

    def add(self, slide):

        self.slides.append(slide)

    def next(self):

        self.show()

        self.pos += 1
        if self.pos >= len(self.slides):
            self.pos = 0

    def show(self):

        slide = self.slides[self.pos]
        image = slide.get('image')
        caption = slide.get('caption')

        if caption is None:
            # use image name, without the suffic
            caption = os.path.splitext(image)[0]

            # convert _ to ' '
            caption = caption.replace('_', ' ')
 
        # create image
        image_file = self.create_image(image, caption)
        
        os.system('eog -w %s &' % image_file)

        # fixme, need default time
        # find all slides with 
        wait = slide.get('time', self.wait)
        time.sleep(wait)

    def create_image(self, image_file, caption):
        """ Create an image with a caption """
        if image_file:
            img = Image.open(image_file)
        else:
            img = Image.new('RGB', (600, 400))

        name = self.add_caption(img, caption)

        return name

    def add_caption(self, image, caption):
        """ Add a caption to the image """

        width, height = image.size
        draw = ImageDraw.Draw(image)

        draw.text((int(width/10), int(height/20)), caption)

        name = "show/slide%d.png" % self.pos
        
        with open(name, 'w') as slide:
            image.save(name)

        print(name)
        return name

    def run(self):
        """ Run the show """

        while True:
            self.next()
        



    
