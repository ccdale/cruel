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

from cruel import errorRaise, log
from cruel.cardname import CardName
from cruel.card import Card


class Stack:
    def __init__(self, cards=None):
        try:
            # log.debug(f"creating Stack({cards=})")
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
            if len(self.cards) == 0:
                return None
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
