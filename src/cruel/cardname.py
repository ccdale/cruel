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
