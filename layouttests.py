import sys

import PySimpleGUI as sg

from cruel import __appname__, __version__, errorNotify, log, playingcards as pc


def cardLayoutTest():
    try:
        # width of card: 100
        # height of card: 140
        # allowing for 8 pixels between cards
        # that is a padding of 4 pixels on each side
        # card area is 108 wide by 148 high
        # 6 cards across and 3 down
        # window size is 688 wide by 444 high
        #
        # that is a bit cramped
        # so, let's make the padding 10 pixels
        log.info("Starting cardLayoutTest")
        layout = []
        for row in range(3):
            rowLayout = []
            for col in range(6):
                cn = (row + 1) * 13 + col + 1
                card = pc.Card(cn)
                rowLayout.append(sg.Image(filename=card.getImage()))
            layout.append(rowLayout)
        window = sg.Window(
            __appname__ + " " + __version__, layout, finalize=True, size=(688, 444)
        )
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
        log.info("Ending cardLayoutTest")
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


def layoutTest():
    try:
        # use frames to hold the cards and columns to hold the frames
        # let pysimplegui handle the distance between cards
        log.info("Starting layoutTest")
        # eighteen cards
        deck = pc.Deck(pullaces=True)
        aceframes = [
            sg.Frame("", [[sg.Image(filename=card.getImage())]]) for card in deck.aces
        ]
        # cards = [pc.Card(i) for i in range(1, 19)]
        cards = deck.deal(19)
        frames = [
            sg.Frame("", [[sg.Image(filename=cards[i].getImage())]]) for i in range(12)
        ]
        row1 = [sg.Push()]
        row1.extend([f for f in aceframes])
        row1.append(sg.Push())
        clayout1 = [
            row1,
            # [sg.Column([[f for f in frames[:6]]])],
            [sg.Column([[f for f in frames[:6]]])],
            [sg.Column([[f for f in frames[6:]]])],
        ]
        clayout1.append(
            [sg.Push(), sg.Button("New Game"), sg.Button("Shuffle"), sg.Push()]
        )

        window = sg.Window(f"{__appname__} {__version__}", clayout1, finalize=True)
        while True:
            event, values = window.read()
            log.debug(f"{event=} {values=}")
            if event == sg.WIN_CLOSED:
                break

    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


if __name__ == "__main__":
    # cardLayoutTest()
    layoutTest()
