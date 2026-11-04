# Materi: Perulangan for, while, break, continue, pass, nested loop

total_log = 0

# 1. Gunakan for dengan range(1, 9) untuk iterasi 8 jam kerja
for jam in range(1, 9):
    # Skip (continue) jam ke-4 (asumsi jam istirahat) dengan menampilkan pesan "[ISTIRAHAT]"
    if jam == 4:
        print(f"Jam ke-{jam}: [ISTIRAHAT]")
        continue

    # Simulasikan jumlah log per jam (jam * 15)
    log_per_jam = jam * 15

    # Berhenti (break) jika total log melebihi 300, tampilkan "Batas kapasitas terlampaui!"
    if total_log + log_per_jam >= 300:
        print("\nBatas kapasitas terlampaui!")
        break

    # Akumulasikan total log menggunakan +=
    total_log += log_per_jam

    # 3. Gunakan pass sebagai placeholder fitur yang belum diimplementasikan
    pass

    print(f"Jam ke-{jam}: Diproses {log_per_jam} log | Total Akumulasi: {total_log} log")

# 4. Tampilkan total log yang berhasil diproses setelah loop selesai
print("=" * 55)
print(f"TOTAL LOG BERHASIL DIPROSES: {total_log} log")
print("=" * 55)