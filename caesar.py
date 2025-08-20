def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    return caesar_encrypt(encrypted_message, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    encrypted_message = caesar_encrypt(message, shift)
    print(f"Encrypted Message: {encrypted_message}")
    decrypted_message = caesar_decrypt(encrypted_message, shift)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
