from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img)

    # Apply encryption by adding key and wrapping around 256
    encrypted_arr = (arr + key) % 256
    encrypted_img = Image.fromarray(encrypted_arr.astype(np.uint8))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img)

    # Apply decryption by subtracting key and wrapping around 256
    decrypted_arr = (arr - key) % 256
    decrypted_img = Image.fromarray(decrypted_arr.astype(np.uint8))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    print("Simple Image Encryption Tool")
    choice = input("Choose an option (encrypt/decrypt): ").lower()
    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    key = int(input("Enter encryption key (integer): "))

    if choice == "encrypt":
        encrypt_image(input_path, output_path, key)
    elif choice == "decrypt":
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
