from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
app = Flask (__name__)
@app.route("/")
def home():
    return render_template('index.html')
#router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key=int(request.form['inputKeyPlain'])
    Caesar=CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key= int(request.form['inputKeyCipher'])
    Caesar=CaesarCipher()
    decrypted_text=Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
@app.route("/vegenere")
def vegenere():
    return render_template('vegenere.html')

@app.route("/encrypt_vegenere", methods=['POST'])
def vegenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)   # gọi đúng method
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt_vegenere", methods=['POST'])
def vegenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)   # gọi đúng method
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence_encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])  # số nguyên key (số lượng rail)
    RailFence = RailFenceCipher()
    encrypted_text = RailFence.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# Thêm route decrypt railfence
@app.route("/railfence_decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    RailFence = RailFenceCipher()
    decrypted_text = RailFence.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')
@app.route("/creatematrix", methods=['POST'])
def create_matrix():
    key = request.form['inputKey']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    # Chuyển matrix thành chuỗi dễ đọc để trả về
    matrix_str = "<br>".join([" ".join(row) for row in matrix])
    return f"<b>Matrix for key '{key}':</b><br>{matrix_str}"

# Route mã hóa Playfair
@app.route("/encrypt_playfair", methods=['POST'])
def encrypt_playfair():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

# Route giải mã Playfair
@app.route("/decrypt_playfair", methods=['POST'])
def decrypt_playfair():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"
#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)