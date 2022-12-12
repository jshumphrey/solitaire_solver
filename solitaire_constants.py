#! /usr/bin/env python
"""This file provides various enums for quickly setting up the decks for various
different solitaire games."""

import enum

class StandardColor(enum.Enum):
    """The colors present in a standard 52-card deck of cards."""
    RED = "red"
    BLACK = "black"

class StandardSuit(enum.Enum):
    """The suits present in a standard 52-card deck of cards."""
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"

class StandardValue(enum.Enum):
    """The card values present in a standard 52-card deck of cards."""
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
