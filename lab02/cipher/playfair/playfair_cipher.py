class PlayfairCipher:
    def __init__(self):
        pass

    def encrypt(self, plain_text, key):
        matrix = self.create_playfair_matrix(key)
        return self.playfair_encrypt(plain_text, matrix)

    def decrypt(self, cipher_text, key):
        matrix = self.create_playfair_matrix(key)
        return self.playfair_decrypt(cipher_text, matrix)

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key) + remaining_letters
        matrix = matrix[:25]  # đảm bảo đúng kích thước 5x5
        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        encrypted_text = ""

        # Chia thành cặp
        i = 0
        while i < len(plain_text):
            a = plain_text[i]
            b = plain_text[i + 1] if i + 1 < len(plain_text) else "X"
            if a == b:
                b = "X"
                i += 1
            else:
                i += 2

            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            a = cipher_text[i]
            b = cipher_text[i + 1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        return decrypted_text
