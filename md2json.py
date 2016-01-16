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
        for line in infile:
            record = {}
            if line.startswith('#'):
                record['caption'] = line[1:].strip()

            if record:
                data.append(record)

        return json.dumps(data)


if __name__ == '__main__':

    mark2json = Mark2Json()

    print(mark2json.interpret(sys.stdin))

