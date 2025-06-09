from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()  # Tạo đối tượng băm SHA-3-256
    sha3_hash.update(message.encode('utf-8'))  # Chuyển đổi dữ liệu thành bytes và băm
    return sha3_hash.digest()  # Trả về giá trị băm ở dạng bytes

def main():
    text = input("Nhập chuỗi văn bản: ")
    hashed_text = sha3(text)
    print("Chuỗi văn bản đã nhập:", text)
    print("SHA-3 Hash:", hashed_text.hex())  # Hiển thị băm dưới dạng hex

if __name__ == "__main__":
    main()