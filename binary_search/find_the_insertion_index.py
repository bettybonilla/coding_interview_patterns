"""
https://bytebytego.com/exercises/coding-patterns/binary-search/find-the-insertion-index

Difficulty: Easy

You are given a sorted array that contains unique values, along with an integer target.
- If the array contains the target value, return its index.
- Otherwise, return the insertion index. This is the index where the target would be if it were inserted in order,
maintaining the sorted sequence of the array.

Example 1:
Input: nums = [1, 2, 4, 5, 7, 8, 9], target = 4
Output: 2

Example 2:
Input: nums = [1, 2, 4, 5, 7, 8, 9], target = 6
Output: 4
Explanation: 6 would be inserted at index 4 to be positioned between 5 and 7: [1, 2, 4, 5, 6, 7, 8, 9].
"""


# Book's solution
# Time complexity: O(logn) since it performs a binary search over a search space of size n + 1
# Space complexity: O(1)
def find_the_insertion_index(nums: list[int], target: int) -> int:
    # Return early for edge case
    if not nums:
        return 0

    left = 0
    right = len(nums)

    # Return early for boundary checks
    if nums[left] > target:
        return 0

    elif nums[right - 1] < target:
        return right

    # Otherwise, perform a binary search
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid

        else:
            left = mid + 1

    return left


# Alternative code
# Time complexity: O(n)
# Space complexity: O(1)
# def find_the_insertion_index(nums: list[int], target: int) -> int:
#     if not nums:
#         return 0
#
#     elif target in nums:
#         return nums.index(target)
#
#     left = 0
#     right = len(nums) - 1
#
#     if nums[left] > target:
#         return 0
#
#     elif nums[right] < target:
#         return right + 1
#
#     while left < right:
#         if nums[left] < target:
#             left += 1
#
#         elif nums[right] > target:
#             right -= 1
#
#     return left


if __name__ == "__main__":
    assert find_the_insertion_index([1, 2, 4, 5, 7, 8, 9], 4) == 2
    assert find_the_insertion_index([1, 2, 4, 5, 7, 8, 9], 6) == 4
    assert find_the_insertion_index([1, 2, 4, 5, 7, 8, 9, 12, 15], 6) == 4
    assert find_the_insertion_index([1, 3, 5, 7], 7) == 3
    assert find_the_insertion_index([2, 3, 5, 7], 8) == 4
    assert find_the_insertion_index([], 5) == 0
