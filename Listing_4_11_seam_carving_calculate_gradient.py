import numpy as np
def calculate_gradient(I):
    R, C = len(I), len(I[0])
    Ix = [[0 for _ in range(C)] for _ in range(R)] 
    Iy = [[0 for _ in range(C)] for _ in range(R)] 
    # calculate Ix 
    for c in range(C):
        Ix[0][c] = I[1][c] - I[0][c]
        Ix[R-1][c] = I[R-1][c] - I[R-2][c]
    for r in range(1, R-1):
        for c in range(C):
            Ix[r][c] = (I[r+1][c] - I[r-1][c]) / 2
    # calculate Iy
    for r in range(R):
        Iy[r][0] = I[r][1] - I[r][0]
        Iy[r][C-1] = I[r][C-1] - I[r][C-2]
    for r in range(R):
        for c in range(1, C-1):
            Iy[r][c] = (I[r][c+1] - I[r][c-1]) /2
    return Ix, Iy
 
def calculate_energy(Ix, Iy):
    R, C = len(Ix), len(Ix[0])
    E = [[0 for _ in range(C)] for _ in range(R)] 
    for r in range(R):
        for c in range(C):
            E[r][c] = abs(Ix[r][c]) + abs(Iy[r][c])   
    return E

if __name__ == "__main__":
    """
    Given a 2D image matrix calculate its gradient along x, y axes
        I = [1 2 1]
            [0 0 1]
            [3 2 1]
        Ix = [-1 -2 0]
             [1 0 0]
             [3 2 0]
        Iy = [1 0 -1]
             [0 0.5 1]
             [-1 -1 -1]
    The result should be equivalent to np.gradient(I)
    x|
     |
     |
     |
    y ------------
    """
    I = [[1, 2, 1],
         [0, 0, 1],
         [3, 2, 1]]
    print (np.gradient(I)[0])
    print (np.gradient(I)[1])
    print (calculate_gradient(I)[0])
    print (calculate_gradient(I)[1])