#!/usr/bin/env python

# Import built-in libraries
import os
import re

# Type aliases
sanity = tuple[str, ...]

# Globals
SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_ROOT = os.path.dirname(SCRIPT_PATH)
PROJECT_ROOT = os.path.dirname(SCRIPT_ROOT)


def read_data_file(filename: str) -> str:
    _data_file = os.path.join(PROJECT_ROOT, "data", filename)
    with open(_data_file, mode="r") as _file:
        return _file.read()


def parse_input(corpus: str) -> list[str]:
    return corpus.splitlines()


def make_sense_of(gobbledygook: str) -> sanity:
    return tuple(re.findall(r"mul\(\d+,\d+\)", gobbledygook))


def extract_multiplicands(cmd: str) -> tuple[int, ...]:
    return tuple(int(multiplicand)
                 for multiplicand in tuple(re.findall(r"\d+", cmd)))


def mul(first: int, second: int) -> int:
    return first * second


def sum_products(products: tuple[int, ...]) -> int:
    return sum(products)


def main() -> None:
    _corpus = read_data_file("scrambled_cmds.txt")
    _data = parse_input(_corpus)

    print("\nPart 1\n------")
    _cmds_per_line = tuple(make_sense_of(_line) for _line in _data)
    _products_per_line = tuple(tuple(mul(*extract_multiplicands(_cmd)) for _cmd in _line)
                               for _line in _cmds_per_line)
    _total_per_line = tuple(sum(_line) for _line in _products_per_line)
    print(f"The total number of safe reports is  {sum(_total_per_line):,}.")


if __name__ == "__main__":
    main()
