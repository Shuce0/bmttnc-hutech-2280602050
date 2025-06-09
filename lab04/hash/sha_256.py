import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()  # Tạo đối tượng băm SHA-256
    sha256_hash.update(data.encode('utf-8'))  # Chuyển đổi dữ liệu thành bytes và băm
    return sha256_hash.hexdigest()  # Trả về biểu diễn hex của chuỗi hash

if __name__ == "__main__":
    data_to_hash = input("Nhập dữ liệu cần băm SHA-256: ")
    hash_value = calculate_sha256_hash(data_to_hash)
    print("Giá trị băm SHA-256:", hash_value)