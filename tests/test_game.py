from cruel import game, playingcards as pc


def test_acesStacks():
    aces = game.acesStacks()
    assert len(aces) == 4
    assert all([isinstance(stack, pc.Stack) for stack in aces])
    assert str(aces[0].showBottomCard()) == "Ace of Spades"
    assert str(aces[1].showBottomCard()) == "Ace of Hearts"
    assert str(aces[2].showBottomCard()) == "Ace of Diamonds"
    assert str(aces[3].showBottomCard()) == "Ace of Clubs"
    assert aces[3].cards[0].value == 0


def test_cardStacks():
    riggeddeck = pc.Deck(pullaces=True, facedown=False)
    stacks = game.cardStacks(riggeddeck)
    assert len(stacks) == 12
    assert len(stacks[0]) == 4
    assert len(stacks[11]) == 4
    assert all([isinstance(stack, pc.Stack) for stack in stacks])
    assert str(stacks[0].cards[0]) == "Two of Spades"
    assert stacks[0].cards[0].value not in [0, 13, 26, 39]
    assert stacks[8].showBottomCard().cardnumber not in [0, 13, 26, 39]
