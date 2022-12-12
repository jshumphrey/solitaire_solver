#! /usr/bin/env python
"""This code models, and solves, various kinds of card solitaires.
It is particularly focused on the card solitaire games bundled in with
the various games published by Zachtronics Interactive."""

import enum
import solitaire_enums as enums  # pylint: disable = unused-import

class Card:
    """A Card represents a single card in a game's deck."""

    def __init__(self, suit: enum.Enum, value: enum.Enum) -> None:
        self.suit = suit
        self.value = value
