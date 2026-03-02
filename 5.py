def mat_vec_mul(mat, vec, mod):
    n      = len(mat)
    result = [0] * n
    for i in range(n):
        for j in range(n):
            result[i] += mat[i][j] * vec[j]
        result[i] %= mod
    return result

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def matrix_inverse_2x2(mat, mod):
    det     = (mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]) % mod
    det_inv = mod_inverse(det, mod)
    inv = [
        [(mat[1][1]  * det_inv) % mod, ((-mat[0][1]) * det_inv) % mod],
        [((-mat[1][0]) * det_inv) % mod, (mat[0][0]  * det_inv) % mod]
    ]
    for i in range(2):
        for j in range(2):
            inv[i][j] = (inv[i][j] + mod) % mod
    return inv

def hill_encrypt(text, key_matrix):
    text = text.upper()
    while len(text) % 2 != 0:
        text += 'X'
    result = ""
    for i in range(0, len(text), 2):
        vec     = [ord(text[i]) - ord('A'), ord(text[i+1]) - ord('A')]
        enc_vec = mat_vec_mul(key_matrix, vec, 26)
        result += chr(enc_vec[0] + ord('A'))
        result += chr(enc_vec[1] + ord('A'))
    return result

def hill_decrypt(text, key_matrix):
    inv_matrix = matrix_inverse_2x2(key_matrix, 26)
    result = ""
    for i in range(0, len(text), 2):
        vec     = [ord(text[i]) - ord('A'), ord(text[i+1]) - ord('A')]
        dec_vec = mat_vec_mul(inv_matrix, vec, 26)
        result += chr(dec_vec[0] + ord('A'))
        result += chr(dec_vec[1] + ord('A'))
    return result

text = input("Enter the text : ")
print("Enter 2x2 key matrix values:")
a = int(input("Enter a (row1, col1) : "))
b = int(input("Enter b (row1, col2) : "))
c = int(input("Enter c (row2, col1) : "))
d = int(input("Enter d (row2, col2) : "))

key_matrix = [[a, b], [c, d]]

encrypted = hill_encrypt(text, key_matrix)
decrypted = hill_decrypt(encrypted, key_matrix)

print("Original  :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)
