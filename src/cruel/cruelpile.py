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

from cruel import errorRaise, image, log, playingcards as pc


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
            errorRaise(sys.exc_info()[2], e)

    def redraw(self):
        try:
            if len(self.cards) > 0:
                self.image = self.show().getImage()
            else:
                self.image = image.blankImage()
            self.doredraw = False
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def setCards(self, cardslist):
        try:
            self.cards = cardslist
            self.doredraw = True
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

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
            errorRaise(sys.exc_info()[2], e)

    def testAndAdd(self, card):
        """Test if a card can be added to the pile and add it if it can be"""
        try:
            if self.test(card):
                self.append(card)
                self.redraw()
                return True
            return False
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)
