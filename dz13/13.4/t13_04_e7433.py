A = input().strip()
P = input().strip()

def convert(A, P):
    stack = []

    A = int(A)
    P = int(P)

    while A > 0:
        remainder = A % P
        stack.append(remainder)
        A //= P
    result = []

    while stack:
        digit = stack.pop()
        if digit > 9:
            result.append(f"[{digit}]")
        else:
            result.append(str(digit))

    return "".join(result)

print(convert(A, P))
