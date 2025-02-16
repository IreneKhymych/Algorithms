import sys
import re

N, M = map(int, sys.stdin.readline().split())
dict = {sys.stdin.readline().strip().lower() for _ in range(N)}
text_words = set()

for _ in range(M):
    line = sys.stdin.readline().strip().lower()
    words = re.findall(r"[a-z]+", line)
    text_words.update(words)

if text_words == dict:
    print("Everything is going to be OK.")
elif text_words - dict:
    print("Some words from the text are unknown.")
else:
    print("The usage of the vocabulary is not perfect.")
