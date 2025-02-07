def main():
    n = int(input())
    collection = set(map(int, input().split()))
    m = int(input())
    butterflies = list(map(int, input().split()))
    for butterfly in butterflies:
        if butterfly in collection:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
