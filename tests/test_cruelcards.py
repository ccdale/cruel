from cruel import cruelcards


def test_cruel_setup():
    deck, acepiles, cardpiles = cruelcards.setup()
    assert len(deck) == 0
    assert str(acepiles[2].cards[0]) == "Ace of Diamonds"
    assert len(cardpiles[8].cards) == 4
