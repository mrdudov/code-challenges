# Instant runoff voting

[Kata on CodeWars](https://www.codewars.com/kata/52996b5c99fdcb5f20000004)

## description

Your task is to implement a function that calculates an election winner from a list of voter selections using an Instant Runoff Voting algorithm. If you haven't heard of IRV, here's a basic overview (slightly altered for this kata):

* Each voter selects several candidates in order of preference.
* The votes are tallied from the each voter's first choice.
* If the first-place candidate has more than half the total votes, they win.
* Otherwise, find the candidate who got the least votes and remove them from each person's voting list.
* In case of a tie for least, remove all of the tying candidates.
* In case of a complete tie between every candidate, return None.
* Start over.
* Continue until somebody has more than half the votes; they are the winner.

Your function will be given a list of voter ballots; each ballot will be a list of candidates (symbols) in descending order of preference. You should return the symbol corresponding to the winning candidate.
