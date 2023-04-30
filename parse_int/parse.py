from typing import List

from .configure import DIGIT_NAMES


def split_string_to_words(string: str) -> List[str]:
    """
    convert 
        'seven hundred eighty-three thousand nine hundred and nineteen'
    to 
        ['seven', 'hundred', 'eighty', 'three', 'thousand', 'nine', 'hundred', 'and', 'nineteen']
    """

    result = []
    for word in string.split():
        if '-' in word:
            for sub_word in word.split('-'):
                result.append(DIGIT_NAMES[sub_word])
        else:
            result.append(DIGIT_NAMES[word])
    return result


def parse_int(string: str) -> int:
    """
    Convert a string into an integer.

    "one" => 1
    "twenty" => 20
    "two hundred forty-six" => 246
    "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
    """
    
    result = 0
    num_part = 0
    hundred = False

    words_sequence = split_string_to_words(string=string)

    for word in words_sequence:
        try:
            num_part += int(word)
        except:

            if word == '*100':
                hundred = True
                num_part *= 100

            if word == '*1000':
                if hundred:
                    result += num_part
                    num_part = 0
                    result *= 1000

                else:
                    num_part *= 1000

            if word == '*1000000':
                num_part *= 1_000_000

            result += num_part
            num_part = 0

    result += num_part

    return result
