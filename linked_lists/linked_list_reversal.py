"""
https://bytebytego.com/exercises/coding-patterns/linked-lists/linked-list-reversal

Difficulty: Easy

Reverse a singly linked list.

Example:
1 -> 2 -> 4 -> 7 -> 3
3 -> 7 -> 4 -> 2 -> 1
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
# Time complexity: O(n)
# Space complexity: O(1)
def linked_list_reversal(head: ListNode) -> Optional[ListNode]:
    if not head:
        return head

    curr_node = head
    prev_node = None
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    head = prev_node
    return head


if __name__ == "__main__":
    my_ll = SinglyLinkedList(1)
    my_ll.append(2)
    my_ll.append(4)
    my_ll.append(7)
    my_ll.append(3)
    my_ll.display()  # 1 -> 2 -> 4 -> 7 -> 3 -> None
    print()

    my_ll.head = linked_list_reversal(my_ll.head)
    assert my_ll.head.val == 3
    my_ll.display()  # 3 -> 7 -> 4 -> 2 -> 1 -> None
