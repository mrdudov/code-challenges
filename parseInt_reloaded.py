def parse_int(string):
    print(string)
    words = string.split()
    number = 0
    sequence = []
    
    ten = {
        "and": 0,
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": '*100',
        "thousand": '*1000',
        "million": '*1000000',
    }
    
    
    for word in words:
        if '-' in word:
            for sub_word in word.split('-'):
                sequence.append(ten[sub_word])
        else:
            sequence.append(ten[word])
            

    print(sequence)
    num_part = 0
    
    for s in sequence:
        try:
            num_part += int(s)
        except:
            if s == '*100':
                num_part *= 100
            if s == '*1000':
                num_part *= 1000
            number += num_part
            num_part = 0

        print(f'{num_part=} {number=} {s=}')
    number += num_part
    return number
