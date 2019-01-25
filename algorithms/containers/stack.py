from typing import Optional, Iterable
from linkedlist import SingleNode


class Stack(object):
    def __init__(self):
        super(Stack, self).__init__()
        self._first = None
        self._size = 0

    def push(self, item: Optional) -> None:
        """push the element to stack.
        """
        node = SingleNode(item, self._first)
        self._first = node
        self._size += 1

    def pop(self) -> Optional:
        """Pop the top element from stack.

        If stack is empty, it will return None,
        else return the value of top element.
        """
        if self._size == 0:
            return None
        item = self._first
        self._first = self._first.next
        self._size -= 1
        return item.value

    def empty(self) -> bool:
        return self._size == 0

    def peek(self) -> Optional:
        """Peek return the value of top element without removing it.

        If stack is empty, it will return None.
        """
        if self._first is None:
            return None
        else:
            return self._first.value

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterable:
        self._cur = self._first
        return self

    def __next__(self) -> Optional:
        if self._cur is None:
            raise StopIteration
        item = self._cur.value
        self._cur = self._cur.next
        return item
