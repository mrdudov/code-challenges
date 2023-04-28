from collections import Counter
import copy
from string import ascii_lowercase
from pprint import pprint


def runoff(voters):

    voters = copy.deepcopy(voters)

    renamed_flag = False

    if len(voters[0][0]) != 1:
        renamed_flag = True
        candidate_iter = iter(voters[0])
        name_iter = iter(ascii_lowercase)
        rename_dict = {next(candidate_iter): next(name_iter)
                       for _ in voters[0]}
        pprint(rename_dict)

        new_voters = []
        for voter in voters:
            new_voters.append([rename_dict[i] for i in voter])
        voters = new_voters

    voters_count = len(voters)

    while voters[0]:
        print("-"*10, " main loop ", "-"*10)
        pprint(voters)

        max_candidate, max_candidate_count = Counter(
            [i[0] for i in voters]).most_common(1)[0]
        max_candidates = list(filter(lambda x: x[1] == max_candidate_count, dict(
            Counter([column[0] for column in voters])).items()))
        print(f"{max_candidates=}")

        if max_candidate_count > voters_count / 2:
            print(f"WINER: {max_candidate}")
            if renamed_flag:
                return [i[0] for i in rename_dict.items() if i[1] == max_candidate][0]
            return max_candidate

        if len(set([i[0] for i in voters])) == len(voters):
            print(f"{set([i[0] for i in voters])=}")
            print("return None")
            return None
        if len(set(Counter([i[0] for i in voters]).values())) == 1:
            return None

        if len(max_candidates) == 1 and len(set(Counter([i[0] for i in voters]).values())) == 2:
            print(f"WINER: {max_candidate}")
            if renamed_flag:
                return [i[0] for i in rename_dict.items() if i[1] == max_candidate][0]
            return max_candidate

        min_candidate_count = min(
            Counter([column[0] for column in voters]).values())
        less_candidates = list(filter(lambda x: x[1] == min_candidate_count, dict(
            Counter([column[0] for column in voters])).items()))
        print(f"{less_candidates=}")

        for candidate in less_candidates:
            for i, vote in enumerate(voters):
                for j, candidate_in_vote in enumerate(vote):
                    if candidate_in_vote == candidate[0]:
                        voters[i].pop(j)

    print(f"WINER: {None}")
