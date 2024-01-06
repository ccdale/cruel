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

from cruel.cardname import CardName
from cruel.deck import Deck
from cruel.stack import Stack


def test_Stack_length():
    s = Stack()
    assert len(s) == 0


def test_Stack_append():
    s = Stack()
    s.append(CardName(2))
    assert len(s) == 1
    assert s.cards[0].cardnumber == 2
    assert repr(s.cards[0]) == "CardName(2)"
    assert repr(s) == "Stack([CardName(2)])"
    assert str(s) == "[CardName(2)]"


def test_Stack_clear():
    s = Stack()
    s.append(CardName(2))
    assert len(s) == 1
    s.clear()
    assert len(s) == 0


def test_Stack_pop():
    s = Stack()
    s.append(CardName(2))
    assert len(s) == 1
    assert s.pop().cardnumber == 2
    assert len(s) == 0


def test_Stack_pop_empty():
    s = Stack()
    assert len(s) == 0
    assert s.pop() is None
    assert len(s) == 0


def test_Stack_topCard():
    s = Stack()
    s.append(CardName(2))
    assert len(s) == 1
    assert s.topCard().cardnumber == 2
    assert len(s) == 0


def test_Stack_topCard_empty():
    s = Stack()
    assert len(s) == 0
    assert s.topCard() is None
    assert len(s) == 0


def test_Stack_bottomCard():
    s = Stack()
    s.append(CardName(2))
    assert len(s) == 1
    assert s.bottomCard().cardnumber == 2
    assert len(s) == 0


def test_Stack_bottomCard_empty():
    s = Stack()
    assert len(s) == 0
    assert s.bottomCard() is None
    assert len(s) == 0


def test_Stack_showBottomCard():
    d = Deck()
    c = d.showBottomCard()
    assert len(d) == 52
    assert c.cardnumber == 52
    assert str(c) == "Ace of Clubs"
    assert repr(c) == "Card(52)"
    assert c.facedown == False


def test_Stack_show_1st():
    s = Stack()
    s.append(CardName(2))
    assert len(s) == 1
    assert s.show().cardnumber == 2
    assert len(s) == 1


def test_Stack_show():
    d = Deck()
    c = d.show()
    assert len(d) == 52
    assert c.cardnumber == 52
    assert str(c) == "Ace of Clubs"
    assert repr(c) == "Card(52)"
    assert c.facedown == False


def test_Stack_show_empty():
    s = Stack()
    assert len(s) == 0
    assert s.show() is None
    assert len(s) == 0


def test_Stack_appendStack():
    s = Stack()
    s.append(CardName(2))
    s2 = Stack()
    s2.append(CardName(3))
    s.appendStack(s2)
    assert len(s) == 2
    assert len(s2) == 0
    assert s.cards[0].cardnumber == 2
    assert s.cards[1].cardnumber == 3
    assert repr(s.cards[0]) == "CardName(2)"
    assert repr(s.cards[1]) == "CardName(3)"
    assert repr(s) == "Stack([CardName(2), CardName(3)])"
    assert str(s) == "[CardName(2), CardName(3)]"
    assert repr(s2) == "Stack([])"
    assert str(s2) == "[]"
