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


def test_Stack_length():
    s = pc.Stack()
    assert len(s) == 0


def test_Stack_append():
    s = pc.Stack()
    s.append(CardName(2))
    assert len(s) == 1
    assert s.cards[0].cardnumber == 2
    assert repr(s.cards[0]) == "CardName(2)"
    assert repr(s) == "Stack([CardName(2)])"
    assert str(s) == "[CardName(2)]"


def test_Stack_clear():
    s = pc.Stack()
    s.append(CardName(2))
    assert len(s) == 1
    s.clear()
    assert len(s) == 0


def test_Stack_pop():
    s = pc.Stack()
    s.append(CardName(2))
    assert len(s) == 1
    assert s.pop().cardnumber == 2
    assert len(s) == 0


def test_Stack_pop_empty():
    s = pc.Stack()
    assert len(s) == 0
    assert s.pop() is None
    assert len(s) == 0


def test_Stack_topCard():
    s = pc.Stack()
    s.append(CardName(2))
    assert len(s) == 1
    assert s.topCard().cardnumber == 2
    assert len(s) == 0


def test_Stack_topCard_empty():
    s = pc.Stack()
    assert len(s) == 0
    assert s.topCard() is None
    assert len(s) == 0


def test_Stack_bottomCard():
    s = pc.Stack()
    s.append(CardName(2))
    assert len(s) == 1
    assert s.bottomCard().cardnumber == 2
    assert len(s) == 0


def test_Stack_bottomCard_empty():
    s = pc.Stack()
    assert len(s) == 0
    assert s.bottomCard() is None
    assert len(s) == 0


def test_Stack_showBottomCard():
    d = pc.Deck()
    c = d.showBottomCard()
    assert len(d) == 52
    assert c.cardnumber == 51
    assert str(c) == "King of Clubs"
    assert repr(c) == "Card(51)"
    assert c.facedown == False


def test_Stack_show_1st():
    s = pc.Stack()
    s.append(CardName(2))
    assert len(s) == 1
    assert s.show().cardnumber == 2
    assert len(s) == 1


def test_Stack_show():
    d = pc.Deck()
    c = d.show()
    assert len(d) == 52
    assert c.cardnumber == 51
    assert str(c) == "King of Clubs"
    assert repr(c) == "Card(51)"
    assert c.facedown == False


def test_Stack_show_empty():
    s = pc.Stack()
    assert len(s) == 0
    assert s.show() is None
    assert len(s) == 0


def test_Stack_appendStack():
    s = pc.Stack()
    s.append(CardName(2))
    s2 = pc.Stack()
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


def test_Deck():
    d = pc.Deck()
    c = d.deal()
    assert len(d) == 51
    assert c[0].cardnumber == 0


def test_Deck_noAces():
    d = pc.Deck(pullaces=True)
    assert len(d) == 48
    c = d.deal()
    assert c[0].cardnumber == 1


def test_Deck_faceDown():
    d = pc.Deck(facedown=True)
    assert len(d) == 52
    c = d.deal()
    assert str(c[0]) == "Face Down"
    assert c[0].facedown == True
    assert repr(c[0]) == "Card('Face Down')"


def test_Deck_faceDown_noAces():
    d = pc.Deck(pullaces=True, facedown=True)
    assert len(d) == 48
    c = d.deal()
    assert str(c[0]) == "Face Down"
    assert c[0].facedown == True
    assert repr(c[0]) == "Card('Face Down')"


def test_acesStacks():
    aces = pc.acesStacks()
    assert len(aces) == 4
    assert all([isinstance(stack, pc.Stack) for stack in aces])
    assert str(aces[0].showBottomCard()) == "Ace of Spades"
    assert str(aces[1].showBottomCard()) == "Ace of Hearts"
    assert str(aces[2].showBottomCard()) == "Ace of Diamonds"
    assert str(aces[3].showBottomCard()) == "Ace of Clubs"
    assert aces[3].cards[0].value == 0


def test_cardStacks():
    riggeddeck = pc.Deck(pullaces=True, facedown=False)
    stacks = pc.cardStacks(riggeddeck)
    assert len(stacks) == 12
    assert len(stacks[0]) == 4
    assert len(stacks[11]) == 4
    assert all([isinstance(stack, pc.Stack) for stack in stacks])
    assert str(stacks[0].cards[0]) == "Two of Spades"
    assert stacks[0].cards[0].value not in [0, 13, 26, 39]
    assert stacks[8].showBottomCard().cardnumber not in [0, 13, 26, 39]
