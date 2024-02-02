def ksa(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S, n):
    i = 0
    j = 0
    key_stream = []

    while n > 0:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key_stream.append(K)
        n -= 1

    return key_stream

def rc4(key, plaintext):
    S = ksa(key)
    prga(S, 1000)
    key_stream = prga(S, len(plaintext))
    return [plain_byte ^ ks_byte for plain_byte, ks_byte in zip(plaintext, key_stream)]


def main():
    key = [int(hex(ord(char)), 16) for char in "exampleKey"]
    plaintext = [int(hex(ord(char)), 16) for char in "hetaqrqire"]


    encrypted_text = rc4(key, plaintext)
    print("Encrypted:", [hex(val)[2:].zfill(2) for val in encrypted_text])

    decrypted_text = rc4(key, encrypted_text)
    print("Decrypted:", ''.join(chr(val) for val in decrypted_text))



if __name__ == "__main__":
    main()
