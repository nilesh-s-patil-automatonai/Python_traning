def add_without_plus_operator(a, b):
    while b != 0:
        result = a & b
        a = a ^ b
        b = result << 1
    return a
print(add_without_plus_operator(2, 3))
