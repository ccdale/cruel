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

from cruel import (
    errorExit,
    errorNotify,
    errorRaise,
    __appname__,
    __version__,
    image,
)
from cruel.cardname import CardName
from cruel.card import Card
from cruel.stack import Stack

"""Playing cards module for the game Cruel."""

log = ccalogging.log


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
