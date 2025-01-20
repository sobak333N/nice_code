from pydantic import BaseModel
from typing import Any, List, Optional


class Node(BaseModel):
    ...

class Node(BaseModel):
    val: Any
    prev: Node=None 
    next: Node=None


class MyDeque(BaseModel):
    tail: Node=None
    head: Node=None
    _size: int=0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def size(self):
        return self._size

    def __validate(self):
        if self.is_empty():
            raise IndexError("pop from empty deque")

    def append(self, item: Any):
        self._size+=1
        node = Node(val=item)
        if self.head:
            self.head.next = node
            self.head.next.prev = self.head

            self.head = self.head.next
        else:
            self.head = node
            self.tail = node
    
    def appendleft(self, item: Any):
        self._size+=1
        node = Node(val=item)
        if self.tail:
            self.tail.prev = node
            self.tail.prev.next = self.tail

            self.tail = self.tail.prev
        else:
            self.head = node
            self.tail = node

    def pop(self):
        self.__validate()
        ans = self.peeklast()   
        if self._size == 1:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.prev
            self.head.next = None
        
        self._size-=1
        return ans



    def popleft(self):
        self.__validate()
        ans = self.peek()   
        if self._size == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.next
            self.tail.prev = None
        
        self._size-=1
        return ans


    def peeklast(self):
        self.__validate()
        return self.head.val

    def peek(self):
        self.__validate()
        return self.tail.val

    def __iter__(self):
        cur = self.tail
        while cur:
            yield cur.val
            cur = cur.next

    def __str__(self):
        values = []
        cur = self.tail
        while cur:
            values.append(cur.val)
            cur = cur.next
        return "[" + ", ".join(list(map(str,values))) + "]"