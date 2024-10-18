# Function to encrypt the text using Caesar cipher
def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Encrypt only alphabetic characters
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Keep spaces and other non-letter characters
    return encrypted_text

# Function to decrypt the text using Caesar cipher
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Decrypt only alphabetic characters
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Keep spaces and other non-letter characters
    return decrypted_text

# Main program
if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt, or 'decrypt' to decrypt: ").lower()
    text = input("Enter your text: ")
    shift = int(input("Enter the shift (key): "))

    if choice == 'encrypt':
        result = caesar_encrypt(text, shift)
        print("Encrypted text:", result)
    elif choice == 'decrypt':
        result = caesar_decrypt(text, shift)
        print("Decrypted text:", result)
    else:
        print("Invalid choice!")
