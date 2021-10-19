
# Shift cipher
def shift(plain, key):
    if plain.isalnum() == False:
        raise ValueError("Plaintext should be alphanumeric")
        
    ctext = ""
    for c in plain:
        if c.islower():
            ctext += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
        elif c.isupper():
            ctext += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
        # numeric is not shifted
        else:
            ctext += c
    return ctext
# Unshift operation for shift cipher
def unshift(cipher, key):
    if cipher.isalnum() == False:
        raise ValueError("Ciphertext should be alphanumeric")
            
    ctext = ""
    for c in cipher:
        if c.islower():
            ctext += chr((ord(c) - ord('a') - key) % 26 + ord('a'))
        elif c.isupper():
            ctext += chr((ord(c) - ord('A') - key) % 26 + ord('A'))
        # numeric is not shifted
        else:
            ctext += c
    return ctext

