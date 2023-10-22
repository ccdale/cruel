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
from pathlib import Path
import sys

import ccalogging
from PIL import Image

from cruel import __appname__, __version__, errorExit, errorNotify, errorRaise

"""Cruel Card Game image module."""

log = ccalogging.log

# cardsize is a global variable in main.py
# so this file must be loaded from main.py, not used standalone

imagepath = Path(__file__).parent.parent / "images"


def getCardFile(cardnumber):
    try:
        cardfile = imagepath / f"{cardnumber}.png"
        if not cardfile.exists():
            raise Exception(f"Card image file {cardfile} does not exist")
        return cardfile
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def getWantedSize(cardnumber):
    try:
        return imagepath / f"{cardnumber}_{cardwidth}x{cardheight}.png"
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def cardImage(cardnumber):
    try:
        wanted = getWantedSize(cardnumber)
        if not wanted.exists():
            cardfile = getCardFile(cardnumber)
            with Image.open(cardfile) as cardimage:
                out = cardimage.resize(cardsize)
                outfile = imagepath / f"{cardnumber}_{cardwidth}x{cardheight}.png"
                out.save(outfile)
        else:
            out = Image.open(wanted)
        return out
    except Exception as e:
        errorExit(sys.exc_info()[2], e)
