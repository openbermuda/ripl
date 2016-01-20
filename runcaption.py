"""  Run whatever I'm doing at the time

Stuff in here probably belongs elsewhere.
"""

# run script from galleries folder

# fixme, make it md2py 
import md2py
import caption
import show
import argv

folder = '.'
if argv[1:]:
    folder = argv[1]
    

mj = md2py

msg = open('../stories/talk.rst')

slides = mj.interpret(msg)

print(slides[:5])

ss = caption.SlideShow()
ss.interpret(dict(slides=slides, folder=folder))


