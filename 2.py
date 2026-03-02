def mono_encrypt(text, key):
    result = ""
    for char in text.upper():
        if char >= 'A' and char <= 'Z':
            index = ord(char) - ord('A')
            result += key[index]
        else:
            result += char
    return result

def mono_decrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in text.upper():
        if char >= 'A' and char <= 'Z':
            index = 0
            for i in range(26):
                if key[i] == char:
                    index = i
                    break
            result += alphabet[index]
        else:
            result += char
    return result

text = input("Enter the text : ")
key  = input("Enter the key (26 unique letters e.g. QWERTYUIOPLKJHGFDSAZXCVBNM) : ")

if len(key) != 26:
    print("Key must be exactly 26 letters!")
else:
    encrypted = mono_encrypt(text, key.upper())
    decrypted = mono_decrypt(encrypted, key.upper())
    print("Original  :", text)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
