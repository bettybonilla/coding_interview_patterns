"""
https://bytebytego.com/exercises/coding-patterns/two-pointers/shift-zeros-to-the-end

Given an array of integers, modify the array in place to move all zeros to the end while maintaining the relative order
of non-zero elements.

Example:
Input: nums = [0, 1, 0, 3, 2]
Output: [1, 3, 2, 0, 0]
"""


# Implements two pointers using the unidirectional traversal strategy
def shift_zeros_to_the_end(nums: list[int]) -> list[int]:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums


if __name__ == "__main__":
    assert shift_zeros_to_the_end([0, 1, 0, 3, 2]) == [1, 3, 2, 0, 0]
    assert shift_zeros_to_the_end([1, 0, 1, 0, 3, 2]) == [1, 1, 3, 2, 0, 0]
    assert shift_zeros_to_the_end([1, 2, 0, 3, 4]) == [1, 2, 3, 4, 0]
    assert shift_zeros_to_the_end([]) == []
    assert shift_zeros_to_the_end([0]) == [0]
    assert shift_zeros_to_the_end([1]) == [1]
    assert shift_zeros_to_the_end([1, 3, 2]) == [1, 3, 2]
    assert shift_zeros_to_the_end([1, 1, 1, 0, 0]) == [1, 1, 1, 0, 0]
    assert shift_zeros_to_the_end([0, 0, 1, 1, 1]) == [1, 1, 1, 0, 0]
