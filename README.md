# Secure-file-encryption-tool
A Python-based file encryption and decryption tool using AES encryption (Fernet).

# Secure File Encryption Tool

This Python tool allows users to encrypt and decrypt files securely using AES encryption (via the Fernet module from the `cryptography` library).

## Features:
- **Encryption**: Converts a file into an unreadable format using AES encryption.
- **Decryption**: Restores the original file from the encrypted version.
- **Key Management**: Generates and stores a secret key for encryption/decryption.

## How to Use:
1. Run the script.
2. Select:
   - `1` to generate a secret key.
   - `2` to encrypt a file.
   - `3` to decrypt a file.
3. The decrypted file will overwrite the original, or you can modify the code to save it as a new file.

## Dependencies:
- `cryptography`
  ```bash
  pip install cryptography

