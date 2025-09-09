"""
Given
P(R-tomorrow|R-today) = 0.5
P(S-tomorrow|R-today) = 0.5
P(R-tomorrow|S-today) = 0.1
P(S-tomorrow|S-today) = 0.9
What is probability it rains on a random day? 
Answer: P(S) = 0.833 and P(R) = 0.167
"""
import random 
from collections import Counter 
import matplotlib.pyplot as plt 
import numpy as np 
random.seed(1234)

def generate_mcmc_chain(chain_length):
    chain = ["R" if random.random() <= 0.5 else "S"]
    for i in range(chain_length - 1):
        if chain[-1] == "R":
            if random.random() <= 0.5:
                chain.append("R")
            else:
                chain.append("S")
        else:
            if random.random() <= 0.1:
                chain.append("R")
            else:
                chain.append("S")
    count_dict = Counter(chain)
    num_sunny_days = count_dict["S"]
    num_rainy_days = count_dict["R"]
    percent_rainy = num_rainy_days / chain_length
    print (f"chain_length: {chain_length}")
    print (f"number sunny days: {num_sunny_days}")
    print (f"number rainy days: {num_rainy_days}")
    return percent_rainy

length_chain_arr = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
percent_rainy_arr = [generate_mcmc_chain(length) for length in length_chain_arr]
percent_sunny_arr = [1 - percent_rain for percent_rain in percent_rainy_arr]
plt.figure(figsize=(10,7))
plt.plot(range(2, len(length_chain_arr) + 2), percent_rainy_arr, "bD-", markersize = 14,lw = 2, label = "probability of rainy on a random day")
plt.plot(range(2, len(length_chain_arr) + 2), percent_sunny_arr, "rD-", markersize = 14,lw = 2, label = "probability of sunny on a random day")
plt.xlabel("Length of Markov Chain in 10 base exponential", fontsize = 16)
plt.ylabel("Probability of Rain", fontsize = 16)
plt.legend(loc= 0)
plt.title("Probability of rainy on a random day with Markov Chain length", fontsize = 18)
plt.grid()
plt.tight_layout()
plt.show()

