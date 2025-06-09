import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)  # Tạo đối tượng băm BLAKE2b với kích thước 64 byte
    blake2_hash.update(message.encode('utf-8'))  # Chuyển đổi dữ liệu thành bytes và băm
    return blake2_hash.digest()  # Trả về giá trị băm ở dạng bytes

def main():
    text = input("Nhập chuỗi văn bản: ")
    hashed_text = blake2(text)
    print("Chuỗi văn bản đã nhập:", text)
    print("BLAKE2 Hash:", hashed_text.hex())  # Hiển thị băm dưới dạng hex

if __name__ == "__main__":
    main()