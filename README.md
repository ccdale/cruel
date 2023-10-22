# Cruel

A python implementation of the card game Cruel that I originally saw with
Windows for Workgroups 3.11.

## Card Images

The card images are in the `images` directory. See the [LICENCE](images/LICENCE)
file for usage information.

## Card Caching

The card images are resized currently resized to 140 pixels high by 100 pixels
wide. The size is set in a global variable `cardsize` in
[main.py](src/cruel/main.py#33) as a tuple, with 2 other convenience globals of
`cardheight` and `cardwidth`. This requires that all modules that use sizing are
called from [main.py](src/cruel/main.py) and not accessed stand-alone.

As each card is used it will be resized by the
[cardImage](src/cruel/image.py#61) method and stored in the cache directory
`~/.cache/cruel/{size}/`. This directory will be automatically created.

The intention is to have some form of dynamic sizing dependent on window size in
the future.

## Card Numbering

The image files are numbered from 1-52. The cards are in Ace - King order, with
the suits in Spades, Hearts, Diamonds and Clubs ordering.
