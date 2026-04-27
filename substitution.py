"""
Substitution Cipher Implementation
- Encrypt and decrypt using substitution cipher with custom mapping
- Frequency analysis to break without knowing the key
"""

def substitution_encrypt(plaintext, mapping):
    """Encrypt text using substitution cipher with given mapping dictionary"""
    plaintext = plaintext.upper()
    result = ""
    
    for char in plaintext:
        if char.isalpha():
            result += mapping.get(char, char)
        else:
            result += char
    
    return result

def substitution_decrypt(ciphertext, mapping):
    """Decrypt text using substitution cipher (reverse the mapping)"""
    # Create reverse mapping
    reverse_mapping = {v: k for k, v in mapping.items()}
    return substitution_encrypt(ciphertext, reverse_mapping)

def get_default_substitution_key():
    """Generate a standard substitution mapping for demo"""
    plaintext_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alphabet   = "QWERTYUIOPASDFGHJKLZXCVBNM"
    
    mapping = {}
    for i, letter in enumerate(plaintext_alphabet):
        mapping[letter] = cipher_alphabet[i]
    
    return mapping

def frequency_analysis(ciphertext):
    """
    Analyze letter frequencies in ciphertext
    Compare to English standard to guess plaintext-to-ciphertext mapping
    """
    print("\n" + "="*60)
    print("FREQUENCY ANALYSIS (Substitution Cipher Breaking)")
    print("="*60)
    
    ciphertext = ciphertext.upper()
    
    # English letter frequencies (in order of commonness)
    english_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    
    # Count frequencies in ciphertext
    freq = {}
    total = 0
    
    for char in ciphertext:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
            total += 1
    
    if total == 0:
        print("No letters found in ciphertext!")
        return {}
    
    # Sort by frequency
    sorted_freq = sorted(freq.items(), key=lambda x: -x[1])
    
    print("\n[Step 1] Ciphertext letter frequencies:")
    print("-"*60)
    for char, count in sorted_freq[:10]:
        percentage = (count / total) * 100
        bar = "█" * int(percentage)
        print(f"{char}: {percentage:5.1f}% {bar}")
    
    # Build mapping based on frequency matching
    print("\n[Step 2] Matching to English frequencies...")
    print("-"*60)
    
    mapping = {}
    ciphertext_order = ''.join([char for char, _ in sorted_freq])
    
    for i, cipher_letter in enumerate(ciphertext_order):
        if i < len(english_order):
            plain_letter = english_order[i]
            mapping[cipher_letter] = plain_letter
            print(f"{cipher_letter} (freq rank {i+1}) → {plain_letter}")
    
    # Decrypt with the guessed mapping
    print("\n[Step 3] Decrypting with guessed mapping...")
    print("-"*60)
    
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted += mapping.get(char, '?')
        else:
            decrypted += char
    
    print(f"Decrypted text (first 100 chars):\n{decrypted[:100]}")
    
    print("\n" + "="*60)
    print("Note: This is an automated guess. Check if it's readable!")
    print("="*60)
    
    return mapping

def substitution_break(ciphertext):
    """
    Break substitution cipher using frequency analysis
    Returns the decrypted text
    """
    mapping = frequency_analysis(ciphertext)
    
    ciphertext = ciphertext.upper()
    decrypted = ""
    
    for char in ciphertext:
        if char.isalpha():
            decrypted += mapping.get(char, '?')
        else:
            decrypted += char
    
    return decrypted

def create_custom_mapping():
    """Allow user to create a custom substitution mapping"""
    print("\nCreating custom substitution mapping...")
    print("Enter 26 letters to replace A-Z (or press Enter for default):")
    
    cipher_alphabet = input("Custom alphabet: ").upper()
    
    if len(cipher_alphabet) != 26 or not cipher_alphabet.isalpha():
        print("Using default mapping: QWERTYUIOPASDFGHJKLZXCVBNM")
        return get_default_substitution_key()
    
    plaintext_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping = {}
    
    for i, letter in enumerate(plaintext_alphabet):
        mapping[letter] = cipher_alphabet[i]
    
    return mapping
