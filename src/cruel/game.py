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

import ccalogging

from cruel import (
    __appname__,
    __version__,
    errorExit,
    cardgui as cg,
)

"""Cruel Card Game main module."""

log = ccalogging.log


def newGame():
    """Start a new game."""
    try:
        log.info(f"Starting new game of {__appname__} {__version__}")
        # define the card piles and the foundation (aces) piles
        cg.gameWindow()
        log.info(f"{__appname__} completed, Exiting.")
    except Exception as e:
        errorExit(sys.exc_info()[2], e)
