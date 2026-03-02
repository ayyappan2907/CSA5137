def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char >= 'A' and char <= 'Z':
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char >= 'a' and char <= 'z':
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, 26 - shift)

text  = input("Enter the text  : ")
shift = int(input("Enter the shift : "))

encrypted = caesar_encrypt(text, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Original  :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)
