class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails <= 1:
            return plain_text

        rails = ['' for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: down, -1: up

        for char in plain_text:
            rails[rail_index] += char
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return ''.join(rails)

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails <= 1:
            return cipher_text

        # First, determine the pattern of rails
        rail_pattern = []
        rail_index = 0
        direction = 1

        for _ in cipher_text:
            rail_pattern.append(rail_index)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Count how many characters go into each rail
        rail_lengths = [rail_pattern.count(i) for i in range(num_rails)]

        # Fill rails with appropriate characters
        rails = []
        index = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[index:index + length]))
            index += length

        # Reconstruct the plain text
        result = ''
        rail_index = 0
        direction = 1
        for _ in cipher_text:
            result += rails[rail_index].pop(0)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return result
