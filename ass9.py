
def encrypt(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def decrypt(cipher_text, key):
    decrypted = ""
    for char in cipher_text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted


choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").strip().lower()
text = input("Enter your message: ")
key = int(input("Enter the key (number): "))

if choice == 'e':
    result = encrypt(text, key)
    print("Encrypted message:", result)
elif choice == 'd':
    result = decrypt(text, key)
    print("Decrypted message:", result)
else:
    print("Invalid choice!")

