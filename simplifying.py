def simplify(examples, formula):
    return formula[0]


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
    print(f'{simplify(examples[i], formula[i])=}')
    print(f'{answer[i]=}')
    print('is test pass: ', simplify(examples[i], formula[i]) == answer[i])
