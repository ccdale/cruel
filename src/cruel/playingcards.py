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

from cruel import errorExit, errorNotify, errorRaise, __appname__, __version__, image

"""Playing cards module for the game Cruel."""

log = ccalogging.log


class CardName:
    def __init__(self, cardnumber):
        try:
            self.cardnumber = cardnumber
            self.value = self.cardnumber % 13
            self.suitindex = self.cardnumber // 13
            self.suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
            self.suit = self.suits[self.suitindex]
            self.hidename = False
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def valtuple(self):
        try:
            return (self.value, self.suit, self.cardnumber)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def __str__(self):
        try:
            cname = "Face Down" if self.hidename else f"{self.value} of {self.suit}"
            return cname
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def __repr__(self):
        try:
            cnum = "Face Down" if self.hidename else self.cardnumber
            return f"CardName({cnum})"
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)


class Card:
    def __init__(self, cardnumber, facedown=False, cardsize=(100, 140)):
        try:
            # log.debug(f"creating card {cardnumber=}, {facedown=}, {cardsize=}")
            self.cardname = CardName(cardnumber)
            self.facedown = facedown
            self.cardsize = cardsize
            self.value, self.suit, self.cardnumber = self.cardname.valtuple()
            self.image = image.cardImage(self.cardnumber)
            self.backimage = image.cardImage(0)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def __str__(self):
        try:
            return self.cardname.__str__()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def __repr__(self):
        try:
            cnum = "'Face Down'" if self.facedown else self.cardnumber
            return f"Card({cnum})"
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def flip(self):
        try:
            self.facedown = not self.facedown
            self.cardname.hidename = self.facedown
            return self.facedown
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def getImage(self):
        try:
            return self.backimage if self.facedown else self.image
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)


class Stack:
    def __init__(self, cards=None):
        try:
            self.cards = cards if isinstance(cards, Stack) else []
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def __repr__(self):
        try:
            return f"Stack({self.cards})"
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def __str__(self):
        try:
            return f"{self.cards}"
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def __len__(self):
        try:
            return len(self.cards)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def append(self, card):
        try:
            self.cards.append(card)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def pop(self):
        try:
            return self.cards.pop()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def clear(self):
        try:
            self.cards.clear()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def topCard(self):
        try:
            return self.cards.pop(0)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def bottomCard(self):
        try:
            return self.pop()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def showBottomCard(self):
        try:
            return self.cards[-1]
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def appendStack(self, stack):
        try:
            self.cards.extend(stack.cards)
            stack.clear()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)


class Deck(Stack):
    def __init__(self, pullaces=False, facedown=False):
        try:
            self.cards = [Card(i) for i in range(52)]
            if pullaces:
                self.cards = [card for card in self.cards if card.value != 0]
            [card.flip() for card in self.cards if facedown]
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def shuffle(self):
        try:
            shuffle(self.cards)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def deal(self, number=1):
        try:
            return [self.topCard() for i in range(number)]
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def dealStack(number=1):
        try:
            stack = Stack()
            stack.cards = self.deal(number)
            return stack
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)
