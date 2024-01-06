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

from cruel import errorRaise, log, playingcards as pc, cruelpile as cp


class CruelGame:
    """CruelGame class is the main class for drawing and playing the game Cruel."""

    def __init__(self, cardwidth=100, theme="DarkGreen4"):
        try:
            self.cardsize = (cardwidth, int(cardwidth * 1.4))
            padding = int(cardwidth * 0.1)
            self.padding = (padding, padding)
            sg.theme(theme)
            self.deck = pc.Deck(pullaces=True, facedown=False, cardsize=self.cardsize)
            self.acepiles = [
                cp.CruelPile(cn + 12, direction=1, cardslist=[ace])
                for cn, ace in enumerate(self.deck.aces)
            ]
            self.cardpiles = [
                cp.CruelPile(i, cardslist=self.deck.deal(4)) for i in range(12)
            ]
            self.doredraw = True
            self.selected = None
            self.window = None
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)
