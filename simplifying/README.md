# Simplifying

[Kata on CodeWars](https://www.codewars.com/kata/57f2b753e3b78621da0020e8)

## Description

You are given a list/array of example equalities such as:

    [ "a + a = b", "b - d = c ", "a + b = d" ]

Use this information to solve a given formula in terms of the remaining symbol such as:

    formula = "c + a + b"

In this example:

    "c + a + b" = "2a"

so the output is "2a".

### Notes

* Variables names are case sensitive.

* There might be whitespaces between the different characters. Or not...

* There should be support for parentheses and their coefficient.
    Example: a + 3 (6b - c).

* You may encounter several imbricated levels of parentheses,
    but you'll get only constant terms for the accompanying coefficients
    (never variables).

* All equations will be linear.

* In your final answer, include a leading 1 when the coefficient
    is 1 (e.g. 1j instead of just j).

* There are no floating-point numbers.

See the sample tests for clarification on what exactly the input/output
formatting should be.

Without giving away too many hints, the idea is to substitute the examples
into the formula and reduce the resulting equation to one unique term.
Look carefully at the example tests: you'll have to identify the pattern
used to replace variables in the formula/other equations. Using this pattern,
only one solution is possible for each test, so if you keep asking yourself
"but what if instead of that I do...", then you've missed the pattern.
