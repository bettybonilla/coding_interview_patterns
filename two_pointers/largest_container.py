"""
https://bytebytego.com/exercises/coding-patterns/two-pointers/largest-container

You are given an array of numbers, each representing the height of a vertical line on a graph. A container can be formed
with any pair of these lines, along with the x-axis of the graph. Return the amount of water which the largest container
can hold.

Example:
Input: heights = [2, 7, 8, 3, 7, 6]
Output: 24
"""


def largest_container(heights: list[int]) -> int:
    max_water_contained = 0
    left = 0
    right = len(heights) - 1
    while left < right:
        current_water_contained = min(heights[left], heights[right]) * (right - left)
        max_water_contained = max(max_water_contained, current_water_contained)

        if heights[left] < heights[right]:
            left += 1

        elif heights[left] > heights[right]:
            right -= 1

        elif heights[left] == heights[right]:
            left += 1
            right -= 1

    return max_water_contained


if __name__ == "__main__":
    assert largest_container([2, 7, 8, 3, 7, 6]) == 24
    assert largest_container([]) == 0
    assert largest_container([1]) == 0
    assert largest_container([0, 1, 0]) == 0
    assert largest_container([3, 3, 3, 3]) == 9
    assert largest_container([1, 2, 3]) == 2
    assert largest_container([3, 2, 1]) == 2
