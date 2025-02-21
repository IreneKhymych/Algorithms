import sys
import re

class HashTable:
    def __init__(self, size=2003):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def add(self, key):
        key = key.lower()
        index = self._hash(key)
        if self.contains(key):
            return
        node = (key, self.table[index])
        self.table[index] = node

    def contains(self, key):
        key = key.lower()
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current[0] == key:
                return True
            current = current[1]
        return False

    @staticmethod
    def extract_words(text):
        return re.findall(r"[a-zA-Z]+", text.lower())

    def check(self, vocab_lines, text_lines):
        vocabulary = HashTable()
        for word in vocab_lines:
            vocabulary.add(word.strip())

        text_words = HashTable()
        for line in text_lines:
            for word in self.extract_words(line):
                text_words.add(word)

        words = True
        for bucket in text_words.table:
            current = bucket
            while current:
                if not vocabulary.contains(current[0]):
                    words = False
                    break
                current = current[1]

        used = True
        for bucket in vocabulary.table:
            current = bucket
            while current:
                if not text_words.contains(current[0]):
                    used = False
                    break
                current = current[1]

        if words and used:
            return "Everything is going to be OK."
        elif not words:
            return "Some words from the text are unknown."
        else:
            return "The usage of the vocabulary is not perfect."

n, m = map(int, sys.stdin.readline().split())
vocab = [sys.stdin.readline().strip() for _ in range(n)]
text = [sys.stdin.readline().strip() for _ in range(m)]

print(HashTable().check(vocab, text))


