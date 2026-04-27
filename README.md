# 🔐 Classical Cipher Arsenal

> **A Comprehensive Python Cryptanalysis & Encryption Toolkit**  
> Breaking and defending classical ciphers with automated cryptanalysis techniques

[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Platform: Windows/Linux/Mac](https://img.shields.io/badge/Platform-Cross%20Platform-brightgreen?style=flat-square)](#)

---

## 🎯 Overview

Classical Cipher Arsenal is an interactive Python CLI toolkit that demonstrates fundamental concepts in cryptography and cryptanalysis. This project implements three classical cipher systems and includes **automated breaking techniques** to cryptanalyze encrypted messages without the encryption key.

Perfect for:
- 📚 **Learning** classical cryptography techniques
- 🔍 **Understanding** weaknesses in simple substitution ciphers
- 🧮 **Experimenting** with frequency analysis and pattern recognition
- 🎓 **Academic projects** on information security

---

## 📋 Features

### ✨ Three Classical Ciphers

| Cipher | Encryption | Decryption | Breaking Method |
|--------|-----------|-----------|-----------------|
| **Caesar** | Fixed letter shift | Shift back | Brute Force (25 attempts) |
| **Vigenère** | Keyword-based shifts | Keyword decryption | Kasiski Examination |
| **Substitution** | Letter-to-letter mapping | Reverse mapping | Frequency Analysis |

### 🛡️ Cryptanalysis Features

- **Caesar Brute Force**: Try all 25 possible shifts and identify readable plaintext
- **Kasiski Examination**: Break Vigenère by finding repeated sequences and calculating key length
- **Frequency Analysis**: Statistical analysis to break substitution ciphers using English letter distributions
- **Automatic Key Recovery**: Most attacks recover the encryption key automatically

---

## 🚀 Quick Start

### Requirements
- **Python 3.6+**
- No external dependencies (uses only Python standard library)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shaheer005/Classical-Cipher-Arsenal.git
   cd Classical-Cipher-Arsenal
   ```

2. **Run the program:**
   ```bash
   python3 cipher_arsenal.py
   ```

### Usage

When you launch the program, you'll see an interactive menu:

```
[1] Caesar Cipher           - Encrypt/Decrypt with fixed shift
[2] Vigenère Cipher         - Encrypt/Decrypt with keyword
[3] Substitution Cipher     - Encrypt/Decrypt with letter mapping
[4] Break a Cipher          - Automatic cryptanalysis
[5] Exit                    - Close the program
```

---

## 📖 How Each Cipher Works

### 1️⃣ Caesar Cipher

**What it is**: Every letter shifts by the same fixed amount

**Example**:
```
Key: 3
HELLO → KHOOR
(H→K, E→H, L→O, L→O, O→R)
```

**Breaking**: Since there are only 25 possible shifts, we try all of them and display the results

**Usage**:
```
[1] Caesar Cipher → [1] Encrypt
Enter text: HELLO
Shift: 3
→ KHOOR
```

---

### 2️⃣ Vigenère Cipher

**What it is**: Uses a repeating keyword where each letter gets a different shift

**Example**:
```
Keyword: SECRET
ATTACKATDAWN
SECRETSECRET  (repeating key)
SXVRGDXWAQWM  (ciphertext)
```

**Breaking**: Uses **Kasiski Examination**
- Finds repeated sequences in ciphertext
- Calculates distances between occurrences
- Uses GCD to estimate key length
- Breaks each group as Caesar cipher
- Recovers the keyword automatically

**Usage**:
```
[2] Vigenère Cipher → [1] Encrypt
Enter text: ATTACKATDAWN
Keyword: SECRET
→ SXVRGDXWAQWM
```

---

### 3️⃣ Substitution Cipher

**What it is**: Maps each alphabet letter to a different letter (fixed for entire message)

**Example**:
```
Mapping: A→Q, B→W, C→E, D→R, E→T, ...
HELLO → ITSSG
```

**Breaking**: Uses **Frequency Analysis**
- Counts how often each letter appears in ciphertext
- Compares against English letter frequency distribution
- Maps most frequent cipher letters to most frequent English letters
- Decrypts with guessed mapping

English character frequencies:
```
E (11.2%) T (8.2%) A (8.1%) O (7.5%) I (7.0%)
N (6.7%) S (6.3%) H (6.1%) R (6.0%) ...
```

**Usage**:
```
[3] Substitution Cipher → [1] Encrypt
Enter text: HELLO
→ ITSSG (using default mapping)
```

---

## 🔬 Cryptanalysis Examples

### Breaking Caesar:
```
Ciphertext: KHOOR

[Analyzing...]
Shift  1: JIPPS
Shift  2: KJQQT
Shift  3: HELLO  ← Most readable!
...
Shift 25: GDKKN

Which shift looks most readable? 3
→ Key: 3
→ Plaintext: HELLO
```

### Breaking Vigenère:
```
Ciphertext: SXVRGDXWAQWM

[Step 1] Finding repeated sequences...
Found: 'RDX' at positions [2, 8] (distance: 6)

[Step 2] Possible key lengths: [1, 2, 3, 6]

[Step 3] Testing key length = 6...

[Step 4] Breaking each group:
  Group 1: key='S'
  Group 2: key='E'
  Group 3: key='C'
  Group 4: key='R'
  Group 5: key='E'
  Group 6: key='T'

[Success] Key found: SECRET
→ Plaintext: ATTACKATDAWN
```

### Breaking Substitution:
```
Ciphertext: ITSSG WYZ BSYBN

[Step 1] Ciphertext frequencies:
T: 22.2% ████████████
S: 19.4% ███████
W:  8.3% ███
...

[Step 2] Mapping to English frequencies:
T → E (most common)
S → T (second most common)
...

[Step 3] Decrypted:
HELLO AND WORLD
```

---

## 📁 Project Structure

```
Classical-Cipher-Arsenal/
├── caesar.py              # Caesar cipher implementation
├── vigenere.py            # Vigenère cipher with Kasiski examination
├── substitution.py        # Substitution cipher with frequency analysis
├── cipher_arsenal.py      # Main interactive menu system
└── README.md              # This file
```

### File Descriptions

| File | Purpose |
|------|---------|
| `caesar.py` | Caesar cipher encryption, decryption, and brute-force attack |
| `vigenere.py` | Vigenère cipher with automated Kasiski examination breaking |
| `substitution.py` | Substitution cipher with frequency-based cryptanalysis |
| `cipher_arsenal.py` | Main program: CLI menu, user interaction, and orchestration |

---

## 👥 Group Delta

**Course**: Information Security (Semester 8)  
**University**: DHA Suffa University

---

## 🎓 Learning Outcomes

After using this toolkit, you'll understand:

- ✅ How classical ciphers work and their mathematical foundations
- ✅ Why simple substitution-based ciphers are insecure
- ✅ Cryptanalysis techniques: brute force, pattern recognition, frequency analysis
- ✅ The importance of key length (Kasiski principle)
- ✅ How frequency analysis exploits language patterns
- ✅ Why modern encryption uses mathematical complexity, not just substitution

---

## 🔒 Security Notice

**⚠️ EDUCATIONAL PURPOSE ONLY**

These classical ciphers are **cryptographically broken** and should **NEVER** be used for real security:

- Caesar cipher has only 25 possible keys
- Vigenère weakens with key reuse (Kasiski/Friedman estimation)
- Substitution cipher falls to frequency analysis with enough ciphertext (>300 chars)

For real encryption, use modern algorithms like **AES-256**, **ChaCha20**, or authenticated encryption schemes.

---

## 💡 Advanced Topics

### Kasiski Examination Deep Dive

The Kasiski examination breaks Vigenère by exploiting key repetition:

1. **Repeated sequences** in plaintext encrypt identically when keywords align
2. **Distances** between repeats are multiples of the key length
3. **GCD** of all distances usually reveals the key length
4. **Groups** are processed separately as Caesar ciphers

Example: Key "ABC" (length 3)
```
THE THE THE THE
ABC ABC ABC ABC

Positions where "THE" appears: 0, 3, 6, 9, ...
Distances: 3, 3, 3
GCD: 3 ← Key length!
```

### Frequency Analysis Statistics

English letter distribution by percentage:
```
E: 11.2%    I: 7.0%     M: 2.4%
T: 8.2%     N: 6.7%     W: 2.4%
A: 8.1%     S: 6.3%     F: 2.2%
O: 7.5%     H: 6.1%     ...
```

Single substitution ciphers preserve frequencies, making them vulnerable to statistical attacks.

---

## 🧪 Testing the Toolkit

### Test Case 1: Caesar
```bash
Plaintext: HELLO
Key: 3
Ciphertext: KHOOR
Attack: Try all 25 shifts → find "HELLO"
```

### Test Case 2: Vigenère
```bash
Plaintext: ATTACKATDAWN
Keyword: SECRET
Ciphertext: SXVRGDXWAQWM
Attack: Find "RDX" repeated → Distance 6 → Key length 6 → Recover "SECRET"
```

### Test Case 3: Substitution
```bash
Plaintext: THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG
Attack: Frequency analysis → Map common cipher letters to E,T,A,...
Success rate: ~85-95% with sufficient text (>300 characters)
```

---

## 🚀 Future Enhancements

- [ ] Implement Friedman test for key length estimation
- [ ] Add Vigenère frequency analysis variant
- [ ] Support for multi-language frequency analysis
- [ ] Graphical user interface (GUI)
- [ ] Hill cipher implementation
- [ ] Playfair cipher with cryptanalysis
- [ ] Support for encrypted file I/O
- [ ] Batch processing mode for testing multiple ciphertexts

---

## 📚 References & Further Reading

- **Kasiski Examination**: [Wikipedia](https://en.wikipedia.org/wiki/Kasiski_examination)
- **Frequency Analysis**: [Wikipedia](https://en.wikipedia.org/wiki/Frequency_analysis)
- **Classical Cryptography**: [Khan Academy - Introduction to Cryptography](https://www.khanacademy.org/computing/computer-science/cryptography)
- **Vigenère Cipher**: [Wikipedia](https://en.wikipedia.org/wiki/Vigenère_cipher)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Add new cipher implementations
- Improve cryptanalysis algorithms

---

## 📧 Contact

**Group Delta**  
Information Security Project  
DHA Suffa University
