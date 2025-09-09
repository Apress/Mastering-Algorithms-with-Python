# Calculation of Pi
# Using Monte Carlo method
# Given a unit square and a circle inscribed inside of it.
# The pi would be the ratio * 4 where ratio is number of times a random point (x, y) with -1<= x, y <=1
# falls inside of the circle between that falls inside the unit square.
import numpy as np 
import matplotlib.pyplot as plt
np.random.seed(1234)

def compute_pi(N_trials):
    x = np.random.uniform(low=-1.0, high=1.0, size=N_trials)
    y = np.random.uniform(low=-1.0, high=1.0, size=N_trials)
    inside_circle = x ** 2 + y ** 2 <= 1
    pi = 4.0 * np.sum(inside_circle) / N_trials
    return pi

x = [10**i for i in range(8)]
y = [compute_pi(i) for i in x]
x_log = [np.log10(i) for i in x]
plt.plot(x_log, y, 'bo-', markersize = 12)
plt.xlabel('Number of trials, log10', fontsize = 12)
plt.ylabel('Computed Pi', fontsize = 12)
plt.title('Compute Pi with Monte Carlo')
plt.hlines(np.pi, min(x_log), max(x_log), 'r', 'dotted', lw=2)
plt.tight_layout()
plt.show() 