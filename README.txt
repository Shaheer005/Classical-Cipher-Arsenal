# Classical Cipher Arsenal
## Multi-Cipher Security Arsenal & Cryptanalysis Suite

**Group Delta**
- Shaheer Ahmed (CS221107)
- Sumeet Jani (CS221109)
- Ahmed Mubarak (CS221116)
- Taha Ahmed (CS221029)

**Course:** Information Security - Semester 8  
**University:** DHA Suffa University

---

## What This Project Does

This is a Python CLI toolkit that:
1. **Encrypts and decrypts** messages using 3 classical ciphers
2. **Automatically breaks** those ciphers without knowing the key

---

## The 3 Ciphers

### 1. Caesar Cipher
Every letter shifts by a fixed number.
```
Key = 3
HELLO → KHOOR
```
**Breaking method:** Brute force (try all 25 shifts)

### 2. Vigenère Cipher
Uses a keyword. Each letter gets a different shift.
```
Keyword: SECRET
ATTACK → SXVRGD
```
**Breaking method:** Kasiski Examination (finds key length via repeated sequences)

### 3. Substitution Cipher
Maps each letter to a fixed different letter.
```
A→Q, B→W, C→E, ...
HELLO → ITSSG
```
**Breaking method:** Frequency Analysis (E appears 12.7% in English)

---

## How to Run

### Requirements
- Python 3.6+
- No external libraries needed (uses only built-in Python)

### Installation
1. Download all 4 files:
   - `caesar.py`
   - `vigenere.py`
   - `substitution.py`
   - `cipher_arsenal.py`

2. Place them in the same folder

### Run the Program
```bash
python3 cipher_arsenal.py
```

---

## Using the Program

### Main Menu
```
[1] Caesar Cipher
[2] Vigenère Cipher
[3] Substitution Cipher
[4] View Cipher Descriptions
[5] Exit
```

### Caesar Cipher
- **Encrypt:** Enter plaintext and shift (0-25)
- **Decrypt:** Enter ciphertext and shift
- **Break:** Enter ciphertext → program tries all 25 shifts → you pick the readable one

### Vigenère Cipher
- **Encrypt:** Enter plaintext and keyword
- **Decrypt:** Enter ciphertext and keyword
- **Break:** Enter ciphertext → Kasiski finds key automatically → message decrypted

### Substitution Cipher
- **Create mapping:** Use default or custom
- **Encrypt:** Enter plaintext with chosen mapping
- **Decrypt:** Enter ciphertext with same mapping
- **Break:** Enter ciphertext → Frequency Analysis finds mapping → message decrypted

---

## Examples to Try

### Caesar
```
Encrypt: HELLO (shift 3)
Result:  KHOOR

Break: KHOOR
Will show all 25 shifts and you pick shift 3
```

### Vigenère
```
Encrypt: ATTACK AT DAWN (keyword: SECRET)
Result:  SXVRGD SX FRAG

Break: SXVRGD SX FRAG
Program finds key = SECRET automatically
```

### Substitution
```
Encrypt: HELLO (default mapping)
Result:  ITSSG

Break: ITSSG
Program guesses mapping using frequency analysis
```

---

## File Structure

```
classical-cipher-arsenal/
├── cipher_arsenal.py      # Main menu program
├── caesar.py              # Caesar cipher module
├── vigenere.py            # Vigenère cipher module
├── substitution.py        # Substitution cipher module
└── README.txt             # This file
```

---

## Technical Details

### Caesar Module (`caesar.py`)
- `caesar_encrypt(text, shift)` - Encrypt with shift
- `caesar_decrypt(text, shift)` - Decrypt with shift
- `caesar_break(ciphertext)` - Try all 25 shifts

### Vigenère Module (`vigenere.py`)
- `vigenere_encrypt(plaintext, keyword)` - Encrypt with keyword
- `vigenere_decrypt(ciphertext, keyword)` - Decrypt with keyword
- `kasiski_examination(ciphertext)` - Find key using Kasiski method

### Substitution Module (`substitution.py`)
- `substitution_encrypt(plaintext, mapping)` - Encrypt with mapping
- `substitution_decrypt(ciphertext, mapping)` - Decrypt with mapping
- `substitution_break(ciphertext)` - Break using frequency analysis
- `frequency_analysis(ciphertext)` - Analyze letter frequencies

---

## How Breaking Works

### Caesar Breaking (Brute Force)
1. Try all 25 possible shifts
2. Print all results
3. User identifies which one is readable English

### Vigenère Breaking (Kasiski Examination)
1. Find repeated 3-letter sequences in ciphertext
2. Calculate distances between repetitions
3. Key length is a factor of those distances
4. Split ciphertext into groups by key length
5. Each group becomes a Caesar cipher
6. Apply frequency analysis to each group
7. Recover the full key

### Substitution Breaking (Frequency Analysis)
1. Count letter frequencies in ciphertext
2. Compare to English standard (E=12.7%, T=9.1%, A=8.2%, etc.)
3. Match most frequent ciphertext letter to E
4. Continue mapping through all letters
5. Decrypt with guessed mapping

---

## Key Learning Outcomes

After using this toolkit you understand:
- How classical encryption algorithms work mathematically
- Why these ciphers are weak and can be broken
- The foundations of modern cryptography (Caesar → DES → AES)
- The importance of key length and randomization
- How frequency analysis reveals information

---

## Notes

- All text is converted to uppercase for consistency
- Spaces, punctuation, and numbers are preserved
- The program is fully CLI-based (no GUI)
- All algorithms are implemented from scratch
- Code is heavily commented and readable

---

## Testing

The program has been tested with:
- ✅ Caesar cipher encryption/decryption
- ✅ Caesar brute force breaking
- ✅ Vigenère encryption/decryption
- ✅ Vigenère Kasiski breaking
- ✅ Substitution encryption/decryption
- ✅ Substitution frequency analysis breaking

All tests pass successfully.

---

## Support

For any issues or questions about the project:
- Shaheer Ahmed: shaheer05ahmed@gmail.com
- GitHub: github.com/Shaheer005

---

**Built with ❤️ by Group Delta**  
Information Security - DHA Suffa University
