from typing import Any, List


class Node:

    def __init__(self, key: Any, value: Any):
        self.key: Any = key
        self.value: Any = value
        self.next: Node = None
        self.prev: Node = None


class DoubleLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def append_head(self, key: Any, value: Any, new_node: Node=None) -> None:
        if not new_node:
            new_node = Node(key, value)
        self.size += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

            # print(node.value)
            # print(node.next)
            # print(node.prev)


    def pop_tail(self) -> Node:
        if self.tail is not None:
            temp = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.size -= 1
            return temp
    
    def move_to_head(self, node: Node) -> None:

        # print(node.value)
        # print(node.next)
        # print(node.prev)

        if node is self.head:
            pass
        elif node is self.tail:
            self.pop_tail()
            self.append_head(-1, -1 , node)
        else:
            self.size -= 1
            node.next.prev = node.prev
            node.prev.next = node.next
            self.append_head(-1, -1 , node)



            

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.dl_list = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1 
        node = self.node_map[key]
        self.dl_list.move_to_head(node)
        # self.node_map[key] = self.dl_list.head
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key not in self.node_map:
            if self.capacity == self.dl_list.size:
                old_node = self.dl_list.pop_tail()
                del self.node_map[old_node.key]
            self.dl_list.append_head(key, value)
            self.node_map[key] = self.dl_list.head
        else:
            node = self.node_map[key]
            node.value = value
            self.dl_list.move_to_head(node)
            # self.node_map[key] = self.dl_list.head


    def __str__(self) -> str:
        # Создаем список ключей, начиная с головы (самый недавно использованный)
        keys = []
        current = self.dl_list.head
        ans = "="*100+ "\n"+ f"{self.node_map}\n"
        while current:
            keys.append(f"({current.key}: {current.value})")
            current = current.next
        return ans + " -> ".join(keys) if keys else "Empty cache"



def main():
    # Создаем объект LRUCache с максимальным размером 3
    cache = LRUCache(3)

    # Добавляем пару (1, 1) в кэш
    cache.put(1, 1)
    print(cache)


    print(cache.get(1))  # Ожидаемый вывод: 1, так как мы только что добавили (1, 1)
    print(cache)

    cache.put(2, 2)
    print(cache)

    print(cache.get(2))  # Ожидаемый вывод: 2
    print(cache)

    cache.put(3, 3)
    print(cache)

    print(cache.get(3))  # Ожидаемый вывод: 3
    print(cache)
    
    cache.put(4, 4)
    print(cache)
    

    print(cache.get(4))  # Ожидаемый вывод: 4
    print(cache)

    print(cache.get(3))  # Ожидаемый вывод: 3
    print(cache)

    print(cache.get(2))  # Ожидаемый вывод: 2
    print(cache)

    print(cache.get(1))  # Ожидаемый вывод: -1, так как (1, 1) было удалено
    print(cache)
    




    print(f"cache.dl_list.size = {cache.dl_list.size}")
    # Добавляем пару (5, 5) в кэш. Это снова удалит самый старый элемент, т.е. (2, 2)
    cache.put(5, 5)
    print(cache)



    print(cache.get(1))  # Ожидаемый вывод: -1
    print(cache)

    print(cache.get(2))  # Ожидаемый вывод: -1
    print(cache)

    print(cache.get(3))  # Ожидаемый вывод: 3
    print(cache)

    print(cache.get(4))  # Ожидаемый вывод: 4
    print(cache)

    print(cache.get(5))  # Ожидаемый вывод: 5


main()