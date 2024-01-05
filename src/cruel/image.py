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
import os
from pathlib import Path
import sys

import ccalogging
from PIL import Image, ImageOps

from cruel import __appname__, __version__, errorExit, errorNotify, errorRaise, log

"""Cruel Card Game image module."""


imagepath = Path(__file__).parent.parent.parent / "images"
log.debug(f"imagepath = {imagepath}")
cachepath = Path(os.path.expanduser("~/.cache")) / __appname__
log.debug(f"cachepath = {cachepath}")
if not cachepath.exists():
    log.debug(f"Creating cache directory {cachepath}")
    cachepath.mkdir(parents=True)
    log.info(f"Created cache directory {cachepath}")


def getCardFile(cardnumber):
    try:
        cardfile = imagepath / f"{cardnumber}.png"
        if not cardfile.exists():
            raise Exception(f"Card image file {cardfile} does not exist")
        return cardfile
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def getWantedSize(cardnumber, cardsize=(100, 140)):
    try:
        cardwidth, cardheight = cardsize
        sizepath = cachepath / f"{cardwidth}x{cardheight}"
        if not sizepath.exists():
            sizepath.mkdir(parents=True)
        cardpath = sizepath / f"{cardnumber}_{cardwidth}x{cardheight}.png"
        invertedpath = sizepath / f"{cardnumber}_inverted_{cardwidth}x{cardheight}.png"
        return cardpath, invertedpath
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def cardImage(cardnumber, cardsize=(100, 140)):
    try:
        wanted, inverted = getWantedSize(cardnumber, cardsize)
        if not wanted.exists():
            cardfile = getCardFile(cardnumber)
            with Image.open(cardfile) as cardimage:
                out = cardimage.resize(cardsize)
                out.save(wanted)
                invertedim = ImageOps.invert(out)
                invertedim.save(inverted)
                log.debug(f"Created card image {wanted} and inverted image {inverted}")
        return wanted
    except Exception as e:
        errorExit(sys.exc_info()[2], e)


def blankImage(cardsize=(100, 140)):
    try:
        cardwidth, cardheight = cardsize
        sizepath = cachepath / f"{cardwidth}x{cardheight}"
        if not sizepath.exists():
            sizepath.mkdir(parents=True)
        blankpath = sizepath / f"blank_{cardwidth}x{cardheight}.png"
        blankfile = imagepath / "blank.png"
        if not blankfile.exists():
            raise Exception(f"Blank image file {blankfile} does not exist")
        if not blankpath.exists():
            with Image.open(blankfile) as blankimage:
                out = blankimage.resize(cardsize)
                out.save(blankpath)
        return blankpath
    except Exception as e:
        errorExit(sys.exc_info()[2], e)
