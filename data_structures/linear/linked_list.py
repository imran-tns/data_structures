class Node:
    """A node in a linked list."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    """A linked list."""

    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.size = 0

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.size += 1

    def remove(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def index(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def __setitem__(self, index, data):
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def __getitem__(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return repr(self.head)
