"""
This one is going to read markdown.

For now, I am trying to read a talk outline and turn it into something
that will create a slideshow.

"""

import os
import sys
import json

import getopt

class Mark2Json:

    def __init__(self):

        pass

    def interpret(self, infile):
        """ Process a file of rest and return json """

        data = []

        for record in self.generate_records(infile):
            data.append(record)

        return json.dumps(data)

            
    def generate_records(self, infile):
        """ Process a file of rest and yield dictionaries """
        for line in infile:
            record = {}

            # any Markdown heading is just a caption, no image
            print(line)
            if line.startswith('#'):
                print(line)
                record['caption'] = line[1:].strip()
                yield record
                continue

            fields = line.split(',')

            # nothing there, carry on
            if not fields: continue

            image = fields[0].strip()

            if not image: continue

            record['image'] = image

            try:
                time = float(fields[1])
            except:
                time = 0

            record['time'] = time

            try:
                caption = fields[2].strip()
            except:
                caption = None

            if caption:
                record['caption'] = caption

            # yield it if we have anything
            if record:
                yield record


x = Mark2Json()

interpret = x.interpret
            

if __name__ == '__main__':

    mark2json = Mark2Json()

    print(mark2json.interpret(sys.stdin))

