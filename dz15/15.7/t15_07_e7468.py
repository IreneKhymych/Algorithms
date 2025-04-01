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

    def ReorderList(self):
        if not self.head or not self.head.next:
            return

        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = self.head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

    def Print(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

n = int(input().strip())
values = map(int, input().split())

linked_list = List()
for value in values:
    linked_list.addToTail(value)

linked_list.ReorderList()
linked_list.Print()
