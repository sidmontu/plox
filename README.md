# Plox

Plox is the Python implementation of the compiler for the Lox programming
language from Robert Nystrom's book called "Crafting Interpreters".

## Getting Started

The project is developed using [Poetry](https://python-poetry.org/). It uses
pre-commit hooks and popular automation tools to improve project management
(e.g. `black` for formatting, `mypy` for static type-checking, etc).

To install the poetry package as a virtual environment, run:

`$ poetry install`

When you first clone the repository to your local machine, you *must* install
the pre-commit hooks so that all the automation checks run on `git commit`. You
can do so by running:

`poetry run pre-commit install`

## Folder Organization

```
plox
│
└─── bin
│   │   Command-line binaries for running python code.
│
└─── plox
│   │   The main python source-code files for the Plox compiler implementation.
│
└─── tests
│   │   Unit-tests.
│   │
│   └─── artifacts
│       │   Test artifacts used by several unit-tests.
│
└─── examples
    │   Example Lox programs (.lox source code files)
```
