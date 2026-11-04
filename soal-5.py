from functools import reduce

# Data log awal
log_data = [
    {"ip": "192.168.1.100", "skor": 9, "status": "blocked"},
    {"ip": "8.8.8.8", "skor": 2, "status": "allowed"},
    {"ip": "10.0.0.1", "skor": 8, "status": "blocked"},
    {"ip": "1.1.1.1", "skor": 3, "status": "allowed"},
    {"ip": "172.16.0.1", "skor": 7, "status": "blocked"},
    {"ip": "203.0.113.5", "skor": 9, "status": "blocked"}
]

# a. Lambda: Buat klasifikasi = lambda skor: "CRITICAL" if skor >= 8 else "HIGH" if skor >= 6 else "MEDIUM" if skor >= 4 else "LOW"
klasifikasi = lambda skor: "CRITICAL" if skor >= 8 else "HIGH" if skor >= 6 else "MEDIUM" if skor >= 4 else "LOW"

# b. Filter: Gunakan filter() dan lambda untuk menyaring log kritis (skor ≥ 7)
log_kritis = list(filter(lambda x: x["skor"] >= 7, log_data))

# c. Map: Gunakan map() dan lambda untuk membuat label format "[STATUS] IP - Skor X" untuk semua log
label_format = list(map(lambda x: f"[{x['status'].upper()}] {x['ip']} - Skor {x['skor']}", log_data))

# d. Reduce: Gunakan reduce() untuk menghitung total skor semua log dan skor maksimum
total_skor = reduce(lambda acc, x: acc + x["skor"], log_data, 0)
skor_maksimum = reduce(lambda acc, x: acc if acc > x["skor"] else x["skor"], log_data, log_data[0]["skor"])

# e. Rekursi: Buat fungsi rekursif hitung_ancaman(n) yang menghitung deret n + (n-1) + (n-2) + ... + 1. Panggil dengan nilai n = skor maksimum yang didapat dari reduce().
def hitung_ancaman(n):
    if n <= 1:
        return n
    return n + hitung_ancaman(n - 1)

hasil_ancaman = hitung_ancaman(skor_maksimum)

# f. Pipeline: Buat satu pipeline: filter (skor ≥ 7) → map (ambil IP) → reduce (gabungkan IP dengan pemisah ", ")
pipeline_hasil = reduce(
    lambda acc, ip: f"{acc}, {ip}",
    map(lambda x: x["ip"], filter(lambda x: x["skor"] >= 7, log_data))
)

# Nampilkan hasil
print("=== a. Lambda ===")
print(f"Skor 9: {klasifikasi(9)}")
print(f"Skor 7: {klasifikasi(7)}")
print(f"Skor 5: {klasifikasi(5)}")
print(f"Skor 2: {klasifikasi(2)}\n")

print("=== b. Filter ===")
for log in log_kritis:
    print(log)
print()

print("=== c. Map ===")
for label in label_format:
    print(label)
print()

print("=== d. Reduce ===")
print(f"Total Skor    : {total_skor}")
print(f"Skor Maksimum : {skor_maksimum}\n")

print("=== e. Rekursi ===")
print(f"n = {skor_maksimum}")
print(f"Hasil hitung_ancaman({skor_maksimum}) : {hasil_ancaman}\n")

print("=== f. Pipeline ===")
print(f"Hasil Pipeline : {pipeline_hasil}")