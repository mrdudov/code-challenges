from itertools import cycle, chain


def encode_rail_fence_cipher(string, n):

    rails = [[] for _ in range(n)]
    index = cycle(chain(range(n), range(n-2, 0, -1)))
    [rails[next(index)].append(character) for character in string]

    return ''.join(chain(*rails))


def decode_rail_fence_cipher(string, n):

    rails = [[] for _ in range(n)]
    index = cycle(chain(range(n), range(n-2, 0, -1)))
    [rails[next(index)].append(character) for character in string]

    line_lens = [len(l) for l in rails]
    index = cycle(chain(range(n), range(n-2, 0, -1)))
    rails = []

    prev_idx = 0
    next_idx = 0
    for line_len in line_lens:
        next_idx += line_len
        rails.append(string[prev_idx:next_idx])
        prev_idx = next_idx

    rails = [iter(s) for s in rails]

    return ''.join([next(rails[next(index)]) for _ in string])
