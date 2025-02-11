def min_x():
    left, right = 0, 10
    significant_figures = 1e-7
    while right - left > significant_figures:
        mid = (left + right) / 2
        if mid**3 + mid + 1 > 5:
            right = mid
        else:
            left = mid
    return round(right, 6)
result = min_x()
print(result)
#1.378797