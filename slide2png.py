"""
Create slides for a slideshow

Each slide is a heading plus a list of rows.

Each row is a list of text strings or image names.

This uses PIL to create an image for each slide.
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
        self.padding = 10
        self.cache = 'show'
        self.font = ImageFont.truetype(FONT, FONTSIZE)

    def interpret(self, msg):
        """ Load input """
        slides = msg.get('slides', [])
        self.cache = msg.get('folder')
        self.gallery = msg.get('gallery', '..')

        with open(self.cache + '/slides.txt', 'w') as logfile:
            for slide in slides:
                image = self.layout(slide)

                continue
                
                heading = slide['heading']
                filename = self.cache_image(heading['text'],
                                            image)

                print('%s,%d' % (filename, slide.get('time', 0)),
                      file=logfile)
        return

    def layout(self, slide):
        """ Return layout information for slide """

        image = Image.new('RGB', (WIDTH, HEIGHT), 'black')
        draw = ImageDraw.Draw(image)

        self.vertical_layout(draw, slide)
        print(slide)
        
        self.horizontal_layout(draw, slide)

        image = self.draw_slide(draw, slide)

        return image

    def draw_slide(self, draw, slide):

        rows = slide['rows']

        for row in rows:
            for item in row['items']:
                print('tl', item['top'], item['left'])
                print('wh', item['width'], item['height'])

                print(item.get('text', ''))
                print(item.get('image', ''))
                      
            print()

    def vertical_layout(self, draw, slide):
        """ Augment slide with vertical layout info """
        padding = self.padding
        heading = slide['heading']

        width, height = draw.textsize(heading['text'], self.font)
        top = padding
        left = padding

        # Calculate size and location of heading
        heading.update(dict(
            width = width,
            height = height,
            top = self.padding,
            left = self.padding))

        top += height + padding

        # count how many rows just text and how many have image
        rows = slide['rows']
        text_rows = 0
        image_rows = 0

        # calculate size of all text objects
        total_height = top
        for row in rows:

            row_height = 0

            images = 0
            for item in row['items']:
                if item.get('image'):
                    images += 1

                text = item.get('text')
                
                if text is None: continue
                    
                width, height = draw.textsize(text, self.font)

                item.update(dict(
                    width = width,
                    height = height))

                row_height = max(row_height, height)
                

            if images:
                image_rows += 1
                row['images'] = images
            else:
                row['height'] = row_height
                text_rows += 1

            total_height += row_height + padding
                
        # Calculate average height for image rows
        if image_rows:
            
            available = HEIGHT - total_height

            image_height = available // image_rows

            image_text_offset = image_height // 2

        # now spin through rows again setting top
        # (and height for images)
        for row in rows:
            text_top = top
            
            images = row.get('images', 0)
            if images:
                text_top += image_text_offset

            for item in row['items']:
                if item.get('text'):
                    item['top'] = text_top
                else:
                    # image
                    item['top'] = top
                
            top += row.get('height', 0) + padding

        return

    def horizontal_layout(self, draw, slide):
        """ Augment slide with horizontal layout info """
        padding = self.padding
        heading = slide['heading']

        top = padding
        left = padding

        top += heading['height'] + padding

        rows = slide['rows']

        for row in rows:

            images = row.get('images', 0)

            items = row['items']
            
            widths = [x.get('width', 0) for x in items]

            available_width = (sum(widths) + 
                ((1 + len(widths)) * padding))

            if images:
                image_width = available_width // images

            # OK, now set left for all items and image_width for images
            left = padding
            for item in row['items']:

                if item.get('image'):
                    item['width'] = image_width

                item['left'] = left    

                left += item['width'] + padding

        return


    def get_image_height(self, draw, text_rows, image_rows):
        padding = self.padding

        # should probably just do this properly
        junk, t_height = draw.textsize('T')

        # space left for images
        image_height = HEIGHT - ((1 + text_rows) * (t_height + padding))

        image_height -= image_rows * padding

        image_height /= image_rows

        return image_height

    def row_counts(self, rows):
        
        text_rows = 0
        image_rows = 0

        for row in rows:
            text = False
            image = False

            for item in row:
                if 'text' in item:
                    text = True
                    
                if 'image' in item:
                    image = True
            if not image:
                text_rows += 1
                
            else:
                image_rows += 1

        return text_rows, image_rows

    def create_image(self, image_file, caption):
        """ Create an image with a caption """
        suffix = 'png'
        if image_file:
            img = Image.open(os.path.join(self.gallery, image_file))
            width, height = img.size
            ratio = width/WIDTH
            img = img.resize((int(width // ratio),
                              int(height // ratio)),
                             Image.ANTIALIAS)
        else:
            img = Image.new('RGB', (WIDTH, HEIGHT), 'black')
            image = self.add_caption(img, caption)
            
        image = img

        return image

    def slugify(self, name):
        """ Turn name into a slug suitable for an image file name """
        slug = ''
        for char in name.lower():
            if not char.isalnum():
                char = '_'

            slug += char

        return slug
    
    def cache_image(self, label, image):

        
        name = "%s/%s.png" % (self.cache, self.slugify(label))
        
        with open(name, 'w') as slide:
            image.save(name)

        return name


    def add_caption(self, image, caption, colour=None):
        """ Add a caption to the image """

        if colour is None:
            colour = "white"
    
        width, height = image.size
        draw = ImageDraw.Draw(image)

        draw.font = self.font

        draw.font = self.font
        draw.text((width // 10, height//20), caption,
                  fill=colour)

        return image


        



    
