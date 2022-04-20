#!/usr/bin/env python3
"""
Contains the class declaration of Token.
"""

from dataclasses import dataclass
from typing import Any

from plox.config import TokenType


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class Token:
    """
    Token class to describe a token object that represents the different types
    of supported tokens in the Lox programming langauge.
    """

    token_type: TokenType
    lexeme: str
    literal: Any
    line: int

    def __str__(self):
        return f"{self.token_type} {self.lexeme} {self.literal}"
