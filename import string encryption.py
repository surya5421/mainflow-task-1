import string

class CustomEncryptor:
    def __init__(self, shift=3):
        self.shift = shift
        self.alphabet = string.ascii_letters + string.digits + string.punctuation + ' '
        self.trans_table = self._generate_cipher()

    def _generate_cipher(self):
        shifted = self.alphabet[self.shift:] + self.alphabet[:self.shift]
        return str.maketrans(self.alphabet, shifted)

    def encrypt(self, text, layers=1):
        for _ in range(layers):
            text = text.translate(self.trans_table)[::-1]
        return text

    def decrypt(self, text, layers=1):
        reverse_table = str.maketrans(
            self.alphabet[self.shift:] + self.alphabet[:self.shift],
            self.alphabet
        )
        for _ in range(layers):
            text = text[::-1].translate(reverse_table)
        return text

encryptor = CustomEncryptor(shift=5)
original_message = "Hello, World! 123"
encrypted = encryptor.encrypt(original_message, layers=2)
decrypted = encryptor.decrypt(encrypted, layers=2)

print("Original:", original_message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
