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
from random import shuffle
import sys

import ccalogging
import PySimpleGUI as sg

from cruel import (
    __appname__,
    __version__,
    bgcolour,
    errorExit,
    errorNotify,
    errorRaise,
    image,
)
from cruel import cardgui as cg, playingcards as pc

# from cruel.image import cardImage

"""Cruel Card Game main module."""

log = ccalogging.log


def customCol(elem, bordercolour="green", pad=(10, 10)):
    # use a pysimplegui column to hold the cards
    # then we can draw a border around the card
    try:
        return sg.Column([[elem]], background_color=bordercolour, pad=pad)
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def rowByRow():
    try:
        log.info("Starting rowByRow")
        aces = [pc.Card(i) for i in range(1, 53, 13)]
        shuffle(aces)
        aelems = [cg.cardElement(ace, bordercolour=bgcolour) for ace in aces]
        r2elems = [
            cg.cardElement(pc.Card(i), bordercolour=bgcolour) for i in range(2, 8)
        ]
        r3elems = [
            cg.cardElement(pc.Card(i), bordercolour=bgcolour) for i in range(15, 21)
        ]
        row1 = [aelems]
        row2 = [r2elems]
        row3 = [r3elems]
        layout = [row1, row2, row3]
        window = sg.Window(
            f"{__appname__} {__version__}",
            layout,
            finalize=True,
            background_color="green",
        )
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
        log.info("ending rowByRow")
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def ltest():
    try:
        log.info("Starting ltest")
        basecolours = ["red", "green", "blue", "yellow"]
        colours = basecolours.copy()
        [colours.extend(basecolours) for i in range(4)]
        # cards = [pc.Card(i) for i in range(0, 19)]
        # frames = [
        #     customCol(sg.Image(filename=cards[i].getImage()), bordercolour=colours[i])
        #     for i in range(1, 19)
        # ]
        frames = []
        for i in range(1, 19):
            # log.debug(f"{i=}, {cards[i]=}, {colours[i]=}")
            if i == 1 or i == 16:
                elem = sg.Text(
                    f"{i=}", background_color="green", expand_x=True, expand_y=True
                )
            else:
                card = pc.Card(i)
                # elem = sg.Image(filename=card.getImage(), background_color="green")
                elem = cg.cardElement(card, bordercolour=bgcolour)
            frames.append(customCol(elem, bordercolour=colours[i]))
        cols = []
        for i in range(0, 16, 3):
            col = sg.Column(
                [[frames[i]], [frames[i + 1]], [frames[i + 2]]],
                background_color="green",
            )
            cols.append(col)
        layout = [cols]
        window = sg.Window(
            f"{__appname__} {__version__}",
            layout,
            finalize=True,
            background_color="green",
        )
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
        log.info("Ending ltest")
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def test2():
    try:
        toprow = [
            sg.Frame(f"top row {i}", layout=[[]], bordercolour="green")
            for i in range(5)
        ]
        layout = [toprow]
        window = sg.Window(
            f"{__appname__} {__version__}",
            layout,
            finalize=True,
            background_color="green",
        )
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)
