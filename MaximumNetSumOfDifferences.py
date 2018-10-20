

def maximum_difference(arr):
    """
    Return the net sum of the maximum differences.

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

    :param arr: A list of integers
    :return: Net sum of differences
    """

    if len(arr) < 2:
        return 0

    min_index = arr[0]
    max_index = -1
    new_min = -1
    net_sum = 0

    for index in arr[1::]:
        if new_min != -1 and index > new_min:
            # If found a new max -> add the old min/max difference to the sum and change
            # the old min/max to the new versions
            net_sum += max_index - min_index
            max_index = index
            min_index = new_min
            new_min = -1
        if index < min_index and max_index == -1:
            # If a max hasn't been found yet, but a lower min has
            min_index = index
        elif index > min_index and index > max_index:
            # If a bigger max has been found
            max_index = index
        elif max_index != -1 and (new_min == -1 or new_min > index):
            # If a new lower min has been found after max
            new_min = index

    if max_index != -1:
        # If a max was found, but a new min/max wasn't found
        net_sum += max_index - min_index

    return net_sum


print(maximum_difference([10, 7, 5, 9, 8, 11]))
