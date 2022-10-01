# https://www.codewars.com/kata/52996b5c99fdcb5f20000004

from collections import Counter
import copy
import math
from pprint import pprint


def runoff(voters):
    # 1. Each voter selects several candidates in order of preference.

    voters = copy.deepcopy(voters)
    voters_count = len(voters)
    
    while True:
        pprint(voters)

        # 2. The votes are tallied from the each voter's first choice.
        max_candidate, max_candidate_count = Counter([i[0] for i in voters]).most_common(1)[0]
        print(f"{max_candidate=}, {max_candidate_count=}")
        
        # 3. If the first-place candidate has more than half the total votes, they win.
        if max_candidate_count > voters_count / 2:
            return max_candidate
        
        # 4. Otherwise, find the candidate who got the least votes and remove them from each person's voting list.
        # 5. In case of a tie for least, remove all of the tying candidates.
        
        all_candidate_count = len(voters[0])
        for idx in range(0, math.ceil(all_candidate_count/2)):
            left_counter = Counter([column[idx] for column in voters])
            right_counter = Counter([column[all_candidate_count - idx - 1] for column in voters])
            print(f"{left_counter=} {right_counter=}")
            print(f"{len(set(right_counter.values()))=}")
            if left_counter == right_counter:
                continue
            if all(map(lambda x : x == 1, right_counter.values())):
                continue
#             if len(set(right_counter.values())) != 1:
            min_candidate, min_candidate_count = right_counter.most_common(1)[0]
            break
        else:
            return None
        
        less_candidates = list(filter(lambda x: x[1] == min_candidate_count , dict(right_counter).items()))
        for candidate in less_candidates:
            for i, vote in enumerate(voters):
                for j, candidate_in_vote in enumerate(vote):
                    if candidate_in_vote == candidate[0]:
                        voters[i].pop(j)
        
        # 6. In case of a complete tie between every candidate, return None
