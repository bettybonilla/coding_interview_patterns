"""
Below is an example of a singly linked list
"""

from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, value: int):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def get(self, index: int) -> Optional[Node]:
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

    def set(self, index: int, value: int):
        if self.get(index):
            self.get(index).value = value

    def append(self, value: int) -> bool:
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def prepend(self, value: int) -> bool:
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop(self) -> Optional[Node]:
        if self.length == 0:
            return None

        temp_node = self.head
        prev_node = self.head
        while temp_node.next:
            prev_node = temp_node
            temp_node = temp_node.next

        self.tail = prev_node
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp_node

    def pop_first(self) -> Optional[Node]:
        if self.length == 0:
            return None

        temp_node = self.head
        next_node = temp_node.next
        self.head = next_node
        temp_node.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp_node

    def insert(self, index: int, value: int) -> bool:
        if index < 0 or index > self.length:
            return False

        elif index == 0:
            return self.prepend(value)

        elif index == self.length:
            return self.append(value)

        new_node = Node(value)
        prev_node = self.get(index - 1)
        next_node = prev_node.next
        new_node.next = next_node
        prev_node.next = new_node
        self.length += 1
        return True

    def remove(self, index: int) -> Optional[Node]:
        if index < 0 or index >= self.length:
            return None

        elif index == 0:
            return self.pop_first()

        elif index == self.length - 1:
            return self.pop()

        prev_node = self.get(index - 1)
        temp_node = prev_node.next
        next_node = temp_node.next
        prev_node.next = next_node
        temp_node.next = None
        self.length -= 1
        return temp_node

    def reverse(self):
        curr_node = self.head
        self.head = self.tail
        self.tail = curr_node
        prev_node = None
        for _ in range(self.length):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

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
                print(curr_node.value, end=" -> ")
                curr_node = curr_node.next

            print("None")


if __name__ == "__main__":
    my_ll = SinglyLinkedList(4)
    my_ll.display()  # 4 -> None
    assert my_ll.get(0).value == 4
    my_ll.set(0, 100)
    my_ll.display()  # 100 -> None
    my_ll.set(0, 4)
    my_ll.display()  # 4 -> None
    assert my_ll.append(5)
    my_ll.display()  # 4 -> 5 -> None
    assert my_ll.prepend(3)
    my_ll.display()  # 3 -> 4 -> 5 -> None
    assert my_ll.insert(1, 10)
    assert my_ll.insert(0, 25)
    assert my_ll.insert(my_ll.length, 50)
    my_ll.display()  # 25 -> 3 -> 10 -> 4 -> 5 -> 50 -> None
    print("length:", my_ll.length)  # length: 6
    print()

    assert my_ll.pop().value == 50
    my_ll.display()  # 25 -> 3 -> 10 -> 4 -> 5 -> None
    print("length:", my_ll.length)  # length: 5
    assert my_ll.pop_first().value == 25
    my_ll.display()  # 3 -> 10 -> 4 -> 5 -> None
    print("length:", my_ll.length)  # length: 4
    assert my_ll.remove(1).value == 10
    assert my_ll.remove(0).value == 3
    assert my_ll.remove(my_ll.length - 1).value == 5
    my_ll.display()  # 4 -> None
    print("length:", my_ll.length)  # length: 1
    print()

    assert my_ll.append(5)
    assert my_ll.append(6)
    my_ll.display()  # 4 -> 5 -> 6 -> None
    my_ll.reverse()
    my_ll.display()  # 6 -> 5 -> 4 -> None
    print()

    my_ll.clear()
    my_ll.display()  # Empty linked list
