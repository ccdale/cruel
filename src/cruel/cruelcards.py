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

from cruel import (
    __appname__,
    __version__,
    bgcolour,
    errorExit,
    errorNotify,
    image,
    log,
    playingcards as pc,
    cruelpile as cp,
)

"""Game module for the game cruel."""


class CruelGame:
    """CruelGame class is the main class for drawing and playing the game Cruel."""

    def __init__(self, cardwidth=100, theme="DarkGreen4"):
        try:
            self.cardsize = (cardwidth, int(cardwidth * 1.4))
            padding = int(cardwidth * 0.1)
            self.padding = (padding, padding)
            sg.theme(theme)
            self.deck = pc.Deck(pullaces=True, facedown=False, cardsize=self.cardsize)
            self.acepiles = [
                cp.CruelPile(cn + 12, direction=1, cardslist=[ace])
                for cn, ace in enumerate(self.deck.aces)
            ]
            self.cardpiles = [
                cp.CruelPile(i, cardslist=self.deck.deal(4)) for i in range(12)
            ]
            self.doredraw = True
            self.selected = None
            self.window = None
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)


def cardElement(card, key, bordercolour=None, pad=(10, 10)):
    try:
        elem = sg.Image(
            filename=card.getImage(), background_color=bgcolour, key=key, pad=pad
        )
        # return sg.Column(
        # [[elem]], background_color=bordercolour, pad=pad, key=f"B {key}"
        # )
        return elem
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def setup():
    try:
        deck = pc.Deck(pullaces=True, facedown=False, cardsize=(150, 210))
        # aces = [pc.Card(i) for i in range(1, 52, 13)]
        log.debug(f"{deck.aces=}")
        # acepiles = []
        # for cn, ace in enumerate(aces):
        #     acepiles.append(cp.CruelPile(cn + 12, direction=1, cardslist=[ace]))
        acepiles = [
            cp.CruelPile(cn + 12, direction=1, cardslist=[ace])
            for cn, ace in enumerate(deck.aces)
        ]
        # deck.shuffle()
        clists = [deck.deal(4) for i in range(12)]
        log.debug(f"{clists=}")
        cardpiles = [cp.CruelPile(i, cardslist=clists[i]) for i in range(12)]
        return (deck, acepiles, cardpiles)
    except Exception as e:
        errorExit(sys.exc_info()[2], e)


def gameWindow():
    """Create the game window. Run the game."""
    try:
        sg.theme("DarkGreen4")
        deck, acepiles, cardpiles = setup()
        cardpileelements = [
            cardElement(c.showBottomCard(), f"L {c.id}") for c in cardpiles
        ]
        cn = len(cardpileelements)
        foundationelements = [
            cardElement(c.showBottomCard(), f"L {c.id}") for c in acepiles
        ]
        # blank = sg.Image(filename=image.blankImage(), background_color=bgcolour)
        # blankr = sg.Image(filename=image.blankImage(), background_color=bgcolour)
        rows = []
        # row = [blank]
        row = [sg.Push()]
        row.extend(foundationelements)
        row.append(sg.Push())
        # row.append(blankr)
        # rows.append([blank, foundationelements, blankr])
        rows.append(row)
        rows.append([cardpileelements[:6]])
        rows.append([cardpileelements[6:]])
        row = [
            sg.Button("New Game"),
            sg.Push(),
            sg.Button("Re-Deal"),
            sg.Push(),
            sg.Button("Quit"),
        ]
        layout = [rows[0], rows[1], rows[2], row]
        window = sg.Window(
            f"{__appname__} {__version__}",
            layout,
            finalize=True,
        )
        window.bind("<Control-q>", "CQHit")
        for id in range(16):
            window[f"L {id}"].bind("<ButtonRelease-1>", "")
        selected = None
        while True:
            event, values = window.read()
            log.debug(f"{event=} {values=}")
            if event == sg.WIN_CLOSED or event == "CQHit" or event == "Quit":
                break
            elif event == "New Game":
                pass
            elif event == "Re-Deal":
                pass
            elif event.startswith("L "):
                if selected is None:
                    id = int(event[2:])
                    # border = f"B {event}"
                    piles = cardpiles if id < 12 else acepiles
                    xid = id if id < 12 else id - 12
                    window[event].update(filename=piles[xid].showBottomCard().inverted)
                    # window[border].update(background_color="red")
                    selected = event
                else:
                    id = int(selected[2:])
                    # border = f"B {selected}"
                    piles = cardpiles if id < 12 else acepiles
                    xid = id if id < 12 else id - 12
                    window[selected].update(filename=piles[xid].showBottomCard().image)
                    # window[border].update(background_color=bgcolour)
                    selected = None
    except Exception as e:
        errorExit(sys.exc_info()[2], e)


if __name__ == "__main__":
    gameWindow()
