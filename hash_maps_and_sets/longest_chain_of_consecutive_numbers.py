"""
https://bytebytego.com/exercises/coding-patterns/hash-maps-and-sets/longest-chain-of-consecutive-numbers

Difficulty: Medium

Find the longest chain of consecutive numbers in an array. Two numbers are consecutive if they have a difference of 1.

Example:
Input: nums = [1, 6, 2, 5, 8, 7, 10, 3]
Output: 4
Explanation: The longest chain of consecutive numbers is 5, 6, 7, 8.
"""


# Book's solution
# Time complexity: O(n) because although there are two loops, the inner loop is only executed when the current number
# is the smallest number in the start its a chain. This ensures each chain is iterated through only once in the inner
# while-loop. Thus, the total number of iterations for both loops combined is: 𝑂(𝑛) the outer for-loop runs 𝑛 times, and
# the inner while-loop runs a total of 𝑛 times across all iterations, resulting in a combined time complexity of
# (𝑛 + 𝑛) = 𝑂(𝑛)
# Space complexity: O(n) since the set stores each unique number from the array input
def longest_chain_of_consecutive_numbers(nums: list[int]) -> int:
    # Return early for edge cases
    if not nums:
        return 0

    if len(nums) == 1:
        return 1

    num_set = set(nums)
    longest_chain = 0
    for num in num_set:
        # If the current number is the smallest number in its chain, search for the length of its chain
        if num - 1 not in num_set:
            smallest_num_in_chain = num
            current_chain = 1

            while (smallest_num_in_chain + 1) in num_set:
                smallest_num_in_chain += 1
                current_chain += 1

            longest_chain = max(longest_chain, current_chain)

    return longest_chain


# Alternative code
# Time complexity: O(nlogn) since .sort() is used
# Space complexity: O(n) since the set and list storage grows depending on the size of the array input
# def longest_chain_of_consecutive_numbers(nums: list[int]) -> int:
#     if not nums:
#         return 0
#
#     if len(nums) == 1:
#         return 1
#
#     nums = list(set(nums))
#     nums.sort()
#
#     max_chain = 0
#     current_chain = 1
#     for num in range(len(nums) - 1):
#         if nums[num + 1] - nums[num] == 1:
#             current_chain += 1
#             max_chain = max(max_chain, current_chain)
#
#         else:
#             current_chain = 1
#
#     if max_chain == 0:
#         return 1
#
#     return max_chain


if __name__ == "__main__":
    assert longest_chain_of_consecutive_numbers([1, 6, 2, 5, 8, 7, 10, 3]) == 4
    assert longest_chain_of_consecutive_numbers([5]) == 1
    assert longest_chain_of_consecutive_numbers([]) == 0
    assert longest_chain_of_consecutive_numbers([10, 20, 30, 40]) == 1
