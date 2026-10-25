# 🛡️ Password Strength Analyzer and Breaker Simulator 

![Python](https://img.shields.io/badge/Language-Python%203.x-blue?style=for-the-badge&logo=python&logoColor=white) <br>
![Security](https://img.shields.io/badge/Cryptography-SHA--256-green?style=for-the-badge) <br>
![Paradigm](https://img.shields.io/badge/Paradigm-OOP-orange?style=for-the-badge) <br>
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge) <br>

>A cybersecurity took designed to evaluate password complexity and simulate dictionary attacks against cryptographic SHA-256 hashes with and without salt.

---

## **Technical Specification:**
● **Language:** Python (version 3.8 or higher) <br>
● **Standard Libraries:** `hashlib` (built-in, zero external dependencies) <br>
● **Hashing Algorithm:** SHA-256 (Secure Hash Algorithm 256-bit) <br>
● **Architecture Paradigm:** Object-Oriented Programming (OOP) & Procedural Simulation <br>

---

## 📌 Project Overview

The first part of this project focused on analyzing password complexity. I created an application that tested passwords according to multiple complexity thresholds 
(character casing, special symbols, password length and numeral inclusion)

Next, to demonstrate why complexity heuristics alone are insufficient, I created 'breaker.py' to demonstrate the mechanics of **Dictionary Attacks** against unsalted cryptographic hashes, 
and to show why **Cryptographic Salting** is mandatory in modern database security.

## The system includes
* **Password Scoring:** scoring out of 100 assessing character classes, length distribution, and symbol presence.
* **Breach & Blacklist Detection:** set-based lookup(O(1) operation) that cross-references inputs against common breached passwords, automatically overriding scores to 0 if compromised.
* **Dictionary Attack (`breaker.py`):** An attack simulator that computes SHA-256 hashes across candidate wordlists to crack target digests.
* **Cryptographic Salt Defense (`breaker_salt.py`):** An applied demonstration showing how appending randomized salts neutralizes the threat.

---

## 📂 Files
Below is an explanation of the files included in this repository:

1.1) **analyzer.py** <br>
Contains the `PasswordAnalyzer` class. Prompts user input, executes length, digit, casing, and symbol checks, cross-references `common_password.txt`, and calculates a final qualitative and quantitative score.

1.2) **breaker.py** <br>
Simulates an offline dictionary attack. Reads words line-by-line from the dictionary, encodes them to bytes, computes SHA-256 digests, and compares them against an unsalted target hash until the plaintext password is recovered.

1.3) **breaker_salt.py** <br>
A companion script demonstrating cryptographic resilience. Targets a hash generated with a salt appended to the password, showing that standard wordlist candidates cannot crack the digest.

1.4) **common_password.txt** <br>
The dictionary file containing common, weak, and compromised passwords used for both the analyzer blacklist and the breaker simulation.

