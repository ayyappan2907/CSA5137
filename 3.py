def create_matrix(key):
    key = key.upper().replace("J", "I")
    seen = []
    for ch in key:
        if ch >= 'A' and ch <= 'Z' and ch not in seen:
            seen.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seen.append(ch)
    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(seen[i * 5 + j])
        matrix.append(row)
    return matrix

def find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return -1, -1

def prepare_text(text):
    text  = text.upper().replace("J", "I")
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 == len(text):
            b = 'X'
            i += 1
        elif text[i] == text[i + 1]:
            b = 'X'
            i += 1
        else:
            b = text[i + 1]
            i += 2
        pairs.append((a, b))
    return pairs

def playfair_encrypt(text, key):
    matrix = create_matrix(key)
    pairs  = prepare_text(text)
    result = ""
    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result

def playfair_decrypt(text, key):
    matrix = create_matrix(key)
    pairs  = []
    for i in range(0, len(text), 2):
        pairs.append((text[i], text[i + 1]))
    result = ""
    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result

# ✅ FIXED clean function
def clean_decrypted(decrypted, original_length):
    result = ""
    i = 0
    count = 0
    while i < len(decrypted):
        if count < original_length:
            # skip X only if it was inserted as padding between same letters
            if (decrypted[i] == 'X' and
                i > 0 and i < len(decrypted) - 1 and
                decrypted[i - 1] == decrypted[i + 1]):
                i += 1
                continue
            result += decrypted[i]
            count  += 1
        i += 1
    # trim to original length to remove trailing padding
    return result[:original_length]

text = input("Enter the text : ")
key  = input("Enter the key  : ")

original_length = len(text)

encrypted = playfair_encrypt(text, key)
decrypted = playfair_decrypt(encrypted, key)
cleaned   = clean_decrypted(decrypted, original_length)  # ✅ trim to original length

print("Original  :", text.upper())
print("Encrypted :", encrypted)
print("Decrypted :", cleaned)
