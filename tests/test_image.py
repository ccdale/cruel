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
import os
from pathlib import Path

from PIL import Image

from cruel import __appname__, image


def test_getCardFile():
    expected = Path(image.imagepath / "1.png")
    assert image.getCardFile(1) == expected


def test_getWantedSize():
    expected = Path(image.cachepath / "100x140" / "1_100x140.png")
    assert image.getWantedSize(1) == expected


def test_cardImage():
    wanted = image.getWantedSize(1)
    im = image.cardImage(1)
    assert isinstance(im, type(Image.open(wanted)))
    assert im.size == (100, 140)
