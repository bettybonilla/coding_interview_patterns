"""
https://bytebytego.com/exercises/coding-patterns/hash-maps-and-sets/pair-sum-unsorted

Given an array of integers, return the indexes of any two numbers that add up to a target. The order of the indexes in
the result doesn't matter. If no pair is found, return an empty array.

Example:
Input: nums = [-1, 3, 4, 2], target = 3
Output: [0, 2]
Explanation: nums[0] + nums[2] = -1 + 4 = 3

Constraints:
The same index cannot be used twice in the result.
"""

from typing import NoReturn


def pair_sum_unsorted(nums: list[int], target: int) -> list[int | NoReturn]:
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]

        num_map[num] = index

    return []


if __name__ == "__main__":
    assert pair_sum_unsorted([-1, 3, 4, 2], 3) == [0, 2]
    assert pair_sum_unsorted([-1, 3, 4, 2], 6) == [2, 3]
