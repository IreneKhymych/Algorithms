import sys

def train(n, order):
    stack = []
    current = 1

    for wagon in order:
        while current <= n and (not stack or stack[-1] != wagon):
            stack.append(current)
            current += 1

        if stack and stack[-1] == wagon:
            stack.pop()
        else:
            return "No"

    return "Yes"

def main():
    input_data = sys.stdin.read().strip().split("\n")
    i = 0

    while i < len(input_data):
        n = int(input_data[i])
        if n == 0:
            break
        i += 1

        results = []
        while i < len(input_data) and input_data[i] != "0":
            order = list(map(int, input_data[i].split()))
            results.append(train(n, order))
            i += 1

        print("\n".join(results))
        print()
        i += 1

if __name__ == "__main__":
    main()
