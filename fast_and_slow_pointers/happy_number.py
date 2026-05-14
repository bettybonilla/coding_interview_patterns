"""
https://bytebytego.com/exercises/coding-patterns/fast-and-slow-pointers/happy-number

Difficulty: Medium

In number theory, a happy number is defined as a number that, when repeatedly subjected to the process of squaring its
digits and summing those squares, eventually leads to 1. An unhappy number will never reach 1 during this process, and
will get stuck in an infinite loop.

Given an integer, determine if it's a happy number.

Example:
Input: n = 23
Output: True
Explanation: 2^2 + 3^2 = 13 -> 1^2 + 3^2 = 10 -> 1^2 + 0^2 = 1
"""


def get_next_num(x: int) -> int:
    next_num = 0
    while x > 0:
        # If the number is more than 10, % 10 extracts the last digit of the number
        # Ex: 23 % 10 = 3 -> 23 / 10 is 2 with a remainder of 3
        # If the number is less than 10, % 10 will just equal the number itself since any number less than 10 divided
        # by 10 is 0 with a remainder of the number itself
        # Ex: 2 % 10 = 2 -> 2 / 10 is 0 with a remainder of 2
        last_digit = x % 10

        # Truncates (removes) the last digit of the number
        # Ex: 23 // 10 = 2 -> 23 / 10 is 2.3 then you just floor (round down) to 2 since it just chops off the decimal
        # Alternative code
        # x //= 10
        x = x // 10

        next_num += last_digit ** 2

    return next_num


def happy_number(n: int) -> bool:
    slow = n
    fast = n
    while True:
        slow = get_next_num(slow)
        fast = get_next_num(get_next_num(fast))

        if fast == 1:
            return True

        elif fast == slow:
            return False


if __name__ == "__main__":
    assert happy_number(23)
    assert not happy_number(116)
