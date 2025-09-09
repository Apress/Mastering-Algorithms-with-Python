import random 
random.seed(1234)
class RSA:
    def __init__(self):
        self.num_bits = 1000 # number of bits for p and q

    def fast_modular_arithmetic(self, base, exponent, N):
        # calculate modular operations using repeated squaring
        # base ** exponent % N
        if exponent == 0:
            return 1 
        
        z = self.fast_modular_arithmetic(base, exponent // 2, N)
        if exponent % 2 == 0:
            return z**2 % N 
        else:
            return base * z**2 % N 

    def greatest_common_divisor(self, num_1, num_2):
        # make sure num_1 >= num_2
        if num_1 < num_2:
            num_1, num_2 = num_2, num_1

        if num_2 == 0:
            return num_1
        else:
            return self.greatest_common_divisor(num_2, num_1 % num_2)

    def extended_euclid(self, num_1, num_2):
        # make sure num_1 >= num_2
        if num_1 < num_2:
            num_1, num_2 = num_2, num_1

        if num_2 == 0:
            return num_1, 1, 0

        d, alpha, beta = self.extended_euclid(num_2, num_1 % num_2)
        return d, beta, alpha - num_1 // num_2 * beta         

    def generate_random_prime(self):
        large_num = random.getrandbits(self.num_bits)
        while not self.primality_test(large_num):
            large_num = random.getrandbits(self.num_bits)
        return large_num

    def primality_test(self, large_num, k = 200):
        k_random_nums = [random.randint(0, large_num) for _ in range(k)]
        for num in k_random_nums:
            if self.fast_modular_arithmetic(num, large_num - 1, large_num) != 1:
                return False # not a prime
        return True 

    def find_p_q_e(self):
        possible_e_vals = [3, 5, 7, 11, 13, 17, 19]
        while True:
            p, q = self.generate_random_prime(), self.generate_random_prime()
            totient = (p-1) * (q-1) 

            for e in possible_e_vals:
                if self.greatest_common_divisor(totient, e) == 1:
                    return p, q, e 

    def rsa_encrypt(self, message):
        p, q, e = self.find_p_q_e()
        N = p * q 
        totient = (p - 1) * (q - 1)
        _, _, d = self.extended_euclid(e, totient) # keep d secret
        d = d % totient
        if d < 0:
            d += totient
        # publish public key (N, e)
        print (f"p --> {p}")
        print (f"q --> {q}")
        print (f"e --> {e}")
        print (f"N --> {N}")
        print (f"d --> {d}")
        print (f"totient --> {totient}")
        print (f"message --> {message}")
        # encrypt 
        encrypted_msg = self.fast_modular_arithmetic(message, e, N)
        return encrypted_msg, d, e, N   

    def rsa_decrypt(self, message, d, N):
        decrypted_msg = self.fast_modular_arithmetic(message, d, N)
        return decrypted_msg
         
if __name__ == "__main__":
    rsa = RSA()
    message = 831169712132104117110103114121463283116971213210211111110810511510433
    print (f"Original message is {message}")
    encrypted_msg, d, e, N  = rsa.rsa_encrypt(message)
    print (f"Encrypted message is {encrypted_msg}")
    decrypted_msg = rsa.rsa_decrypt(encrypted_msg, d, N)
    print (f"Decrypted message is {decrypted_msg}")


