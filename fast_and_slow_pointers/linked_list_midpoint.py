"""
https://bytebytego.com/exercises/coding-patterns/fast-and-slow-pointers/linked-list-midpoint

Difficulty: Easy

Given a singly linked list, find and return its middle node. If there are two middle nodes, return the second one.

Example 1:
1 -> 2 -> 4 -> 7 -> 3
Output: Node 4

Example 2:
1 -> 2 -> 4 -> 7
Output: Node 4

Constraints:
The linked list contains at least one node.
The linked list contains unique values.
"""

from typing import Optional


class ListNode:
    def __init__(self, value=None, next_node=None):
        self.val = value
        self.next = next_node


class SinglyLinkedList:
    def __init__(self, value: int):
        new_node = ListNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value: int) -> bool:
        new_node = ListNode(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def display(self):
        if self.length == 0:
            print("Empty linked list")

        else:
            curr_node = self.head
            while curr_node:
                print(curr_node.val, end=" -> ")
                curr_node = curr_node.next

            print("None")


# Book's solution
# Time complexity: O(n) -> 1 O(n) iteration
# Space complexity: O(1)
def linked_list_midpoint(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


# Alternative code
# Time complexity: O(n) -> 2 O(n) iterations
# Space complexity: O(1)
# def linked_list_midpoint(head: ListNode) -> ListNode:
#     curr_node = head
#     length = 1
#     while curr_node and curr_node.next:
#         curr_node = curr_node.next
#         length += 1
#
#     curr_node = head
#     midpoint = length // 2
#     for _ in range(midpoint):
#         curr_node = curr_node.next
#
#     return curr_node


if __name__ == "__main__":
    my_ll = SinglyLinkedList(1)
    my_ll.append(2)
    my_ll.append(4)
    my_ll.append(7)
    my_ll.append(3)
    my_ll.display()  # 1 -> 2 -> 4 -> 7 -> 3 -> None
    assert linked_list_midpoint(my_ll.head).val == 4
    print()

    my_ll.clear()
    my_ll.append(1)
    my_ll.append(2)
    my_ll.append(4)
    my_ll.append(7)
    my_ll.display()  # 1 -> 2 -> 4 -> 7 -> None
    assert linked_list_midpoint(my_ll.head).val == 4
