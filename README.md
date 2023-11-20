# Cruel

A python implementation of the card game Cruel that originally came with
Windows. See this [wikipedia page](https://en.wikipedia.org/wiki/Cruel_(solitaire))
for the rules.

## Card Images

The card images are in the `images` directory. See the [LICENCE](images/LICENCE)
file for usage information.

## Card Caching

The card images are by default resized currently to 140 pixels high by 100
pixels wide. The size is set in an optional variable `cardsize` in the call to
the cardImage function in [image.py](src/cruel/image.py#63) as a tuple.

As each card is used it will be resized by the
[cardImage](src/cruel/image.py#63) method and stored in the cache directory
`~/.cache/cruel/{size}/`. This directory will be automatically created.

The intention is to have some form of dynamic sizing dependent on window size in
the future.

## Card Numbering

The image files are numbered from 1-52. The cards are in Ace - King order, with
the suits in Spades, Hearts, Diamonds and Clubs ordering.
