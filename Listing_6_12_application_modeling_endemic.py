import random 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp 
random.seed(1234)

def sir_model_func(t, z, beta, gamma):
    S, I, R = z
    N = S + I + R 
    dS_dt = -beta * I * S / N 
    dI_dt = beta * I * S / N - gamma * I 
    dR_dt = gamma * I  
    return [dS_dt, dI_dt, dR_dt]

def solve_using_scipy_ode_solver(beta, gamma, S_0, I_0, R_0, num_days):
    t_span = [0, num_days]
    initial_state = [S_0, I_0, R_0]
    ode_solution = solve_ivp(sir_model_func, t_span, initial_state, args=(beta, gamma), dense_output=True)
    t = [i for i in range(num_days)]
    z = ode_solution.sol(t)
    S, I, R = z 
    return S, I, R, t 

def sir_model_monte_carlo(beta, gamma, S_0, I_0, R_0, num_days):
    N = S_0 + I_0 + R_0 
    # denote 0: susceptibles; 1: infected; 2: recovered
    S = [0 for _ in range(num_days)]
    I = [0 for _ in range(num_days)]
    R = [0 for _ in range(num_days)]
    population = [0 for _ in range(S_0)] + [1 for _ in range(I_0)] + [2 for _ in range(R_0)]
    random.shuffle(population)

    for n in range(num_days):
        num_susceptibles = population.count(0)
        num_infected = population.count(1)
        num_recovered = population.count(2)
        S[n] = num_susceptibles
        I[n] = num_infected
        R[n] = num_recovered
        for i in range(int(num_infected)):
            if random.random() < beta:
                rand_index = random.randint(0, N-1)
                if population[rand_index] == 0:
                    population[rand_index] = 1

        for i in range(int(num_infected)):                
            if random.random() < gamma:
                while True:
                    rand_index = random.randint(0, N-1)
                    if population[rand_index] == 1:
                        population[rand_index] = 2
                        break 
    t = [i for i in range(num_days)]
    return S, I, R, t

def run_monte_carlo_multiple_times(num_trials, beta, gamma, S_0, I_0, R_0, num_days):
    S = np.zeros(num_days)
    I = np.zeros(num_days)
    R = np.zeros(num_days)

    for _ in range(num_trials):
        cur_S, cur_I, cur_R, t = sir_model_monte_carlo(beta, gamma, S_0, I_0, R_0, num_days)
        S += np.array(cur_S)
        I += np.array(cur_I)
        R += np.array(cur_R)
    S /= num_trials
    I /= num_trials
    R /= num_trials
    return S, I, R, t 

def plot_results(S1, I1, R1, S2, I2, R2, t):
    y_data = [S1, I1, R1, S2, I2, R2]
    labels = ["S1", "I1", "R1", "S2", "I2", "R2"]
    symbols = ["b-", "r-", "g-", "b--", "r--", "g--"]
    for y, label, symbol in zip(y_data, labels, symbols):
        plt.plot(t, y, symbol, lw=2, label = label)
    plt.xlabel('Time (days)', fontsize = 12)
    plt.ylabel('Population', fontsize = 12)
    plt.legend(loc=0)
    plt.title('SIR Model')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    conditions = dict(beta=0.04, gamma=0.1, S_0 = 900, I_0=100, R_0=0, num_days=50)
    S1, I1, R1, t = solve_using_scipy_ode_solver(**conditions)
    S2, I2, R2, t = run_monte_carlo_multiple_times(num_trials=1000, **conditions) 
    plot_results(S1, I1, R1, S2, I2, R2, t)


