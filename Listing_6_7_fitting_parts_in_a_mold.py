import numpy as np 
np.random.seed(1234)
def prob_fitting_parts_in_a_mold(num_trials=1000000):
    length_mold = 15
    part_1_length = np.random.triangular(3.5,4,5, num_trials)
    part_2_length = np.random.normal(6,1, num_trials)
    part_3_length = np.random.uniform(4.5, 5.5, num_trials)
    total_part_length = part_1_length + part_2_length + part_3_length
    num_success_trials = sum(total_part_length <=length_mold)
    return num_success_trials / num_trials

if __name__ == "__main__":
    print (prob_fitting_parts_in_a_mold())
    
