sequence = input().strip()

def bracket_sequence(s):
    stack = []
    bracket = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != bracket[char]:
                return "no"
            stack.pop()
    return "yes" if not stack else "no"

print(bracket_sequence(sequence))
