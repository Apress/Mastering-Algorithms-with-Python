import math
def find_prime_numbers_eratosthenes_method(num_digits):
    if num_digits == 1:
        return [2,3,5,7]
    min_num = 10 ** (num_digits - 1)
    max_num = 10 ** num_digits - 1
    # all odd numbers within the range can be the candidates for prime numbers
    prime_numbers_candidates = set([num for num in range(min_num, max_num) if num % 2 == 1]) 
    pseudo_prime_numbers = [num for num in range(3, math.floor(math.sqrt(max_num)) + 1) if num % 2 == 1]
    for pseudo_prime_number in pseudo_prime_numbers:
        multiplier = 2
        while pseudo_prime_number * multiplier <= max_num:
            if pseudo_prime_number * multiplier in prime_numbers_candidates:
                prime_numbers_candidates.remove(pseudo_prime_number * multiplier)
            multiplier += 1
    print (f"There are in total {len(prime_numbers_candidates)} prime numbers for a number of {num_digits} digits")
    return prime_numbers_candidates

if __name__ == '__main__':
    find_prime_numbers_eratosthenes_method(5)