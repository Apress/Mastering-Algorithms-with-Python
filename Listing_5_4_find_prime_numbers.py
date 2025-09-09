import math
def is_an_odd_number_prime_number(odd_num):
    upper_bound = math.floor(math.sqrt(odd_num))
    for divisor in range(3, upper_bound + 1):
        if divisor % 2 == 1 and odd_num % divisor == 0:
            return False
    return True 

def find_prime_numbers_modulo_method(num_digits):
    if num_digits == 1:
        return [2,3,5,7]
    
    prime_numbers = []
    for num in range(10 ** (num_digits - 1), 10 ** num_digits):
        if  num % 2 == 1 and is_an_odd_number_prime_number(num): # num must be an odd number to be a prime number:
            prime_numbers.append(num)
    print (f"There are in total {len(prime_numbers)} prime numbers for a number of {num_digits} digits")
    return prime_numbers

if __name__ == '__main__':
    print (find_prime_numbers_modulo_method(2))
