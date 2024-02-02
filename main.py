class SimpleRC4:
    def __init__(self, init_key):
        self.key_matrix = self.initialize_key(init_key)
        self.x, self.y = 0, 0

    @staticmethod
    def initialize_key(init_key):
        matrix = list(range(256))
        idx = 0
        key_len = len(init_key)
        for ctr in range(256):
            idx = (idx + matrix[ctr] + init_key[ctr % key_len]) % 256
            matrix[ctr], matrix[idx] = matrix[idx], matrix[ctr]
        return matrix

    def generate_keystream(self, stream_length):
        stream = []
        for _ in range(stream_length):
            self.x = (self.x + 1) % 256
            self.y = (self.y + self.key_matrix[self.x]) % 256
            self.key_matrix[self.x], self.key_matrix[self.y] = self.key_matrix[self.y], self.key_matrix[self.x]
            stream.append(self.key_matrix[(self.key_matrix[self.x] + self.key_matrix[self.y]) % 256])
        return stream

    def cipher(self, text_data):
        self.generate_keystream(1000)
        stream = self.generate_keystream(len(text_data))
        return [byte_data ^ key_byte for byte_data, key_byte in zip(text_data, stream)]


def main_procedure():
    passphrase = [ord(ch) for ch in "exampleKey"]
    message = [ord(ch) for ch in "hetaqrqire"]

    cipher_instance = SimpleRC4(passphrase)
    coded_message = cipher_instance.cipher(message)

    print("Coded Message:", ['{:02x}'.format(item) for item in coded_message])

    decoded_message = SimpleRC4(passphrase).cipher(coded_message)
    print("Decoded Message:", ''.join(chr(item) for item in decoded_message))


if __name__ == "__main__":
    main_procedure()
