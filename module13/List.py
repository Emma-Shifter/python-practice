class LinkedList:
    def __init__(self) -> None:
        self.__count = 0
        self.__head: Node = None
        self.__current_iter_item = self.__head
        self.__tail: Node = self.__head
    def append(self, item):
        node = Node(item)
        if self.__head is None:
            self.__head = node
            self.__tail = self.__head
        self.__tail.set_next(node)
        self.__tail = node
        self.__count += 1
    def get(self, index: int):
        if (index >= self.__count or index < 0): raise IndexError
        currentNode = self.__head
        currentIndex = 0
        while (currentIndex < index):
            currentNode = currentNode.get_next()
            currentIndex += 1
        return currentNode

    def remove(self, index: int):
        if (index >= self.__count or index < 0): raise IndexError
        currentNode = None
        currentIndex = 0
        while currentIndex <= index - 1:
            currentNode = currentNode.get_next() if currentNode is not None else self.__head
            currentIndex += 1
        deleteItem: Node = currentNode.get_next() if currentNode is not None else self.__head
        if (currentNode is not None): currentNode.set_next(deleteItem.get_next() if deleteItem is not None else None)
        if (deleteItem is self.__head): self.__head = deleteItem.get_next() if deleteItem is not None else None
        self.__count -= 1
        return currentNode
    def __iter__(self):
        self.__current_iter_item = self.__head
        return self
    def __next__(self):
        if (self.__current_iter_item is None): raise StopIteration
        else:
            returned = self.__current_iter_item
            self.__current_iter_item = self.__current_iter_item.get_next()
            return returned


class Node:
    def __init__(self, item) -> None:
        self.__item = item
        self.__next = None
    def set_next(self, node) -> None:
        self.__next = node
    def get_next(self):
        return self.__next
    def get_item(self):
        return self.__item