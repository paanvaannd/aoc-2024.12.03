#!/usr/bin/env python

# Import built-in libraries
import re

# Import 3rd-party libraries
import pytest

# Import custom modules
from mull_it_over import mull_it_over as mull


@pytest.mark.parametrize(
    "gobbledygook, expected",
    (
        ("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
            ("mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)")),
    )
)
def test_make_sense_of(gobbledygook, expected) -> None:
    assert mull.make_sense_of(gobbledygook) == expected


@pytest.mark.parametrize(
    "cmd, expected",
    (
        ("mul(2,4)", (2, 4)),
        ("mul(5,5)", (5, 5)),
        ("mul(11,8)", (11, 8)),
        ("mul(8,5)", (8, 5)),
        ("mul(0,10)", (0, 10))
    )
)
def test_extract_multiplicands(cmd, expected) -> None:
    assert mull.extract_multiplicands(cmd) == expected
