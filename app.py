from flask import Flask

# Inisialisasi aplikasi Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # Buat variabel untuk menampung pesan dalam format HTML
    message = f"<h1>Halo Dunia!</h1>"
    message += f"<p>Ini adalah versi aplikasi yang sudah diperbarui.</p>"
    message += f"<p>Pipeline CI/CD saya berhasil! ✅</p>"
    
    # Kembalikan isi variabel message
    return message

if __name__ == "__main__":
    # Jalankan aplikasi di port 8080
    app.run(host='0.0.0.0', port=8080)