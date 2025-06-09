def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    # Khởi tạo các hằng số MD5
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    # Xử lý dữ liệu đầu vào
    original_length = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += (original_length * 8).to_bytes(8, 'little')

    # Chia dữ liệu thành các khối 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        a, b, c, d = a0, b0, c0, d0

        # Vòng lặp chính của thuật toán MD5
        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * j) % 16

            temp = d
            d = c
            c = b
            b = (b + left_rotate(a + f + 0x5A827999 + words[g], 3)) & 0xFFFFFFFF
            a = temp

        # Cộng giá trị vào ban đầu
        a0 = (a0 + a) & 0xFFFFFFFF
        b0 = (b0 + b) & 0xFFFFFFFF
        c0 = (c0 + c) & 0xFFFFFFFF
        d0 = (d0 + d) & 0xFFFFFFFF

    # Xuất kết quả dạng hex
    return '{:08X}{:08X}{:08X}{:08X}'.format(a0, b0, c0, d0)

if __name__ == "__main__":
    input_string = input("Nhập chuỗi cần băm: ")
    md5_hash = md5(input_string.encode('utf-8'))
    print("Mã băm MD5 của chuỗi '{}': {}".format(input_string, md5_hash))