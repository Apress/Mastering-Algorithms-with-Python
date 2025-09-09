def multiply_n_bits_integers(x, y):
    binary_x = bin(x)[2:]
    binary_y = bin(y)[2:]
    n_x = len(binary_x)
    n_y = len(binary_y)

    if n_x == 1 or n_y == 1:
        return x * y 
    
    n = max(n_x, n_y)
    if n % 2 == 1:
        n += 1
    binary_x = binary_x.zfill(n)
    binary_y = binary_y.zfill(n)

    x_left = int(binary_x[: n//2], 2)
    x_right = int(binary_x[n //2: ], 2)
    y_left = int(binary_y[:n//2], 2)
    y_right = int(binary_y[n//2: ], 2)
    A = multiply_n_bits_integers(x_left, y_left)
    B = multiply_n_bits_integers(x_right, y_right)
    C = multiply_n_bits_integers(x_left + x_right, y_left + y_right) 
    return 2**n * A + 2**(n // 2) * (C - A - B) + B 
    
if __name__ == "__main__":
    print (multiply_n_bits_integers(11, 9) == 11 * 9)
    print (multiply_n_bits_integers(123, 45678) == 123 * 45678)

