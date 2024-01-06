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
from cruel import playingcards as pc
from cruel.cardname import CardName


def test_CardName():
    cn = CardName(2)
    assert cn.cardnumber == 2
    assert cn.value == 2
    assert cn.suitindex == 0
    assert cn.suit == "Spades"
    assert cn.valtuple() == (2, "Spades", 2)
    assert repr(cn) == "CardName(2)"
    assert str(cn) == "Three of Spades"


def test_CardName_High_card():
    cn = CardName(51)
    assert cn.cardnumber == 51
    assert cn.value == 12
    assert cn.suitindex == 3
    assert cn.suit == "Clubs"
    assert cn.valtuple() == (12, "Clubs", 51)
    assert repr(cn) == "CardName(51)"
    assert str(cn) == "King of Clubs"
