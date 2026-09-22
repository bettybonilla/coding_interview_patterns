"""
https://bytebytego.com/exercises/coding-patterns/sliding-window/substring-anagrams

Difficulty: Medium

Given two strings, s and t, both consisting of lowercase English letters, return the number of substrings in s that are
anagrams of t.

An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original
letters exactly once.

Example:
Input: s = 'caabab', t = 'aba'
Output: 2
Explanation: There is an anagram of t starting at index 1 ("caabab") and another starting at index 2 ("caabab")
"""


# Book's solution
# Implements a fixed sliding window using two pointers
# Time complexity: O(n)
# Space complexity: O(1)
def substring_anagrams(s: str, t: str) -> int:
    len_s = len(s)
    len_t = len(t)

    if len_t > len_s:
        return 0

    # Initialize arrays to keep track of the letter frequencies of the target and the window for comparison
    # The indexes represent lowercase letters a-z (Ex: index 0 = a, index 1 = b, index 2 = c, ... index 25 = z)
    target_freqs = [0] * 26
    window_freqs = [0] * 26

    # Set the letter frequencies of the target
    for char in t:
        target_freqs[ord(char) - ord("a")] += 1

    left = 0
    right = 0
    counter = 0
    while right < len_s:
        # The length of the current window
        len_window = right - left + 1

        # Increment the letter frequency at the right pointer before advancing the right pointer
        window_freqs[ord(s[right]) - ord("a")] += 1

        # If the window has reached the fixed length of t, we can check the letter frequencies of the window and the
        # target then advance the left and right pointer to slide the window
        if len_window == len_t:
            if window_freqs == target_freqs:
                counter += 1

            # Decrement the letter frequency at the left pointer before advancing the left pointer
            window_freqs[ord(s[left]) - ord("a")] -= 1
            left += 1

        right += 1

    return counter


if __name__ == "__main__":
    assert substring_anagrams("caabab", "aba") == 2
