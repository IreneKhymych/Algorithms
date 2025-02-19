import random

EMPTY = "EMPTY"
DELETED = "DELETED"

size: int = 11
count: int = 0
keys: list[list[tuple[str, str]]]
values: list[list[str]]

def init():
    global table, size, count, keys, values
    size = 11
    count = 0
    table = [[] for _ in range(size)]
    keys = [[] for _ in range(size)]
    values = [[] for _ in range(size)]

def _hash(author):
    return hash(author) % size

def addBook(author, title):
    index = _hash(author)
    for book in table[index]:
        if book[0] == author and book[1] == title:
            return
    table[index].append((author, title))
    keys[index].append((author, title))
    values[index].append(title)

def find(author, title):
    index = _hash(author)
    return any(book[0] == author and book[1] == title for book in table[index])

def delete(author, title):
    index = _hash(author)
    table[index] = [(a, t) for a, t in table[index] if not (a == author and t == title)]
    keys[index] = [(a, t) for a, t in keys[index] if not (a == author and t == title)]
    values[index] = [t for t in values[index] if t != title]

def findByAuthor(author):
    index = _hash(author)
    books = [title for a, title in table[index] if a == author]
    return sorted(books)

def restoreDeleted():
    if count == 0:
        return None
    num = random.randint(0, size - 1)
    while not table[num]:
        num = random.randint(0, size - 1)
    return table[num][0]
