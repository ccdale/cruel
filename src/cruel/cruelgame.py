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

import PySimpleGUI as sg

from cruel import __appname__, __version__, errorRaise, log, cruelpile as cp
from cruel.deck import Deck


class CruelGame:
    """CruelGame class is the main class for drawing and playing the game Cruel."""

    def __init__(self, cardwidth=100, theme="DarkGreen4"):
        try:
            self.cardsize = (cardwidth, int(cardwidth * 1.4))
            padding = int(cardwidth * 0.1)
            self.padding = (padding, padding)
            sg.theme(theme)
            self.doredraw = True
            self.selected = None
            self.window = None
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def setupGame(self):
        try:
            self.deck = Deck(pullaces=True, facedown=False, cardsize=self.cardsize)
            self.acepiles = [
                cp.CruelPile(
                    cn + 12, direction=1, cardslist=[ace], padding=self.padding
                )
                for cn, ace in enumerate(self.deck.aces)
            ]
            self.cardpiles = [
                cp.CruelPile(i, cardslist=self.deck.deal(4), padding=self.padding)
                for i in range(12)
            ]
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def gameWindow(self):
        try:
            foundationelems = [c.getElem() for c in self.acepiles]
            foundationelems.insert(0, sg.Push())
            foundationelems.append(sg.Push())
            layoutelems = [c.getElem() for c in self.cardpiles]
            layout = []
            layout.append(foundationelems)
            layout.append(layoutelems[:6])
            layout.append(layoutelems[6:])
            row = [
                sg.Button("New Game"),
                sg.Push(),
                sg.Button("Deal"),
                sg.Push(),
                sg.Button("Quit"),
            ]
            layout.append(row)
            self.window = sg.Window(
                f"{__appname__} {__version__}", layout, finalize=True
            )
            self.window.bind("<Control-q>", "CQquit")
            for id in range(16):
                self.window[f"L {id}"].bind("<ButtonRelease-1>", "")
            self.selected = None
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def gameLoop(self):
        try:
            while True:
                event, values = self.window.read()
                log.debug(f"{event=} {values=}")
                if event == sg.WIN_CLOSED or event == "CQquit" or event == "Quit":
                    break
                elif event == "New Game":
                    pass
                elif event == "Re-Deal":
                    pass
                elif event.startswith("L "):
                    if self.selected is None:
                        id = int(event[2:])
                        piles = self.cardpiles if id < 12 else self.acepiles
                        xid = id if id < 12 else id - 12
                        self.window[event].update(filename=piles[xid].show().inverted)
                        self.selected = event
                    else:
                        id = int(selected[2:])
                        piles = self.cardpiles if id < 12 else self.acepiles
                        xid = id if id < 12 else id - 12
                        self.window[self.selected].update(
                            filename=piles[xid].show().image
                        )
                        self.selected = None
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)


def main():
    try:
        cg = CruelGame()
        cg.setupGame()
        cg.gameWindow()
        cg.gameLoop()
    except Exception as e:
        errorRaise(sys.exc_info()[2], e)


if __name__ == "__main__":
    main()
