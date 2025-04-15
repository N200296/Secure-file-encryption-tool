from cryptography.fernet import Fernet

# Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption Key Generated and Saved as 'secret.key'.")

# Load the key from file
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a file
def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"File '{filename}' encrypted successfully!")

# Decrypt a file
def decrypt_file(encrypted_filename, key):
    fernet = Fernet(key)
    with open(encrypted_filename, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    original_filename = encrypted_filename.replace(".enc", "")
    with open(original_filename, "wb") as dec_file:
        dec_file.write(decrypted)

    print(f"File '{encrypted_filename}' decrypted successfully!")

# Main menu
if __name__ == "__main__":
    print("=== Secure File Encryption Tool ===")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        generate_key()
    else:
        key = load_key()
        if choice == "2":
            filename = input("Enter the filename to encrypt: ")
            encrypt_file(filename, key)
        elif choice == "3":
            encrypted_filename = input("Enter the encrypted filename to decrypt: ")
            decrypt_file(encrypted_filename, key)
        else:
            print("Invalid choice.")
