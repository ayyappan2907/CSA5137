def vigenere_encrypt(text, key):
    result  = ""
    key     = key.upper()
    k_len   = len(key)
    k_index = 0
    for char in text.upper():
        if char >= 'A' and char <= 'Z':
            shift   = ord(key[k_index % k_len]) - ord('A')
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            k_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result  = ""
    key     = key.upper()
    k_len   = len(key)
    k_index = 0
    for char in text.upper():
        if char >= 'A' and char <= 'Z':
            shift   = ord(key[k_index % k_len]) - ord('A')
            result += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            k_index += 1
        else:
            result += char
    return result

text = input("Enter the text : ")
key  = input("Enter the key  : ")

encrypted = vigenere_encrypt(text, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Original  :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)
