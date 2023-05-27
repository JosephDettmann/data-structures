class LinkedList:
    def __init__(self, vals):
        self.head = None
        current = None

    def insert(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node


class Node:
    def __init__(self, val):
        self.val = None
        self.next = None
