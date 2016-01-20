"""  Run whatever I'm doing at the time

Stuff in here probably belongs elsewhere.
"""

# run script from galleries folder
import sys

# fixme, make it md2py 
import md2py
import show

folder = '.'
if len(sys.argv) > 1:
    folder = sys.argv[1]

mj = md2py

msg = open('show/slides.txt')

slides = mj.interpret(msg)

print(slides[:5])

ss = show.SlideShow()

ss.interpret(dict(slides=slides, captions=folder))

ss.set_duration(30)

print('wait:', ss.wait)

ss.run()
