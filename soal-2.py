# Materi: Percabangan if-elif-else, nested if, operator ternary

ip = input("Masukkan alamat IP : ")

# b. Mengklasifikasikan IP
if ip in ["192.168.1.100", "10.0.0.1", "172.16.0.1"]:
    status_ip = "BERBAHAYA"
    rekomendasi = "Blokir IP ini!"
elif ip.startswith(("192.168.", "10.", "172.")):
    status_ip = "IP PRIVAT"
    rekomendasi = "Pantau alamat IP ini"
else:
    status_ip = "IP PUBLIC"
    rekomendasi = "Verifikasi alamat IP ini"

# c. Meminta input password dari pengguna
password = input("Masukkan password anda : ")
panjang_password = len(password)

# d. Menggunakan operator ternary untuk menentukan status:
status_panjang = "PANJANG" if panjang_password >= 8 else "TIDAK PANJANG"
kategori = "AMAN" if panjang_password >= 12 else "SEDANG" if panjang_password >= 8 else "LEMAH"

# e. Menampilkan password dalam bentuk bintang (*)
bintang = "*" * panjang_password

# f. Menggunakan nested if untuk menentukan tingkat risiko:
if status_ip == "BERBAHAYA":
    if kategori == "LEMAH":
        tingkat_resiko = "TINGGI"
    else:
        tingkat_resiko = "SEDANG"
else:
    if kategori == "LEMAH":
        tingkat_resiko = "SEDANG"
    else:
        tingkat_resiko = "RENDAH"

# g. Menampilkan hasil
print("\n" + "=" * 40)
print("HASIL ANALISIS KEAMANAN")
print("=" * 40)
print(f"Alamat IP : {ip}")
print(f"Status IP : {status_ip}")
print(f"Rekomendasi : {rekomendasi}")
print("-" * 40)
print(f"Panjang password : {panjang_password} karakter ({status_panjang})")
print(f"Kategori password : {kategori}")
print("-" * 40)
print(f"Tingkat resiko : {tingkat_resiko}")
