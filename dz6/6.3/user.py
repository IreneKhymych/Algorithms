import math

EMPTY = "EMPTY"
DELETED = "DELETED"

size: int = 11
count: int
keys: list[tuple[str, str]]
values: list[str]

def prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def rehash():
    global size
    size = size * 2 + 1
    while not prime(size):
        size += 2

    _keys = keys
    _values = values
    init()
    for i in range(len(_keys)):
        if _keys[i] not in (EMPTY, DELETED):
            addBook(_keys[i][0], _keys[i][1])

def hash_key(author: str, title: str):
    return hash((author, title)) % size

def init():
    global count, keys, values
    count = 0
    keys = [EMPTY for _ in range(size)]
    values = [EMPTY for _ in range(size)]

def addBook(author: str, title: str) -> None:
    global count

    if size * 0.7 < count:
        rehash()

    i = hash_key(author, title)
    j = -1
    while keys[i] is not EMPTY:
        if keys[i] == (author, title):
            values[i] = title
            return
        if j == -1 and keys[i] == DELETED:
            j = i
        i = (i + 1) % size

    if j == -1:
        j = i
    count += 1
    keys[j] = (author, title)
    values[j] = title

def find(author: str, title: str):
    i = hash_key(author, title)
    while keys[i] is not EMPTY:
        if keys[i] == (author, title):
            return True
        i = (i + 1) % size
    return False

def delete(author: str, title: str) -> None:
    i = hash_key(author, title)
    while keys[i] is not EMPTY:
        if keys[i] == (author, title):
            keys[i] = DELETED
            values[i] = DELETED
            return
        i = (i + 1) % size

def findByAuthor(author: str):
    books = [values[i] for i in range(size) if keys[i] is not EMPTY and keys[i] is not DELETED and keys[i][0] == author]
    return sorted(books)

