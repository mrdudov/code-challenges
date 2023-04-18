import re
from string import ascii_lowercase


def parse_equalities(equ):
    return dict(map(lambda s: s.strip(), e.split("=")[::-1]) for e in equ)


def replace_equalities_in_formula(formula, equalities):
    new_formula = formula
    old_formula = formula

    while True:
        old_formula = new_formula

        for key, val in equalities.items():
            if key in new_formula:
                new_formula = new_formula.replace(key, f"({val})")

        if new_formula == old_formula:
            break
    return new_formula


def remove_whitespace(formula: str) -> str:
    return formula.replace(" ", "")


def to_char_add_digit(formula: str) -> str:
    pattern = r"(?<=[^0-9])[a-z]{1}"

    def add_one(x: re.Match) -> str:
        if x.group(0):
            return f"1{x.group(0)}"

    formula = re.sub(pattern=pattern, repl=add_one, string=formula)
    return formula


def open_the_brackets(formula: str) -> str:
    def calc(match: re.Match) -> str:
        if match.group(2) == "+":
            return str(int(match.group(1)) + int(match.group(3))) + match.group(4)
        if match.group(2) == "-":
            return str(int(match.group(1)) - int(match.group(3))) + match.group(4)

    while "(" in formula:
        pattern = r"\(([+-]*[0-9]*)[a-z]([+-])([+-]*[0-9]*)([a-z])\)"
        formula = re.sub(pattern=pattern, repl=calc, string=formula)
        print(formula)
        # break
    return formula


def simplify(equalities, formula):
    equalities = parse_equalities(equalities)

    formula = replace_equalities_in_formula(formula=formula, equalities=equalities)
    formula = remove_whitespace(formula=formula)

    print("")
    print(f"remove_whitespace: {formula=}")

    formula = to_char_add_digit(formula=formula)

    print("")
    print(f"to_char_add_digit: {formula=}")
    print("")

    formula = open_the_brackets(formula=formula)

    return formula
