from cruel import game, playingcards as pc


def test_acesStacks():
    aces = game.acesStacks()
    assert len(aces) == 4
    assert all([isinstance(stack, pc.Stack) for stack in aces])
    assert str(aces[0].showBottomCard()) == "Ace of Spades"
    assert aces[0].showBottomCard().value == 1
    assert aces[0].showBottomCard().cardnumber == 1
    assert aces[0].showBottomCard().suit == "Spades"
    assert aces[1].showBottomCard().value == 1
    assert aces[1].showBottomCard().cardnumber == 14
    assert aces[1].showBottomCard().suit == "Hearts"
    assert aces[2].showBottomCard().value == 1
    assert aces[2].showBottomCard().cardnumber == 27
    assert aces[2].showBottomCard().suit == "Diamonds"
    assert aces[3].showBottomCard().value == 1
    assert aces[3].showBottomCard().cardnumber == 40
    assert aces[3].showBottomCard().suit == "Clubs"
    assert aces[3].cards[0].value == 1


def test_cardStacks():
    riggeddeck = pc.Deck(pullaces=True, facedown=False)
    stacks = game.cardsStacks(riggeddeck)
    assert len(stacks) == 12
    assert len(stacks[0]) == 4
    assert len(stacks[11]) == 4
    assert all([isinstance(stack, pc.Stack) for stack in stacks])
    assert str(stacks[0].cards[0]) == "Two of Spades"
    assert stacks[0].cards[0].value not in [0, 13, 26, 39]
    assert stacks[8].showBottomCard().cardnumber not in [0, 13, 26, 39]
