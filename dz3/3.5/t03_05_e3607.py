def heights(arr, a, b):
    count = 0
    for i in arr:
        if a <= i <= b:
            count += 1
    return count

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            arr = [int(x) for x in input().split()]
            a, b = map(int, input().split())
            print(heights(arr, a, b))
        except EOFError:
            break
        except ValueError:
            print("Неправильний формат вводу")
