# Gunakan base image Python resmi
FROM python:3.9-slim

# Set direktori kerja di dalam kontainer
WORKDIR /app

# Salin file requirements dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin sisa kode aplikasi ke dalam kontainer
COPY . .

# Expose port yang digunakan oleh aplikasi
EXPOSE 8080

# Perintah untuk menjalankan aplikasi saat kontainer dimulai
CMD ["python", "app.py"]