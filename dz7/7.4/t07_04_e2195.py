import sys
import re

N, M = map(int, sys.stdin.readline().split())
dict = {sys.stdin.readline().strip().lower() for _ in range(N)}
text = set()

for _ in range(M):
    line = sys.stdin.readline().strip().lower()
    words = re.findall(r"[a-z]+", line)
    text.update(words)

if text == dict:
    print("Everything is going to be OK.")
elif text - dict:
    print("Some words from the text are unknown.")
else:
    print("The usage of the vocabulary is not perfect.")
