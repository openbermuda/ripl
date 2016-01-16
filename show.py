"""
Simple slide shower using eog.

TODO: would be nice if it did not give eog focus.
"""
import os
import time

class SlideShow:

    def __init__(self):

        self.slides = []
        self.pos = 0

    def add(self, slide):

        self.slides.append(slide)

    def next(self):

        self.show()

        self.pos += 1
        if self.pos >= len(self.slides):
            self.pos = 0

    def show(self):

        print(self.slides[self.pos])
        os.system('eog -w %s &' % self.slides[self.pos])
        time.sleep(10)


if __name__ == '__main__':        

    import sys

    show = SlideShow()

    for line in sys.stdin:

        filename = line.strip()
        if os.path.exists(filename):
            show.add(filename)

    while True:
        show.next()
        time.sleep(3)

    
