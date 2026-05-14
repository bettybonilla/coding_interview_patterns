"""
https://bytebytego.com/exercises/coding-patterns/two-pointers/next-lexicographical-sequence

Given a string of lowercase English letters, rearrange the characters to form a new string representing the next
immediate sequence in lexicographical (alphabetical) order. If the given string is already last in lexicographical order
among all possible arrangements, return the arrangement that's first in lexicographical order.

Example 1:
Input: s = 'abcd'
Output: 'abdc'
Explanation: "abdc" is the next sequence in lexicographical order after rearranging "abcd".

Example 2:
Input: s = 'dcba'
Output: 'abcd'
Explanation: Since "dcba" is the last sequence in lexicographical order, we return the first sequence: "abcd".

Constraints:
The string contains at least one character.
"""


# Implements two pointers using the staged traversal strategy
def next_lexicographical_sequence(s: str) -> str:
    letters = list(s)
    pivot = len(letters) - 2

    while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:
        pivot -= 1

    if pivot == -1:
        return "".join(reversed(letters))

    right_successor = len(letters) - 1
    while letters[right_successor] <= letters[pivot]:
        right_successor -= 1

    letters[pivot], letters[right_successor] = letters[right_successor], letters[pivot]
    letters[pivot + 1 :] = reversed(letters[pivot + 1 :])
    return "".join(letters)


if __name__ == "__main__":
    assert next_lexicographical_sequence("abcd") == "abdc"
    assert next_lexicographical_sequence("dcba") == "abcd"
    assert next_lexicographical_sequence("abc") == "acb"
    assert next_lexicographical_sequence("a") == "a"
    assert next_lexicographical_sequence("aaaa") == "aaaa"
    assert next_lexicographical_sequence("ynitsed") == "ynsdeit"
