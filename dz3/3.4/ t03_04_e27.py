def cyclic(n):
    binary = bin(n)[2:]
    shifts = [binary[i:] + binary[:i] for i in range(len(binary))]
    max_value = max(int(shift, 2) for shift in shifts)
    return max_value

print(cyclic(int(input())))
