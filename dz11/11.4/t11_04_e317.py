import sys
sys.set_int_max_str_digits(10000)

def multiply(a: str, b: str) -> str:
    a, b = a[::-1], b[::-1]
    result = [0] * (len(a) + len(b))

    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] += int(a[i]) * int(b[j])
            if result[i + j] >= 10:
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return ''.join(map(str, result[::-1]))

def karatsuba(x: str, y: str) -> str:
    if len(x) == 1 or len(y) == 1:
        return str(int(x) * int(y))

    max_len = max(len(x), len(y))
    half = max_len // 2
    x, y = x.zfill(max_len), y.zfill(max_len)
    a, b = x[:-half], x[-half:]
    c, d = y[:-half], y[-half:]
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(str(int(a) + int(b)), str(int(c) + int(d)))
    ad_plus_bc = str(int(ad_plus_bc) - int(ac) - int(bd))
    result = int(ac) * (10 ** (2 * half)) + int(ad_plus_bc) * (10 ** half) + int(bd)

    return str(result)

def main():
    with open("input.txt", "r") as f:
        a, b = f.readline().split()

    if len(a) < 10 or len(b) < 10:
        result = multiply(a, b)
    else:
        result = karatsuba(a, b)

    with open("output.txt", "w") as f:
        f.write(result + "\n")

if __name__ == "__main__":
    main()
