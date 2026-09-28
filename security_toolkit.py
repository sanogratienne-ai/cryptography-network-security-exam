#!/usr/bin/env python3
"""
ULK Polytechnic Institute - Security Toolkit
Module: ETTCS801 Cryptography and Network Security
Handles AES-128/256-CBC Fernet Encryption, Decryption, and SHA-256 File Integrity.
"""

import os
import sys
import hashlib
from cryptography.fernet import Fernet, InvalidToken

KEY_ENV_VAR = "APP_ENCRYPTION_KEY"

def load_or_get_key() -> bytes:
    """Loads encryption key from environment variable or generates one in session."""
    key = os.environ.get(KEY_ENV_VAR)
    if not key:
        print(f"[*] Environment variable '{KEY_ENV_VAR}' not found. Generating temporary session key...")
        key = Fernet.generate_key().decode()
        os.environ[KEY_ENV_VAR] = key
    return key.encode()

def calculate_sha256(file_path: str) -> str:
    """Calculates SHA-256 hash of a file with error handling."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"[!] Error: File '{file_path}' not found for hash calculation.")
        return ""
    except Exception as e:
        print(f"[!] File reading error: {e}")
        return ""

def encrypt_file(input_file: str, output_file: str, key: bytes):
    """Encrypts input_file and saves output to output_file."""
    try:
        f = Fernet(key)
        with open(input_file, "rb") as file_in:
            data = file_in.read()
        encrypted_data = f.encrypt(data)
        with open(output_file, "wb") as file_out:
            file_out.write(encrypted_data)
        print(f"[+] File successfully encrypted: '{output_file}'")
    except FileNotFoundError:
        print(f"[!] Encryption Error: Source file '{input_file}' does not exist.")
    except Exception as e:
        print(f"[!] Encryption failed: {e}")

def decrypt_file(input_file: str, output_file: str, key: bytes):
    """Decrypts input_file and saves output to output_file."""
    try:
        f = Fernet(key)
        with open(input_file, "rb") as file_in:
            encrypted_data = file_in.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(output_file, "wb") as file_out:
            file_out.write(decrypted_data)
        print(f"[+] File successfully decrypted: '{output_file}'")
    except FileNotFoundError:
        print(f"[!] Decryption Error: Encrypted file '{input_file}' not found.")
    except InvalidToken:
        print("[!] Decryption failed: Invalid encryption key or corrupted ciphertext.")
    except Exception as e:
        print(f"[!] Decryption failed: {e}")

def verify_integrity(original_file: str, decrypted_file: str):
    """Compares SHA-256 hashes of original and decrypted files."""
    hash_orig = calculate_sha256(original_file)
    hash_dec = calculate_sha256(decrypted_file)
    
    print(f"Original File SHA-256  : {hash_orig}")
    print(f"Decrypted File SHA-256 : {hash_dec}")
    
    if hash_orig and hash_dec and hash_orig == hash_dec:
        print("[SUCCESS] Integrity Match: The file has not been altered.")
    else:
        print("[ALERT] Integrity Mismatch: File has been modified or corrupted!")

if __name__ == "__main__":
    key = load_or_get_key()
    
    orig = "sample_students.csv"
    enc = "sample_students.csv.enc"
    dec = "sample_students_decrypted.csv"
    
    # Create sample file if it doesn't exist
    if not os.path.exists(orig):
        with open(orig, "w") as f:
            f.write("ID,Name,Department,GPA\n202401,Alice Miller,Computer Science,3.8\n202402,Bob Davis,Networking,3.5\n")
        print(f"[+] Created sample input file: '{orig}'")
        
    print("\n--- Step 1: Encrypting File ---")
    encrypt_file(orig, enc, key)
    
    print("\n--- Step 2: Decrypting File ---")
    decrypt_file(enc, dec, key)
    
    print("\n--- Step 3: Verifying File Integrity ---")
    verify_integrity(orig, dec)
    
    print("\n--- Step 4: Robustness & Error Testing ---")
    decrypt_file("non_existent_file.enc", "out.csv", key)
