from flask import Flask

# Inisialisasi aplikasi Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # Pesan yang akan kita ubah nanti untuk melihat efek CI/CD
    return "Halo Dunia! Ini adalah versi pertama dari aplikasi DevOps saya di AWS."

if __name__ == "__main__":
    # Jalankan aplikasi di port 8080
    app.run(host='0.0.0.0', port=8080)