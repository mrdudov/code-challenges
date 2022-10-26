from string import ascii_lowercase as lc
from typing import List
import re


def simplify(examples: List, formula: str) -> str:

    d = dict(map(lambda s: s.strip(), e.split('=')[::-1]) for e in examples)

    result = formula

    while len(set(filter(lambda l: l in lc, result))) > 1:
        for ch in result:
            if ch in lc and d.get(ch, None):
                result = result.replace(ch, f"({d[ch]})")

    result = result.replace(' ', '')

    print('--------------------------')
    while '(' in result:
        r = re.findall(r'\(([^\(]*?)\)', result)
        print(r)

        for i in r:
            print(re.split('\+|-|/|\*', i))

        break
    print('--------------------------')

    return result


examples = [["a + a = b", "b - d = c", "a + b = d"],
            ["a + 3g = k", "-70a = g"],
            ["-j -j -j + j = b"]
            ]
formula = ["c + a + b",
           "-k + a",
           "-j - b"
           ]
answer = ["2a",
          "210a",
          "1j"
          ]

for i in range(len(answer)):
    print('*'*60)
    print('examples:' + str(examples[i]))
    print('formula:' + str(formula[i]))
    print('expected answer:' + str(answer[i]))
    print(f'resut: {simplify(examples[i], formula[i])}')
    # print('is test pass: ', simplify(examples[i], formula[i]) == answer[i])
    # break
