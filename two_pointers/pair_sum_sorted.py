"""
https://bytebytego.com/exercises/coding-patterns/two-pointers/pair-sum-sorted

Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers in
the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, return an
empty array.

Example 1:
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
Explanation: nums[2] + nums[3] = 3 + 4 = 7

Example 2:
Input: nums = [1, 1, 1], target = 2
Output: [0, 1]
Explanation: other valid outputs could be [1, 0], [0, 2], [2, 0], [1, 2] or [2, 1].
"""

from typing import NoReturn


def pair_sum_sorted(nums: list[int], target: int) -> list[int | NoReturn]:
    left = 0
    right = len(nums) - 1
    while left < right:
        left_right_sum = nums[left] + nums[right]

        if left_right_sum == target:
            return [left, right]

        if left_right_sum < target:
            left += 1

        if left_right_sum > target:
            right -= 1

    return []


if __name__ == "__main__":
    assert pair_sum_sorted([-5, -2, 3, 4, 6], 7) == [2, 3]
    assert pair_sum_sorted([1, 1, 1], 2) == [0, 2]
    assert pair_sum_sorted([1, 2, 3, 4, 5], 3) == [0, 1]
    assert pair_sum_sorted([], 0) == []
    assert pair_sum_sorted([1], 1) == []
    assert pair_sum_sorted([2, 3], 5) == [0, 1]
    assert pair_sum_sorted([2, 4], 5) == []
    assert pair_sum_sorted([2, 2, 3], 5) == [0, 2]
    assert pair_sum_sorted([-3, -2, -1], -5) == [0, 1]
