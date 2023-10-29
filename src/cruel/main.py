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

from cruel import __appname__, __version__, errorExit, errorNotify, errorRaise, image
from cruel import playingcards as pc

# from cruel.image import cardImage

"""Cruel Card Game main module."""

ccalogging.setDebug()
# ccalogging.setInfo()
log = ccalogging.log


def cardLayoutTest():
    try:
        # width of card: 100
        # height of card: 140
        # allowing for 8 pixels between cards
        # that is a padding of 4 pixels on each side
        # card area is 108 wide by 148 high
        # 6 cards across and 3 down
        # window size is 648 wide by 444 high
        log.info("Starting cardLayoutTest")
        layout = []
        for row in range(3):
            rowLayout = []
            for col in range(6):
                cn = row * 13 + col
                card = pc.Card(cn)
                rowLayout.append(sg.Image(data=card.getImage()))
            layout.append(rowLayout)
        window = sg.Window(
            __appname__ + " " + __version__, layout, finalize=True, size=(648, 444)
        )
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
        log.info("Ending cardLayoutTest")
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)
