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

from cruel import errorRaise, log
from cruel.card import Card
from cruel.stack import Stack


class Deck(Stack):
    def __init__(
        self, pullaces=False, shuffleaces=True, facedown=False, cardsize=(100, 140)
    ):
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
                    self.aces.append(self.pop(i))
                if shuffleaces:
                    # randomise the order of the aces
                    shuffle(self.aces)
                [card.flip() for card in self.aces if facedown]
            [card.flip() for card in self.cards if facedown]
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def shuffle(self, times=1):
        try:
            for i in range(times):
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

    def undeal(self, cards):
        try:
            self.cards.extend(cards)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def dealStack(self, number=1):
        try:
            cards = self.deal(number)
            return Stack(cards)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)
