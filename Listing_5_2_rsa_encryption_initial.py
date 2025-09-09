import math 

def rsa_encrypt(p, q, message):
    N = p * q 
    t = (p -1) * (q - 1) # totient
    e = 2
    while e < t:
        if math.gcd(e, t) == 1:
            break 
        e += 1
    d = 0
    while True:
        if d * e % t == 1:
            break
        d += 1
    # encryption
    encrypted_text = pow(message, e, N)
    return encrypted_text, d, e, N 

def rsa_decrypt(message, d, N):
    # decryption
    decrypted_text = pow(message, d, N)
    return decrypted_text

if __name__ == "__main__":
    p, q, message = 53, 59, 89
    print (f"Original message is {message}")
    encrypted_msg, d, e, N = rsa_encrypt(p, q, message)
    print (f"Encrypted message is {encrypted_msg}")
    decrypted_msg = rsa_decrypt(encrypted_msg, d, N)
    print (f"Decrypted message is {decrypted_msg}")

