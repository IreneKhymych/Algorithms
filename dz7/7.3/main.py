N = int(input())
phone_book = {}
for number in input().split():
    phone_book[number] = True
print(len(phone_book))
