import sys

import ccalogging

from cruel import __appname__, __version__, errorExit, errorRaise, errorNotify

"""Cruel Card Game main module."""

ccalogging.setDebug()
# ccalogging.setInfo()
log = ccalogging.log

# fixed sizes of cards for now, maybe dynamic with window size later
cardsize = (100, 140)
cardwidth, cardheight = cardsize
