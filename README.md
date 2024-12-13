# Mull It Over

_Advent of Code 2024, Day 3_

**Status**:

[![UNIX (macOS & Linux)](https://github.com/paanvaannd/aoc-2024.12.03/actions/workflows/run_tests.yaml/badge.svg)](https://github.com/paanvaannd/aoc-2024.12.03/actions/workflows/run_tests.yaml)

## Puzzle 1

Given a long string that contains a target string of a given pattern (i.e., "mul(<integer>, <integer>)") with other characters including letters, numbers, and symbols, find and extract all target strings in the input. Taking those extracted strings, multiply the integers that are part of the matched target string. For each input to the program, sum all products of the aforementioned multiplication operations and output this total sum.

## Puzzle 2

In each line of corrupted commands, there are switch statements (`do()` and `don't()`, specifically) that signal to the interpreting program whether the `mul()` commands that follow should or should not be interpreted, respectively. Subsequent calls to `do()` or `don't()` toggle the evaluation of subsequent `mul()` commands.
