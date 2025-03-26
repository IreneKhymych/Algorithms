class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push_front(self, item):
        new_node = Node(item, None, self._front)
        if self._front:
            self._front.prev = new_node
        self._front = new_node
        if self._size == 0:
            self._back = new_node
        self._size += 1
        return "ok"

    def push_back(self, item):
        new_node = Node(item, self._back, None)
        if self._back:
            self._back.next = new_node
        self._back = new_node
        if self._size == 0:
            self._front = new_node
        self._size += 1
        return "ok"

    def pop_front(self):
        if self._size == 0:
            return "error"
        item = self._front.value
        self._front = self._front.next
        if self._front:
            self._front.prev = None
        else:
            self._back = None
        self._size -= 1
        return item

    def pop_back(self):
        if self._size == 0:
            return "error"
        item = self._back.value
        self._back = self._back.prev
        if self._back:
            self._back.next = None
        else:
            self._front = None
        self._size -= 1
        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._front.value

    def back(self):
        if self._size == 0:
            return "error"
        return self._back.value

    def size(self):
        return self._size

    def clear(self):
        self._front = self._back = None
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)

if __name__ == '__main__':
    deque = Deque()
    import sys
    for command in sys.stdin.read().strip().split("\n"):
        res = deque.execute(command.strip())
        print(res)
        if res == "bye":
            break
