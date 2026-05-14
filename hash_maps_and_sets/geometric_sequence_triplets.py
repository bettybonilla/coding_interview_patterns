"""

https://bytebytego.com/exercises/coding-patterns/hash-maps-and-sets/geometric-sequence-triplets

Difficulty: Medium

A geometric sequence triplet is a sequence of three numbers where each successive number is obtained by multiplying the
preceding number by a constant called the common ratio.

Let's examine three triplets to understand how this works:

(1, 2, 4): This is a geometric sequence with a ratio of 2 (i.e., [1, 1⋅2 = 2, 2⋅2 = 4]).
(5, 15, 45): This is a geometric sequence with a ratio of 3 (i.e., [5, 5⋅3 = 15, 15⋅3 = 45]).
(2, 3, 4): Not a geometric sequence.

Given an array of integers and a common ratio r, find all triplets of indexes (i, j, k) that follow a geometric sequence
for i < j < k. It's possible to encounter duplicate triplets in the array.

Example:
Input: nums = [2, 1, 2, 4, 8, 8], r = 2
Output: 5
Explanation:
Triplet [2, 4, 8] occurs at indexes (0, 3, 4), (0, 3, 5), (2, 3, 4), (2, 3, 5).
Triplet [1, 2, 4] occurs at indexes (1, 2, 3).
"""

from collections import defaultdict


def geometric_sequence(nums: list[int], r: int) -> int:
    # To find the triplets for each value, we can use the (x/r, x, x·r) triplet representation which allows us to always
    # maintain order by looking for x/r to the left of x and x·r to the right.
    # Use 'defaultdict' to ensure the default value of 0 is returned when accessing a key that doesn’t exist in the hash
    # map. This effectively sets the default frequency of all elements to 0.
    left_map = defaultdict(int)
    right_map = defaultdict(int)
    counter = 0

    # Initially fill right_map with the frequency of each element since we're traversing the array starting from the
    # left so every element is a potential candidate for x·r to the right.
    for x in nums:
        right_map[x] += 1

    # Search for geometric triplets that have x as the middle of a triplet.
    for x in nums:
        # Decrement the frequency of the current value in the right_map since this value is currently being processed
        # and cannot be to the right of itself
        right_map[x] -= 1

        # x needs to be divisible by r otherwise it cannot form a triplet
        if x % r == 0:
            counter += left_map[x // r] * right_map[x * r]

        # Increment the frequency of x in left_map since it'll be a part of the left side of the array once we iterate
        # to the next value of x in the array.
        left_map[x] += 1

    return counter


if __name__ == "__main__":
    assert geometric_sequence([2, 1, 2, 4, 8, 8], 2) == 5
