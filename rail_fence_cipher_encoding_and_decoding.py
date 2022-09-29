from itertools import cycle, chain


def encode_rail_fence_cipher(string, n):
    rails = [[] for _ in range(n)]

    c = cycle(chain(range(n), range(n-2, 0, -1)))

    for character in string:
        rails[next(c)].append(character)

    result = ''

    for rail in rails:
        result += ''.join(rail)

    return result


def decode_rail_fence_cipher(string, n):
    rails_len = []
    return ''
