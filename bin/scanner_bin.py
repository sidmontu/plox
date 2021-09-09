#!/usr/bin/env python3
"""
Binary of the scanner implementation.
"""
from os.path import isfile
from typing import Optional

import typer
from loguru import logger

from plox.scanner import Scanner

app = typer.Typer()


@app.command()
def main(fpath: Optional[str] = None):
    """
    Run scanner from the cmdline.

    Args:

        fpath (str, optional): Path to lox file to evaluate. Default set to
        None. If no fpath is supplied, then the scanner executes in interactive
        mode.
    """

    # instantiate a Scanner object
    scanner = Scanner()

    if fpath:
        logger.info(f"Evaluating file {fpath}")
        if not isfile(fpath):
            logger.error("File not found.")
            return
        with open(fpath, "r") as fp:
            file_contents = fp.read()
        tokens = scanner.scan_tokens(file_contents)
        print(f"Tokens: {tokens}")
    else:
        logger.info("No file supplied, launching interactive mode:")
        print("plox scanner v0.1")
        print('Type "q();" to quit the prompt.')
        while True:
            print("> ", end="")
            line = input()
            if line in ["q();", "q()"]:
                break
            tokens = scanner.scan_tokens(line)
            print(f"Tokens: {tokens}")


def _main():
    """
    Dummy hidden function to get typer app working with poetry script cmd
    """
    app()
