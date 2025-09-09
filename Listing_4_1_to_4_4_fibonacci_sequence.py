"""
Fibonacci sequence
0 1 1 2 3 5 8 13 21 34 55 89... 
F(n) = F(n-1) + F(n-2) 
"""
# method 1: recursive
def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n 
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# method 2: dynamic programming
def fibonacci_dynamic_programming(n):
    if n == 0 or n == 1:
        return n 
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

# method 3: dynamic programming no extra space
def fibonacci_dynamic_programming_no_extra_space(n):
    if n == 0 or n == 1:
        return n 
    counter = 1
    fib_num_two_steps_back = 0
    fib_num_one_step_back = 1
    while counter < n:
        fib_num_current = fib_num_two_steps_back + fib_num_one_step_back
        fib_num_two_steps_back = fib_num_one_step_back
        fib_num_one_step_back = fib_num_current
        counter += 1
    return fib_num_current

# method 4: mathematical expression
def fibonacci_mathematical_expression(n):
    phi = (1 + 5 ** 0.5) / 2
    numerator = phi ** n - (-phi)**(-n)
    denominator = 2 * phi - 1
    return numerator / denominator

if __name__ == "__main__": 
    #print (fibonacci_recursive(100)) # don't run this! Computer crash!
    print (fibonacci_dynamic_programming(50))
    print (fibonacci_dynamic_programming_no_extra_space(50))
    print (fibonacci_mathematical_expression(50))

    