def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Tool ===")
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value: "))
            encrypted = encrypt(message, shift)
            print("Encrypted message:", encrypted)

        elif choice == '2':
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value: "))
            decrypted = decrypt(message, shift)
            print("Decrypted message:", decrypted)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
