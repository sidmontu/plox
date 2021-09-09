#!/usr/bin/env python3
"""
Scanner implementation of the Lox programming language.
"""

from typing import List

import attr


@attr.s
class Scanner:
    """
    Scanner class that encapsulates all related methods.
    """

    def scan_tokens(self, src: str) -> List[str]:
        """
        Takes in input string as source and scans it for tokens.

        Args:

            src (str): String to scan for tokens.

        Returns:

            List[str]: list of tokens, where each token is a string.
        """

        # TODO: placeholder for now
        return list(src)
