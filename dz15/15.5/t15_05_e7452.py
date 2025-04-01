class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToTail(self, val: int):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def PrintReverse(self):
        def reversePrint(node):
            if node:
                reversePrint(node.next)
                print(node.data, end=" ")

        reversePrint(self.head)
        print()

n = int(input().strip())
values = map(int, input().split())

linked_list = List()
for value in values:
    linked_list.addToTail(value)

linked_list.Print()
linked_list.PrintReverse()
