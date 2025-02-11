import math

def f(x):
    return x ** 3 + 4 * x ** 2 + x - 6

def root(a, b, significant_figures=1e-6):
    if f(a) * f(b) > 0:
        print("Немає кореня або їх парна кількість")
        return None
    while (b - a) > significant_figures:
        c = (a + b) / 2
        if abs(f(c)) < significant_figures:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

a, b = 0, 2
root = root(a, b)

if root is not None:
    print(root)
#1.0