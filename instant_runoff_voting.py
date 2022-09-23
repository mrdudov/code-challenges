# https://www.codewars.com/kata/52996b5c99fdcb5f20000004

from collections import Counter
import copy
from pprint import pprint


def runoff(voters):
    voters = copy.deepcopy(voters)

    while True:
        
        candidate_count = len(voters[0])
        voters_count = len(voters)
        max_c = Counter([i[0] for i in voters])
        min_c = Counter([i[-1] for i in voters])
        less_candidate = min_c.most_common(1)[0][0]
        less_candidates = list(filter(lambda x: x == less_candidate , min_c))
        
        pprint(voters)
        print(f"{less_candidate=}")
        
        if max_c.most_common(1)[0][1] > voters_count / 2:
            return max_c.most_common(1)[0][0]
        if min_c.most_common(1)[0] == max_c.most_common(1)[0]:
#         if min_c == max_c:
            print(f"{min_c=}")
            print(f"{max_c=}")
            print('return from ==')
            return None
        for candidate in less_candidates:
            for i, vote in enumerate(voters):
                for j, candidate_in_vote in enumerate(vote):
                    if candidate_in_vote == candidate:
                        voters[i].pop(j)               
    return None