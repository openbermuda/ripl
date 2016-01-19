"""  Run whatever I'm doing at the time

Stuff in here probably belongs elsewhere.
"""


# fixme, make it md2py 
import md2py

mj = md2py

msg = open('stories/talk.rst')

x = mj.interpret(msg)

print(x)
