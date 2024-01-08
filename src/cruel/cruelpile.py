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

import PySimpleGUI as sg

from cruel import errorRaise, log
from cruel.image import blankImage
from cruel.stack import Stack


class CruelPile(Stack):
    """CruelPile class is a subclass of Stack for the game Cruel."""

    def __init__(self, pileid, direction=-1, cardslist=None, padding=(1, 1)):
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
            self.key = f"L {self.id}"
            self.tkey = f"T {self.id}"
            self.direction = direction
            self.image = blankImage()
            # self.doredraw = True
            self.elem = None
            self.padding = padding
            self.selected = False
            if cardslist is not None:
                self.setCards(cardslist)
            # if self.doredraw:
            #     self.redraw()
            self.createElement()
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def redraw(self, window):
        try:
            # log.debug(f"pile redraw: {self.id=} {len(self)=} {self.cards=}")
            if len(self) > 0:
                self.image = (
                    self.show().image if not self.selected else self.show().inverted
                )
            else:
                self.image = blankImage()
            window[self.key].update(filename=self.image)
            # self.doredraw = False
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def setCards(self, cardslist, window):
        try:
            # log.debug(f"setCards: {self.id=} {len(cardslist)=} {self.cards=} {cardslist=}")
            self.cards = cardslist
            self.redraw(window)
            # log.debug(f"setCards: {self.id=} {len(cardslist)=} {self.cards=}")
            # self.image = self.show().image
            # self.doredraw = True
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def createElement(self):
        try:
            self.elem = sg.Image(filename=self.image, key=self.key, pad=self.padding)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def getElem(self):
        try:
            return self.elem
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def test(self, card):
        """Test if a card can be added to the pile"""
        try:
            # log.debug(f"test: {len(self)=}")
            if len(self):
                expected = self.show().cardnumber + self.direction
                # log.debug(f"test: {expected=}")
                # log.debug(f"test: {card.cardnumber=}")
                if card.cardnumber == expected:
                    log.debug("test: True")
                    return True
            # log.debug("test: False")
            return False
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def testAndAdd(self, card, window):
        """Test if a card can be added to the pile and add it if it can be"""
        try:
            if self.test(card):
                self.append(card)
                self.redraw(window)
                return True
            return False
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)
