import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# key = os.urandom(32)
# print("carotte = ", int.from_bytes(key) % 17488856370348678479)
# print("radis   = ", int.from_bytes(key) % 16548497022403653709)
# print("tomate  = ", int.from_bytes(key) % 17646308379662286151)
# print("pomme   = ", int.from_bytes(key) % 14933475126425703583)
# print("banane  = ", int.from_bytes(key) % 17256641469715966189)

# flag = open("flag.txt", "rb").read()
# E = AES.new(key, AES.MODE_ECB)
# enc = E.encrypt(pad(flag, 16))
# print(f"enc = {enc.hex()}")

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import math
from functools import reduce

# Extended Euclidean Algorithm to find Bezout coefficients
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

# Find modular multiplicative inverse
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# Chinese Remainder Theorem
def chinese_remainder_theorem(remainders, moduli):
    # Check if all moduli are pairwise coprime
    for i in range(len(moduli)):
        for j in range(i+1, len(moduli)):
            if math.gcd(moduli[i], moduli[j]) != 1:
                raise Exception(f"Moduli {moduli[i]} and {moduli[j]} are not coprime")
    
    product = reduce(lambda a, b: a * b, moduli)
    result = 0
    
    for i in range(len(remainders)):
        ai = remainders[i]
        mi = moduli[i]
        ni = product // mi
        inv = mod_inverse(ni, mi)
        result = (result + ai * ni * inv) % product
    
    return result

# The moduli from the original code
moduli = [
    17488856370348678479,  # carotte
    16548497022403653709,  # radis
    17646308379662286151,  # tomate
    14933475126425703583,  # pomme
    17256641469715966189,  # banane
]

# The actual output values from the original program
remainders = [
    392278890668246705,  # carotte
    4588810924820033807,  # radis
    17164682861166542664,  # tomate
    12928514648456294931,  # pomme
    5973470563196845286,  # banane
]

# The encrypted flag
enc_hex = "2da1dbe8c3a739d9c4a0dc29a27377fe8abc1c0feacc9475019c5954bbbf74dcedce7ed3dc3ba34fa14a9181d4d7ec0133ca96012b0a9f4aa93c42c61acbeae7640dd101a6d2db9ad4f3b8ccfe285e0d"

def main():
    try:
        # Apply Chinese Remainder Theorem
        print("Applying Chinese Remainder Theorem...")
        reconstructed_value = chinese_remainder_theorem(remainders, moduli)
        print(f"Reconstructed value: {reconstructed_value}")
        
        # Since os.urandom(32) produces a 32-byte (256-bit) key
        # Our value might be larger than 2^256, so we need to consider modulo 2^256
        key_max = 2**256
        possible_key = reconstructed_value % key_max
        print(f"Possible 256-bit key: {possible_key}")
        
        # Convert to 32 bytes for AES
        key_bytes = possible_key.to_bytes(32, byteorder='big')
        print(f"Key in hex: {key_bytes.hex()}")

        # Decrypt using AES-ECB
        ciphertext = bytes.fromhex(enc_hex)
        cipher = AES.new(key_bytes, AES.MODE_ECB)
        decrypted = cipher.decrypt(ciphertext)
        
        # Try to unpad and print the flag
        try:
            flag = unpad(decrypted, 16)
            print(f"Decrypted flag: {flag.decode('utf-8')}")
        except Exception as e:
            print(f"Unpadding error: {e}")
            print(f"Raw decrypted data: {decrypted}")
            print(f"As UTF-8 (ignoring errors): {decrypted.decode('utf-8', errors='ignore')}")
            print(f"As hex: {decrypted.hex()}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()