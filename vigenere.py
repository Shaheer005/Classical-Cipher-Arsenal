"""
Vigenère Cipher Implementation
- Encrypt and decrypt using Vigenère cipher with keyword
- Kasiski Examination to break without knowing the key
"""

from math import gcd
from functools import reduce

def vigenere_encrypt(plaintext, keyword):
    """Encrypt text using Vigenère cipher with keyword"""
    plaintext = plaintext.upper()
    keyword = keyword.upper()
    result = ""
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - 65
            encrypted = chr((ord(char) - 65 + shift) % 26 + 65)
            result += encrypted
            key_index += 1
        else:
            result += char
    
    return result

def vigenere_decrypt(ciphertext, keyword):
    """Decrypt text using Vigenère cipher with keyword"""
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    result = ""
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - 65
            decrypted = chr((ord(char) - 65 - shift) % 26 + 65)
            result += decrypted
            key_index += 1
        else:
            result += char
    
    return result

def find_repeated_sequences(ciphertext, seq_len=3):
    """Find repeated sequences of given length in ciphertext"""
    ciphertext = ciphertext.upper()
    sequences = {}
    
    for i in range(len(ciphertext) - seq_len + 1):
        seq = ciphertext[i:i+seq_len]
        if seq.isalpha():
            if seq not in sequences:
                sequences[seq] = []
            sequences[seq].append(i)
    
    repeated = {seq: positions for seq, positions in sequences.items() if len(positions) > 1}
    return repeated

def calculate_distances(repeated_sequences):
    """Calculate distances between repeated sequences"""
    distances = []
    
    for seq, positions in repeated_sequences.items():
        for i in range(len(positions) - 1):
            distance = positions[i+1] - positions[i]
            distances.append(distance)
    
    return distances

def find_gcd_of_distances(distances):
    """Find GCD of all distances (likely key length factors)"""
    if not distances:
        return None
    
    return reduce(gcd, distances)

def get_factors(n):
    """Get all factors of a number"""
    factors = []
    for i in range(1, min(n + 1, 26)):  # Key length unlikely to be > 25
        if n % i == 0:
            factors.append(i)
    return factors

def frequency_score(text):
    """Score text based on how close letter frequencies are to English"""
    english_freq = {
        'E': 11.2, 'T': 8.2, 'A': 8.1, 'O': 7.5, 'I': 7.0,
        'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3,
        'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4,
        'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5
    }
    
    text = text.upper()
    letter_count = sum(1 for c in text if c.isalpha())
    
    if letter_count == 0:
        return 0
    
    score = 0
    for letter, expected_freq in english_freq.items():
        actual_count = sum(1 for c in text if c == letter)
        actual_freq = (actual_count / letter_count) * 100
        score += abs(actual_freq - expected_freq)
    
    return -score  # Negative so higher is better

def break_caesar_group(ciphertext):
    """Break a single Caesar cipher (used for breaking Vigenère by groups)"""
    best_score = float('-inf')
    best_shift = 0
    
    for shift in range(26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted += char
        
        score = frequency_score(decrypted)
        if score > best_score:
            best_score = score
            best_shift = shift
            best_decrypted = decrypted
    
    return best_shift, best_decrypted

def kasiski_examination(ciphertext):
    """
    Break Vigenère cipher using Kasiski Examination
    Returns the most likely key
    """
    print("\n" + "="*60)
    print("KASISKI EXAMINATION (Vigenère Breaking)")
    print("="*60)
    
    # Step 1: Find repeated sequences
    print("\n[Step 1] Finding repeated 3-letter sequences...")
    repeated = find_repeated_sequences(ciphertext, 3)
    
    if not repeated:
        print("No repeated sequences found. Trying 4-letter sequences...")
        repeated = find_repeated_sequences(ciphertext, 4)
    
    if not repeated:
        print("Cannot find repeated sequences. Using default key length = 3")
        likely_key_length = 3
    else:
        print(f"Found {len(repeated)} repeated sequence(s):")
        for seq, positions in list(repeated.items())[:5]:
            distances = [positions[i+1] - positions[i] for i in range(len(positions)-1)]
            print(f"  '{seq}' at positions {positions} (distances: {distances})")
        
        # Step 2: Calculate distances
        print("\n[Step 2] Calculating distances between sequences...")
        distances = calculate_distances(repeated)
        print(f"Distances: {sorted(set(distances))}")
        
        # Step 3: Find GCD
        print("\n[Step 3] Finding common factors of distances...")
        gcd_val = find_gcd_of_distances(distances)
        factors = get_factors(gcd_val) if gcd_val else [2, 3, 4, 5]
        print(f"GCD of distances: {gcd_val}")
        print(f"Possible key lengths: {factors}")
        
        likely_key_length = factors[0] if factors else 3
    
    # Step 4: Try each likely key length
    print(f"\n[Step 4] Testing key length = {likely_key_length}...")
    
    ciphertext_upper = ciphertext.upper()
    groups = [[] for _ in range(likely_key_length)]
    
    key_index = 0
    for char in ciphertext_upper:
        if char.isalpha():
            groups[key_index % likely_key_length].append(char)
            key_index += 1
    
    # Step 5: Break each group as Caesar
    print("[Step 5] Breaking each group as Caesar cipher...")
    key_letters = []
    
    for i, group in enumerate(groups):
        group_text = ''.join(group)
        shift, decrypted = break_caesar_group(group_text)
        key_letter = chr((shift) % 26 + 65)
        key_letters.append(key_letter)
        print(f"  Group {i+1}: shift={shift} → key letter '{key_letter}'")
    
    key = ''.join(key_letters)
    print(f"\n[Success] Key found: {key}")
    print("="*60)
    
    return key
