#!/usr/bin/env python

# Import built-in libraries
import os
import re

# Type aliases
sanity = list[str]

# Globals
SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_ROOT = os.path.dirname(SCRIPT_PATH)
PROJECT_ROOT = os.path.dirname(SCRIPT_ROOT)


def read_data_file(filename: str) -> str:
    _data_file = os.path.join(PROJECT_ROOT, "data", filename)
    with open(_data_file, mode="r") as _file:
        return _file.read()


def please_do(gobbledygook: str) -> str:
    _segments = re.split(r"(?=do(?:n't)?\(\))", gobbledygook)
    _gobbledygook_sans_negatives = [_segment for _segment in _segments
                                    if _segment.startswith("do()")
                                    or _segment == _segments[0]]
    return "".join(_gobbledygook_sans_negatives)


def make_sense_of(gobbledygook: str) -> sanity:
    return re.findall(r"mul\(\d+,\d+\)", gobbledygook)


def extract_multiplicands(cmd: str) -> list[int]:
    return [int(multiplicand) for multiplicand in re.findall(r"\d+", cmd)]


def mul(first: int, second: int) -> int:
    return first * second


def sum_products(data: str) -> int:
    _cmds = make_sense_of(data)
    _products = [mul(*extract_multiplicands(_cmd)) for _cmd in _cmds]
    return sum(_products)


def main() -> None:
    _data = read_data_file("scrambled_cmds.txt").replace("\n", "")

    print("\nPart 1\n------")
    print(f"The sum of all mul() products is {sum_products(_data):,}.")

    print("\nPart 2\n------")
    _data_trimmed = please_do(_data)
    print(f"The sum of all toggled mul() products is {sum_products(_data_trimmed):,}.")


if __name__ == "__main__":
    main()
