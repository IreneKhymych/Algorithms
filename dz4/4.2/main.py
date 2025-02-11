C = float(input())

def x(C):
    left, right = 0, C
    significant_figures = 1e-7
    while right - left > significant_figures:
        mid = (left + right) / 2
        if mid ** 2 + mid ** 0.5 < C:
            left = mid
        else:
            right = mid
    return round(left, 6)

print(x(C))
