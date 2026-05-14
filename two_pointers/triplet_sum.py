"""
https://bytebytego.com/exercises/coding-patterns/two-pointers/triplet-sum

Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 . The solution must not contain
duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates). If no such triplets are found, return an
empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [[-3, 1, 2], [-1, 0, 1]]
"""

from typing import NoReturn


def pair_sum_sorted_all_pairs(
    nums: list[int], start: int, target: int
) -> list[list[int] | NoReturn]:
    all_pairs = []
    left = start
    right = len(nums) - 1
    while left < right:
        left_right_sum = nums[left] + nums[right]

        if left_right_sum == target:
            all_pairs.append([nums[left], nums[right]])
            left += 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1

        elif left_right_sum < target:
            left += 1

        elif left_right_sum > target:
            right -= 1

    return all_pairs


def triplet_sum(nums: list[int]) -> list[list[int] | NoReturn]:
    nums.sort()
    triplets = []
    for i in range(len(nums)):
        if nums[i] > 0:
            break

        elif i > 0 and nums[i] == nums[i - 1]:
            continue

        all_pairs = pair_sum_sorted_all_pairs(nums, i + 1, -nums[i])
        for pair in all_pairs:
            if not pair:
                return triplets

            triplets.append([nums[i]] + pair)

    return triplets


if __name__ == "__main__":
    assert triplet_sum([0, -1, 2, -3, 1]) == [[-3, 1, 2], [-1, 0, 1]]
    assert triplet_sum([-4, -4, -2, 0, 0, 1, 2, 3]) == [[-4, 1, 3], [-2, 0, 2]]
    assert triplet_sum([]) == []
    assert triplet_sum([0]) == []
    assert triplet_sum([-1, 1]) == []
    assert triplet_sum([-2, -1, -1, 1, 2, 2]) == [[-1, -1, 2]]
    assert triplet_sum([1, 0, 1]) == []
