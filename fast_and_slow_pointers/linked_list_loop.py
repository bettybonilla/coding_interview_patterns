"""
https://bytebytego.com/exercises/coding-patterns/fast-and-slow-pointers/linked-list-loop

Difficulty: Easy

Given a singly linked list, determine if it contains a cycle. A cycle occurs if a node's next pointer references an
earlier node in the linked list, causing a loop.
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

    def get(self, index: int) -> Optional[ListNode]:
        if index < 0 or index >= self.length:
            return None

        elif index == 0:
            return self.head

        elif index == self.length - 1:
            return self.tail

        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next

        return curr_node

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


def linked_list_loop(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True

    return False


if __name__ == "__main__":
    my_ll = SinglyLinkedList(0)
    my_ll.append(1)
    my_ll.append(2)
    my_ll.append(3)
    my_ll.append(4)
    my_ll.append(5)
    my_ll.display()  # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
    assert not linked_list_loop(my_ll.head)
    print()

    my_ll.get(5).next = my_ll.get(2)
    assert my_ll.get(5).next == my_ll.get(2)  # Now has a cycle/loop
    # my_ll.display()
    assert linked_list_loop(my_ll.head)

    my_ll.clear()
    my_ll.append(1)
    my_ll.display()  # 1 -> None
    assert not linked_list_loop(my_ll.head)
