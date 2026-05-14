"""
https://bytebytego.com/exercises/coding-patterns/two-pointers/is-palindrome-valid

A palindrome is a sequence of characters that reads the same forward and backward.

Given a string, determine if it's a palindrome after removing all non-alphanumeric characters. A character is
alphanumeric if it's either a letter or a number.

Example 1:
Input: s = 'a dog! a panic in a pagoda.'
Output: True

Example 2:
Input: s = 'abc123'
Output: False

Constraints:
The string may include a combination of lowercase English letters, numbers, spaces, and punctuations.
"""


# Implements two pointers using the inward traversal strategy - Uses the Python built-in .isalnum() function
def is_palindrome_valid(s: str) -> bool:
    s = s.lower().strip()
    s = "".join(filter(lambda char: char.isalnum(), s))
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


# Alternative code
# Implements two pointers using the inward traversal strategy - Uses the Python built-in string module
# def is_palindrome_valid(s: str) -> bool:
#     s = s.lower().strip()
#     alphanumeric = string.ascii_lowercase + string.digits
#     s = "".join(filter(lambda char: char in alphanumeric, s))
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#
#         left += 1
#         right -= 1
#
#     return True


# Alternative code
# def is_palindrome_valid(s: str) -> bool:
#     s = s.lower().strip()
#     alphanumeric = string.ascii_lowercase + string.digits
#     s = "".join(filter(lambda char: char in alphanumeric, s))
#     return s == s[::-1]


if __name__ == "__main__":
    assert is_palindrome_valid("a dog! a panic in a pagoda.")
    assert not is_palindrome_valid("abc123")
    assert is_palindrome_valid("123321")
    assert not is_palindrome_valid("hello")
    assert is_palindrome_valid("racecar")
    assert is_palindrome_valid("raceecar")
    assert is_palindrome_valid("")
    assert is_palindrome_valid("a")
    assert is_palindrome_valid("aa")
    assert not is_palindrome_valid("ab")
    assert is_palindrome_valid("!, (?)")
    assert is_palindrome_valid("12.02.2021")
    assert not is_palindrome_valid("21.02.2021")
