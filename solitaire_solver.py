#! /usr/bin/env python
"""This code models, and solves, various kinds of card solitaires.
It is particularly focused on the card solitaire games bundled in with
the various games published by Zachtronics Interactive."""

import random
from collections.abc import Sequence
from enum import Enum

import solitaire_constants as constants  # pylint: disable = unused-import


class Card:
    """A Card represents a single card in a game's deck."""

    def __init__(self, suit: Enum, value: Enum) -> None:
        self.suit = suit
        self.value = value


class Deck:
    """A Deck represents the entire population of Cards used in a particular Game."""

    def __init__(self, suits: Sequence[Enum], values: Sequence[Enum]) -> None:
        self.suits = suits
        self.values = values
        self.cards = [Card(suit, value) for (suit, value) in zip(self.suits, self.values)]

    def deal(self):
        """Yield each card of the Deck in a random order."""
        shuffled_deck = random.sample(self.cards, k = len(self.cards))
        for card in shuffled_deck:
            yield card


class Pile:
    """A Pile represents a "slot" on a Board that can accept one-to-many Cards.
    This might be a regular "pile" of cards in the "normal play area" of the Board,
    it might be a "free cell" that allows the storage of a single card at once,
    or it might be an "output" pile used to move cards off the board as they are "cleared"."""


class Move:
    """A Move represents a single movement of a card (or stack of cards) to a new Pile."""


class Board:
    """A Board"""


class Game:
    """A Game consists of a deck of cards, a board to place them on, and
    a set of rules to govern which moves are considered valid."""

    def __init__(self, deck, board: Board) -> None:
        pass
