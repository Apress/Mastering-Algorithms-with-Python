import numpy as np 
# calculate the stationary distribution programatically 
Q = np.array([[0.9, 0.1],[0.5, 0.5]])
init_s = np.array([[1, 0]])
epsilon =1 
while epsilon>10e-9:
    next_s = np.dot(init_s,Q)
    epsilon = np.sqrt(np.sum(np.square(next_s - init_s)))
    init_s = next_s
print(init_s)