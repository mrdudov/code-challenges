import re


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
    pattern = r"(?<=[^0-9])[a-zA-Z]{1}"

    def add_one(x: re.Match) -> str:
        if x.group(0):
            return f"1{x.group(0)}"

    formula = re.sub(pattern=pattern, repl=add_one, string=formula)
    return formula


def calc(match: re.Match) -> str:
    if match.group(2) == "+":
        result = int(match.group(1)) + int(match.group(3))
        if result == 0:
            return f"+{result}{match.group(4)}"
    if match.group(2) == "-":
        result = int(match.group(1)) - int(match.group(3))
        if result == 0:
            return f"+{result}{match.group(4)}"
    return f"+{result}{match.group(4)}" if result > 0 else f"{result}{match.group(4)}"


def cleaner(formula: str) -> str:
    formula = re.sub(pattern=r"--", repl="+", string=formula)
    formula = re.sub(pattern=r"\+\+", repl="+", string=formula)
    formula = re.sub(pattern=r"\+-", repl="-", string=formula)
    formula = re.sub(pattern=r"-\+", repl="-", string=formula)
    formula = re.sub(pattern=r"\+\)", repl=")", string=formula)
    formula = re.sub(pattern=r"\-\)", repl=")", string=formula)
    return formula


def simplify(equalities, formula):
    equalities = parse_equalities(equalities)

    formula = replace_equalities_in_formula(formula=formula, equalities=equalities)
    formula = remove_whitespace(formula=formula)
    formula = to_char_add_digit(formula=formula)

    while True:
        old_formula = formula


        new_formula = cleaner(formula=formula)
        if new_formula != formula:
            print(formula)
        formula = new_formula

        
        # -2a+3a 
        pattern = r"([-]*[0-9]*)[a-zA-Z]([+-])([+-]*[0-9]*)([a-zA-Z])"
        new_formula = re.sub(pattern=pattern, repl=calc, string=formula)
        if new_formula != formula:
            print(formula)
        formula = new_formula
        

        new_formula = cleaner(formula=formula)
        if new_formula != formula:
            print(formula)
        formula = new_formula


        # 2(-36a)
        pattern = r"([0-9]{1,})\(([+-]*[0-9]*)([a-zA-Z])\)"
        new_formula = re.sub(
            pattern=pattern,
            repl=lambda match: f"{int(match.group(1)) * int(match.group(2))}{match.group(3)}",
            string=formula,
        )
        if new_formula != formula:
            print(formula)
        formula = new_formula


        new_formula = cleaner(formula=formula)
        if new_formula != formula:
            print(formula)
        formula = new_formula


        pattern = r"\(([+-]*[0-9]*[a-zA-Z])\)"
        new_formula = re.sub(
            pattern=pattern, repl=lambda m: f"{m.group(1)}", string=formula
        )
        if new_formula != formula:
            print(formula)
        formula = new_formula


        new_formula = cleaner(formula=formula)
        if new_formula != formula:
            print(formula)
        formula = new_formula


        pattern = r"^[+]*([0-9]*[a-zA-Z])$"
        new_formula = re.sub(
            pattern=pattern, repl=lambda m: f"{m.group(1)}", string=formula
        )
        if new_formula != formula:
            print(formula)
        formula = new_formula


        if old_formula == formula:
            break
    
    return formula
