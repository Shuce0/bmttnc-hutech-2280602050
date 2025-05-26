from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher

app = Flask(__name__)

# Trang chủ
@app.route("/")
def home():
    return render_template("index.html")

# ===== CAESAR =====
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return render_template('caesar.html', result=f'Encrypted Text: {encrypted_text}')

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return render_template('caesar.html', result=f'Decrypted Text: {decrypted_text}')

# ===== VIGENERE =====
@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        action = request.form["action"]
        vigenere = VigenereCipher()
        if action == "encrypt":
            result = vigenere.encrypt(text, key)
        elif action == "decrypt":
            result = vigenere.decrypt(text, key)
    return render_template("vigenere.html", result=result)

# ===== RAIL FENCE =====
@app.route("/railfence", methods=["GET", "POST"])
def railfence():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        key = int(request.form["key"])
        action = request.form["action"]
        rail = RailFenceCipher()
        if action == "encrypt":
            result = rail.encrypt(text, key)
        elif action == "decrypt":
            result = rail.decrypt(text, key)
    return render_template("railfence.html", result=result)

# ===== PLAYFAIR =====
@app.route("/playfair", methods=["GET", "POST"])
def playfair():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        action = request.form["action"]
        pf = PlayfairCipher()
        if action == "encrypt":
            result = pf.encrypt(text, key)
        elif action == "decrypt":
            result = pf.decrypt(text, key)
    return render_template("playfair.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
