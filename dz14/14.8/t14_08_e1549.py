class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push_back(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def push_front(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def pop_front(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.count -= 1
        return value

    def size(self):
        return self.count

def rotate(deq, r):
    for _ in range(r):
        deq.push_back(deq.pop_front())

while True:
    line = input().strip()
    if not line:
        continue
    n, m, k = map(int, line.split())

    if n == 0 and m == 0 and k == 0:
        break
    circle = Deque()
    for _ in range(n):
        circle.push_back("G")
    for _ in range(m):
        circle.push_back("K")

    while circle.size() > 1:
        rotate(circle, (k - 1) % circle.size())
        sacrifice1 = circle.pop_front()
        rotate(circle, (k - 1) % circle.size())
        sacrifice2 = circle.pop_front()
        new_servant = "G" if sacrifice1 == sacrifice2 else "K"
        circle.push_front(new_servant)
        rotate(circle, 1)

    print("Gared" if circle.pop_front() == "G" else "Keka")
