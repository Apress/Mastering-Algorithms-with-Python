import numpy as np 

def can_form_valid_triangle(a, b, c):
    if a + b > c  and a + c > b and b + c > a:
        return True
    return False 

def probability_form_a_triangle(num_trials = 100000):
    success = 0
    for i in range(num_trials):
        a, b, c = np.random.dirichlet(np.ones(3), size = 1)[0]
        if can_form_valid_triangle(a, b, c):
            success += 1
    return success / num_trials

if __name__ == "__main__":
    print (probability_form_a_triangle())