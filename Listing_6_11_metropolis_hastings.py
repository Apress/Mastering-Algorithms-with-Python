import numpy as np 
import matplotlib.pyplot as plt 
import random 
from scipy import integrate
random.seed(1234)

def P(x):
    return 2*np.exp(-(x + 4)**2/2) + 3*np.exp(-x**2/2) + np.exp(-(x-3)**2/2)

def plot_target_distribution(x_arr, y_arr):
    plt.xlabel("x", fontsize = 12)
    plt.ylabel("Target Distribution (unnormalized)", fontsize = 12)
    plt.plot(x_arr, y_arr, 'b-', label='P(x)')
    plt.legend(loc='upper right', shadow=True)
    plt.tight_layout()
    plt.show()    

def metropolis_hasting(num_iter=100000, burn_in_ratio = 0.5, start_x = 0, sigma = 1):
    samples = []
    prev_x = start_x
    num_accept = 0
    num_reject = 0
    for _ in range(num_iter):
        proposal_x = random.normalvariate(prev_x, sigma)
        accept_prob = min(P(proposal_x) / P(prev_x), 1)
        U = random.uniform(0,1)
        if accept_prob > U:
            new_x = proposal_x
            num_accept += 1
        else:
            new_x = prev_x
            num_reject += 1
        samples.append(new_x)
        prev_x = new_x 
    acceptance_rate = num_accept / num_iter
    print (acceptance_rate)
    return samples[int(num_iter * burn_in_ratio):]

def plot_samples_from_metropolis_hasting(x_arr, y_arr, Z, samples):
    plt.hist(samples, bins=50, histtype='bar', facecolor='g', alpha=0.75, density=1, label='bins')
    plt.xlabel("x", fontsize = 12)
    plt.ylabel("Distribution (normalized)", fontsize = 12)
    plt.plot(x_arr, y_arr/Z, 'r', label='P(x)')
    plt.title('Metropolis Hastings')
    plt.legend(loc='upper right', shadow=True)
    plt.show()

if __name__ == "__main__":
    x_arr = np.linspace(-10, 10, 1000)
    y_arr = P(x_arr)
    Z, error = integrate.quad(P, -10, 10)
    samples = metropolis_hasting(num_iter=100000, burn_in_ratio = 0.5, start_x = 0, sigma = 1)
    plot_target_distribution(x_arr, y_arr)
    plot_samples_from_metropolis_hasting(x_arr, y_arr, Z, samples)


