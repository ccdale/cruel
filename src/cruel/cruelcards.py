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
)

"""Game module for the game cruel."""


class CruelPile(pc.Stack):
    """CruelPile class is a subclass of Stack for the game Cruel."""

    def __init__(self, pileid, direction=-1, cardslist=None):
        """Initialise the CruelPile class.
        pileid is an integer to form the key for pysimplegui columns
        direction argument shows which direction the cards are placed on the pile.
        -1 is down, 1 is up.
        This argument is directly used to test the validity of a card move.
        cardslist argument is a list of cards to be placed on the pile.
        """
        try:
            super().__init__()
            self.id = pileid
            self.key = f"pile{self.id}"
            self.direction = direction
            self.image = image.blankImage()
            self.doredraw = True
            if cardslist is not None:
                self.setCards(cardslist)
            if self.doredraw:
                self.redraw()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def redraw(self):
        try:
            if len(self.cards) > 0:
                self.image = self.show().getImage()
            else:
                self.image = image.blankImage()
            self.doredraw = False
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def setCards(self, cardslist):
        try:
            self.cards = cardslist
            self.doredraw = True
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def test(self, card):
        """Test if a card can be added to the pile"""
        try:
            log.debug(f"test: {len(self)=}")
            if len(self):
                expected = self.show().cardnumber + self.direction
                log.debug(f"test: {expected=}")
                log.debug(f"test: {card.cardnumber=}")
                if card.cardnumber == expected:
                    log.debug("test: True")
                    return True
            log.debug("test: False")
            return False
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def testAndAdd(self, card):
        """Test if a card can be added to the pile and add it if it can be"""
        try:
            if self.test(card):
                self.append(card)
                self.redraw()
                return True
            return False
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)


def cardElement(card, bordercolour=None, pad=(10, 10), key=None):
    try:
        elem = sg.Image(filename=card.getImage(), background_color=bgcolour, key=key)
        return sg.Column([[elem]], background_color=bordercolour, pad=pad)
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def setup():
    try:
        deck = pc.Deck(pullaces=True, facedown=False)
        # aces = [pc.Card(i) for i in range(1, 52, 13)]
        log.debug(f"{deck.aces=}")
        # acepiles = []
        # for cn, ace in enumerate(aces):
        #     acepiles.append(CruelPile(cn + 12, direction=1, cardslist=[ace]))
        acepiles = [
            CruelPile(cn + 12, direction=1, cardslist=[ace])
            for cn, ace in enumerate(deck.aces)
        ]
        # deck.shuffle()
        clists = [deck.deal(4) for i in range(12)]
        log.debug(f"{clists=}")
        cardpiles = [CruelPile(i, cardslist=clists[i]) for i in range(12)]
        return (deck, acepiles, cardpiles)
    except Exception as e:
        errorExit(sys.exc_info()[2], e)


def gameWindow():
    """Create the game window. Run the game."""
    try:
        deck, acepiles, cardpiles = setup()
        cardpileelements = [
            cardElement(c.showBottomCard(), key=f"L {c.id}") for c in cardpiles
        ]
        cn = len(cardpileelements)
        foundationelements = [
            cardElement(c.showBottomCard(), key=f"A {c.id}")
            # cardElement(a.showBottomCard(), key=f"A{cn + acn}")
            for c in acepiles
            # for acn, a in enumerate(acepiles)
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
            background_color="green",
        )
        window.bind("<Control-q>", "CQHit")
        while True:
            event, values = window.read()
            log.debug(f"{event=} {values=}")
            if event == sg.WIN_CLOSED or event == "CQHit" or event == "Quit":
                break
    except Exception as e:
        errorExit(sys.exc_info()[2], e)


if __name__ == "__main__":
    gameWindow()
