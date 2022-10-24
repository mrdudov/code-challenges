from string import ascii_lowercase

def simplify(examples, formula):
    
    d = {}
    for e in examples:
        v, k = map(lambda s: s.strip(), e.split('='))
        d[k] = v
    result = formula
    for ch in formula:
        if ch in ascii_lowercase:
            result = result.replace(ch, f"({d.get(ch, ch)})")
    
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
    print('is test pass: ', simplify(examples[i], formula[i]) == answer[i])
    break

