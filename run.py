"""  Run whatever I'm doing at the time

Stuff in here probably belongs elsewhere.
"""

# run script from galleries folder

# fixme, make it md2py 
import md2py
import show

mj = md2py

msg = open('../stories/talk.rst')

slides = mj.interpret(msg)

print(slides[:5])

ss = show.SlideShow()

ss.interpret(slides)

ss.run()
