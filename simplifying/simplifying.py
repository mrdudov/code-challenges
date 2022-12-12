import re
from string import ascii_lowercase


def get_equalities(equ):

    return dict(map(lambda s: s.strip(), e.split('=')[::-1]) for e in equ)


def replace_symbol_to_equality(formula, equalities):
    while len(set(filter(lambda l: l in ascii_lowercase, formula))) > 1:
        for ch in formula:
            if ch in ascii_lowercase and equalities.get(ch, None):
                formula = formula.replace(ch, f"({equalities[ch]})")

    formula = formula.replace(' ', '')

    return formula


def simplify(equalities, formula):

    equalities = get_equalities(equalities)

    formula = replace_symbol_to_equality(
        formula=format,
        equalities=equalities
    )

    while '(' in formula:
        r = re.findall(r'\(([^\(]*?)\)', formula)
        print(r)

        for i in r:
            print(re.split('\+|-|/|\*', i))

        break

    return formula
