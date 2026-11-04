# Materi: List, tuple, method list, slicing, list comprehension

# a. Membuat tuple PROTOKOL_AMAN = ("HTTPS", "SSH", "SFTP", "TLS") (data konstan)
PROTOKOL_AMAN = ("HTTPS", "SSH", "SFTP", "TLS")

# b. Membuat list log_aktivitas berisi minimal 8 dictionary dengan field: ip, protokol, port
log_aktivitas = [
    {"ip": "192.168.1.10", "protokol": "HTTPS", "port": 443},
    {"ip": "10.0.0.5", "protokol": "HTTP", "port": 80},
    {"ip": "172.16.0.2", "protokol": "SSH", "port": 22},
    {"ip": "192.168.1.50", "protokol": "TELNET", "port": 23},
    {"ip": "10.0.0.12", "protokol": "SFTP", "port": 22},
    {"ip": "192.168.1.100", "protokol": "SMB", "port": 445},
    {"ip": "172.16.0.15", "protokol": "TLS", "port": 8443},
    {"ip": "10.0.0.20", "protokol": "RDP", "port": 3389}
]

# c. Menggunakan method list:
# c.1 append() untuk menambah 1 log baru
log_baru = {"ip": "192.168.1.200", "protokol": "HTTPS", "port": 443}
log_aktivitas.append(log_baru)

# c.2 remove() untuk menghapus 1 log tertentu
log_dihapus = {"ip" : "192.168.1.10", "protokol" : "HTTPS", "port": 443}
log_aktivitas.remove(log_dihapus)

# c.3 sort() untuk mengurutkan log berdasarkan port
log_aktivitas.sort(key=lambda x: x["port"])

# d. Menggunakan slicing untuk:
# d.1 Menampilkan 3 log pertama
tiga_pertama = log_aktivitas[:3]

# d.2 Menampilkan 3 log terakhir
tiga_terakhir = log_aktivitas[-3:]

# d.3 Membalik urutan seluruh log
log_terbalik = log_aktivitas[::-1]

# e. Menggunakan list comprehension untuk:
# e.1 Menyaring log dengan protokol AMAN
log_aman = [log for log in log_aktivitas if log["protokol"] in PROTOKOL_AMAN]

# e.2 Menyaring log dengan port berbahaya ([21, 23, 25, 135, 445, 3389])
port_berbahaya = [21, 23, 25, 135, 445, 3389]
log_berbahaya = [log for log in log_aktivitas if log["port"] in port_berbahaya]

# e.3 Membuat list IP dengan prefix "IP-"
ip_prefix = [f"IP-{log['ip']}" for log in log_aktivitas]

# f. Menampilkan semua hasil dalam format yang rapi
print("=" * 50)
print("Hasil dalam format tabel:")
print(f"{'IP Address' :<20} | {'Protokol' :<10} | {'Port' :<6}")
print("-" * 50)
for log in log_aktivitas:
    print(f"{log['ip']:<20} | {log['protokol']:<10} | {log['port']:<6}")
print("=" * 50)