"""
Caesar Cipher Implementation
- Encrypt and decrypt using Caesar cipher
- Brute force attack to break without knowing the key
"""

def caesar_encrypt(text, shift):
    """Encrypt text using Caesar cipher with given shift"""
    result = ""
    shift = shift % 26
    
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    
    return result

def caesar_decrypt(text, shift):
    """Decrypt text using Caesar cipher with given shift"""
    return caesar_encrypt(text, -shift)

def caesar_break(ciphertext):
    """
    Break Caesar cipher by trying all 25 possible shifts
    Returns the most likely plaintext (readable English)
    """
    print("\n" + "="*60)
    print("ATTEMPTING BRUTE FORCE ATTACK (Caesar)")
    print("="*60)
    
    results = []
    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        results.append((shift, decrypted))
        print(f"Shift {shift:2d}: {decrypted[:80]}")
    
    print("\n" + "-"*60)
    print("Which shift looks most readable? (Enter 1-25)")
    print("-"*60)
    
    return results
