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
from cruel.image import cardImage, invertedImage


class Card:
    def __init__(self, cardnumber, facedown=False, cardsize=(100, 140)):
        try:
            # log.debug(f"creating card {cardnumber=}, {facedown=}, {cardsize=}")
            self.cardname = CardName(cardnumber)
            self.facedown = facedown
            self.cardsize = cardsize
            self.value, self.suit, self.cardnumber = self.cardname.valtuple()
            self.image = cardImage(self.cardnumber, cardsize=self.cardsize)
            self.inverted = invertedImage(self.cardnumber, cardsize=self.cardsize)
            self.backimage = cardImage(0)
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
