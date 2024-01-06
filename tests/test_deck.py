from cruel.deck import Deck


def test_Deck():
    d = Deck()
    c = d.deal()
    assert len(d) == 51
    assert c[0].cardnumber == 1


def test_Deck_noAces():
    d = Deck(pullaces=True)
    assert len(d) == 48
    c = d.deal()
    assert c[0].cardnumber == 2


def test_Deck_faceDown():
    d = Deck(facedown=True)
    assert len(d) == 52
    c = d.deal()
    assert str(c[0]) == "Face Down"
    assert c[0].facedown == True
    assert repr(c[0]) == "Card('Face Down')"


def test_Deck_faceDown_noAces():
    d = Deck(pullaces=True, facedown=True)
    assert len(d) == 48
    c = d.deal()
    assert str(c[0]) == "Face Down"
    assert c[0].facedown == True
    assert repr(c[0]) == "Card('Face Down')"
