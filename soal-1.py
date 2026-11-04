# Materi: Variabel, tipe data, operator, input/output, f-string

# a. Meminta input dari pengguna: nama analis (string), NIM (string), jumlah log yang dianalisis (integer), dan tingkat kewaspadaan (integer 1–10)
nama = input("Masukkan nama Anda : ")
nim = input("Masukkan NIM Anda : ")
jumlah_log = int(input("Masukkan jumlah log : "))
tingkat_kewaspadaan = int(input("Tingkat kewaspadaan : "))

# b. Menghitung rata-rata log per jam (asumsi 1 shift = 8 jam)
log_per_jam = jumlah_log / 8

# c. Menghitung estimasi waktu analisis dalam menit (asumsi 1 log = 30 detik)
estimasi = jumlah_log * 30 / 60

# d. Menghitung 2 pangkat tingkat kewaspadaan
pangkat_kewaspadaan = 2 ** tingkat_kewaspadaan

# e. Menampilkan seluruh hasil dengan f-string dalam format yang rapi
print("\nHasil Analisis Log")
print("=" * 40)
print(f"Nama Analis : {nama}")
print(f"NIM : {nim}")
print(f"Jumlah Log : {jumlah_log}")
print("-" * 40)
print(f"Rata-rata Log per Jam : {log_per_jam:.2f}")
print(f"Estimasi Waktu Analisis : {estimasi:.2f} menit")
print(f"2 pangkat Tingkat Kewaspadaan : {pangkat_kewaspadaan}")
print("=" * 40)