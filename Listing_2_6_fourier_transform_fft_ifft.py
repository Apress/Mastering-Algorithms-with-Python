from cmath import sqrt 
from math import e, pi
i = sqrt(-1)

def fast_fourier_transform(Xn):
    N = len(Xn)
    if N == 1:
        return Xn 
    w = e**(2 * pi * i / N) 
    X_even, X_odd = Xn[::2], Xn[1::2]
    Y_even, Y_odd = fast_fourier_transform(X_even), fast_fourier_transform(X_odd)  
    Y = [0] * N 
    for j in range(N // 2):
        Y[j] = Y_even[j] + w**j * Y_odd[j]
        Y[j + N // 2] = Y_even[j] - w**j * Y_odd[j]
    return Y 

def IFFT_helper(Xn):   
    N = len(Xn)
    if N == 1:
        return Xn 

    w =  e**(-2 * pi * i / N)
    X_even, X_odd = Xn[::2], Xn[1::2]
    Y_even, Y_odd = IFFT_helper(X_even), IFFT_helper(X_odd)
    Y = [0] * N 
    for j in range(N // 2):
        Y[j] = Y_even[j] + w**j * Y_odd[j]
        Y[j + N // 2] = Y_even[j] - w**j * Y_odd[j]
    return Y

def inverse_fourier_transform(Xn):
    return [val / (len(Xn)) for val in  IFFT_helper(Xn)]

if __name__ == "__main__":  
    a_x = [-5, 4, 3, 2] 
    b_x = [-2, 2, 3, 5]
    print (fast_fourier_transform(a_x))
    print (fast_fourier_transform(b_x))

    #calculate the polynomial multiplication
    a_x_pad_zeros = a_x + [0] * len(a_x)
    b_x_pad_zeros = b_x + [0] * len(b_x)
    A_x = fast_fourier_transform(a_x_pad_zeros)
    B_x = fast_fourier_transform(b_x_pad_zeros)
    C_x = [A_x[i] * B_x[i] for i in range(len(A_x))]
    c_x = inverse_fourier_transform(C_x)
    print (c_x)