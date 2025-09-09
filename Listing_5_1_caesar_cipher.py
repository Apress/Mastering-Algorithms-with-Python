from string import ascii_lowercase, ascii_uppercase 

def caesar_cipher_encrypt(message, shift):
    encrypted_msg = ""
    for char in message:
        if char in ascii_lowercase:
            char_index = ascii_lowercase.index(char)
            new_char_index = (char_index + shift) % 26
            encrypted_msg += ascii_lowercase[new_char_index]
        elif char in ascii_uppercase:
            char_index = ascii_uppercase.index(char)
            new_char_index = (char_index + shift) % 26
            encrypted_msg += ascii_uppercase[new_char_index]
        else:
            encrypted_msg += char
    return encrypted_msg

def caesar_cipher_decrypt(message, shift):
    return caesar_cipher_encrypt(message, -shift) 

if __name__ == "__main__":
    message = "Stay hungry. Stay foolish."
    shift = 3
    encrypted_msg = caesar_cipher_encrypt(message, shift)
    decrypted_msg = caesar_cipher_decrypt(encrypted_msg, shift)
    print ("encrypted msg:", encrypted_msg)
    print ("decrypted msg:", decrypted_msg)
    assert message == decrypted_msg