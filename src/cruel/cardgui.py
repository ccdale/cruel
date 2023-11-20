#
# Copyright (c) 2023, Chris Allison
#
#     This file is part of cruel.
#
#     cruel is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     cruel is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with cruel.  If not, see <http://www.gnu.org/licenses/>.
#
import sys

import ccalogging
import PySimpleGUI as sg

# from cruel import errorExit, errorNotify, errorRaise, __appname__, __version__
from cruel import errorNotify, bgcolour, playingcards as pc

"""card gui module for the game Cruel."""

log = ccalogging.log


def cardElement(card, bordercolour=None, pad=(10, 10), key=None):
    try:
        elem = sg.Image(filename=card.getImage(), background_color=bgcolour)
        return sg.Column([[elem]], background_color=bordercolour, pad=pad)
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def gameWindow(cardpiles, foundations):
    """Create the game window. Run the game."""
    try:
        pass
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)
