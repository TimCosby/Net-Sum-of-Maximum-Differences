# Net Sum of Maximum Differences
Returns the net sum of the maximum differences.

    Rules:
    1. Find the net sum of the maximum differences
    2. Min has to be in an earlier stage of the list
    3. You can have multiple sums of maximum differences to make the net sum
    4. Can only use a new min sum after you've found a max sum ie. a new sum cannot intersect with an old sum

    Strategy:
    Find MIN until found a MAX
    Find MAX until found a a NEW_MIN
    Find NEW_MIN strictly after MAX until NEW_MAX

    If NEW_MIN and NEW_MAX are found:
       sum MAX - MIN
       MIN = NEW_MIN
       MAX = NEW_MAX
       REPEAT

    If NEW_MIN and NEW_MAX can't be found:
       sum MAX - MIN
    return sum

Ex: list of [10, 7, 5, 9, 8, 11]
5 and 9 are a pair of differences
8 and 11 are a pair of differences
Note: 10 and 7 aren't because the min occurs after
(9 - 5) + (11 - 8) = 7

Ex: list of [10, 7, 5, 9, 11]
5 and 11 is the only pair of differences since 9 can not be paired with anything anything else non-intersecting
(11 - 5) = 6
