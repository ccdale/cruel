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
    valueNames = [
        "Ace",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self, cardnumber):
        try:
            log.debug(f"creating CardName({cardnumber=})")
            self.cardnumber = cardnumber
            self.value = self.cardnumber % 13
            self.valuename = self.valueNames[self.value]
            self.suitindex = (self.cardnumber - 1) // 13
            log.debug(f"{self.suitindex=}")
            self.suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
            self.suit = self.suits[self.suitindex]
            self.hidename = False
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def valtuple(self):
        try:
            return (self.value, self.suit, self.cardnumber)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __str__(self):
        try:
            cname = "Face Down" if self.hidename else f"{self.valuename} of {self.suit}"
            return cname
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __repr__(self):
        try:
            cnum = "Face Down" if self.hidename else self.cardnumber
            return f"CardName({cnum})"
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)


class Card:
    def __init__(self, cardnumber, facedown=False, cardsize=(100, 140)):
        try:
            # log.debug(f"creating card {cardnumber=}, {facedown=}, {cardsize=}")
            self.cardname = CardName(cardnumber)
            self.facedown = facedown
            self.cardsize = cardsize
            self.value, self.suit, self.cardnumber = self.cardname.valtuple()
            self.image = image.cardImage(self.cardnumber, cardsize=self.cardsize)
            self.inverted = image.invertedImage(self.cardnumber, cardsize=self.cardsize)
            self.backimage = image.cardImage(0)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __str__(self):
        try:
            return self.cardname.__str__()
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __repr__(self):
        try:
            cnum = "'Face Down'" if self.facedown else self.cardnumber
            return f"Card({cnum})"
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def flip(self):
        try:
            self.facedown = not self.facedown
            self.cardname.hidename = self.facedown
            return self.facedown
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def getImage(self):
        try:
            return self.backimage if self.facedown else self.image
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)


class Stack:
    def __init__(self, cards=None):
        try:
            log.debug(f"creating Stack({cards=})")
            self.cards = cards if isinstance(cards, list) else []
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __repr__(self):
        try:
            return f"Stack({self.cards})"
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __str__(self):
        try:
            return f"{self.cards}"
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __len__(self):
        try:
            return len(self.cards)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def append(self, card):
        try:
            self.cards.append(card)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def pop(self, position=-1):
        try:
            return self.cards.pop(position)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def clear(self):
        try:
            self.cards.clear()
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def topCard(self):
        try:
            return self.pop(0)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def bottomCard(self):
        try:
            return self.pop()
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def showBottomCard(self):
        try:
            # log.debug(f"showBottomCard: {self.cards=}")
            if len(self.cards) > 0:
                return self.cards[-1]
            else:
                return None
        except Exception as e:
            # errorRaise(sys.exc_info()[2], e)
            errorRaise(sys.exc_info()[2], e)

    def show(self):
        try:
            return self.showBottomCard()
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def appendStack(self, stack):
        try:
            self.cards.extend(stack.cards)
            stack.clear()
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)


class Deck(Stack):
    def __init__(self, pullaces=False, facedown=False, cardsize=(100, 140)):
        try:
            log.debug(f"creating Deck({pullaces=}, {facedown=})")
            self.cards = [Card(i, cardsize=cardsize) for i in range(1, 53)]
            self.aces = None
            if pullaces:
                self.aces = []
                acepos = [i for i in range(0, 52, 13)]
                # we need to pull the aces in reverse order
                # as when we pop each of them off the deck
                # all the cards change position by 1
                acepos.reverse()
                for i in acepos:
                    self.aces.append(self.cards.pop(i))
                [card.flip() for card in self.aces if facedown]
            [card.flip() for card in self.cards if facedown]
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def shuffle(self):
        try:
            shuffle(self.cards)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def deal(self, number=1):
        try:
            number = min(number, len(self.cards))
            if number > 0:
                return [self.topCard() for i in range(number)]
            return []
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def dealStack(self, number=1):
        try:
            cards = self.deal(number)
            return Stack(cards)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)


class Pile:
    def __init__(self, stack, row, col):
        try:
            self.row = row
            self.col = col
            self.stack = stack
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)


def acesStacks():
    try:
        foundations = []
        aces = [Card(i) for i in range(0, 52, 13)]
        for i in range(4):
            stack = Stack()
            stack.append(aces[i])
            foundations.append(stack)
        return foundations
    except Exception as e:
        errorRaise(sys.exc_info()[2], e)


def cardStacks(deck=None):
    try:
        if deck is None:
            deck = Deck(pullaces=True, facedown=False)
            deck.shuffle()
        cardpiles = [deck.dealStack(4) for i in range(12)]
        return cardpiles
    except Exception as e:
        errorRaise(sys.exc_info()[2], e)
