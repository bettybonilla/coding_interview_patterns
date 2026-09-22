"""
https://bytebytego.com/exercises/coding-patterns/sliding-window/longest-substring-with-unique-characters

Difficulty: Medium

Given a string, determine the length of its longest substring that consists only of unique characters.

Example:
Input: s = 'abcba'
Output: 3
Explanation: Substring "abc" is the longest substring of length 3 that contains unique characters ("cba" also fits this
description).
"""


# Book's solution
# Implements a dynamic sliding window using two pointers
# Time complexity: O(n)
# Space complexity: O(m) because we use a hash map to store unique characters, where m represents the total number of
# unique characters within the string
def longest_substring_with_unique_chars(s: str) -> int:
    left = 0
    right = 0
    max_len = 0
    prev_indexes = {}
    while right < len(s):
        # If a previous index of the current character is present in the current window, it's a duplicate character in
        # the window
        if s[right] in prev_indexes and prev_indexes[s[right]] >= left:
            # Shrink the window to exclude the previous occurrence of this character
            left = prev_indexes[s[right]] + 1

        len_window = right - left + 1
        max_len = max(max_len, len_window)
        prev_indexes[s[right]] = right

        # Expand the window
        right += 1

    return max_len


if __name__ == "__main__":
    assert longest_substring_with_unique_chars("abcba") == 3
    assert longest_substring_with_unique_chars("cabcdeca") == 5
