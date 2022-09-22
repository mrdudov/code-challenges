# https://www.codewars.com/kata/52996b5c99fdcb5f20000004

from collections import Counter
import copy
from itertools import takewhile
from pprint import pprint


def runoff(voters):
    voters = copy.deepcopy(voters)
    max_c = Counter()
    min_c = Counter()

    while True:
        pprint(voters)
        candidate_count = len(voters[0])
        voters_count = len(voters)
        max_c = Counter([i[0] for i in voters])
        min_c = Counter([i[-1] for i in voters])

        if min_c.most_common(1)[0][0] == max_c.most_common(1)[0][0]:
            return None

        if max_c.most_common(1)[0][1] > voters_count / 2:
            return max_c.most_common(1)[0][0]
        else:
            less_c = min_c.most_common(1)[0][0]
            print(f"{less_c=}")
            less_candidates = list(filter(lambda x: x == less_c, min_c))

            for candidate in less_candidates:
                for i, vote in enumerate(voters):
                    for j, candidate_in_vote in enumerate(vote):
                        if candidate_in_vote == candidate:
                            voters[i].pop(j)
#             print(f"{less_candidates=}")

    return None
