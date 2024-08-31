# Main Author(s): Jagbir Singh
# Main Reviewer(s):

class SortedList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self.prev

    def __init__(self):
        self.front = self.Node(None)
        self.back = self.Node(None, None, self.front)
        self.front.next = self.back
        self._size = 0

    def get_front(self):
        if self.is_empty():
            return None
        return self.front.next

    def get_back(self):
        if self.is_empty():
            return None
        return self.back.prev

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def insert(self, data):
        new_node = self.Node(data)
        current = self.front.next
        while current != self.back and current.data < data:
            current = current.next

        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node
        self._size += 1
        return new_node

    def erase(self, node):
        if node is None or node == self.front or node == self.back:
            raise ValueError('Cannot erase node referred to by None')
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

    def search(self, data):
        current = self.front.next
        while current != self.back:
            if current.data == data:
                return current
            current = current.next
        return None
