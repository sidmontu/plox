#!/usr/bin/env python3
"""
Contains utility functions for handling and reporting errors.
"""


def report(line: int, where: str, message: str):
    """
    Prints error message to console.

    Args:

        line (int): line number where error occurred

        where (str): location where the error occurred

        message (str): error message for debugging clues

    Returns: None
    """

    print(f"[line {line}] Error {where}: {message}")
