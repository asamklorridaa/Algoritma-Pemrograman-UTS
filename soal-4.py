# Materi: Fungsi, parameter, return, multiple return, scope variabel

# Variabel global buat hitung berapa kali analisis_password() dipanggil
counter_analisis_password = 0

# a. validasi_ip(ip) menerima satu string, mengembalikan True jika format IP valid (4 oktet, masing-masing 0 – 255), False jika tidak.
def validasi_ip(ip: str) -> bool:
    bagian  = ip.split(".")
    if len(bagian ) != 4:
        return False

    for b in bagian :
        if not b.isdigit():
            return False
        nilai = int(b)
        if nilai < 0 or nilai > 255:
            return False

    return True


# b. analisis_password(password, username="") menerima password dan username opsional, mengembalikan 3 nilai:
def analisis_password(password: str = "", username: str = ""):
    global counter_analisis_password
    counter_analisis_password += 1 

    # b.1 skor (0–5): minimal 8 karakter, ada huruf besar, ada huruf kecil, ada angka, ada karakter spesial
    skor = 0

    # Minimal 8 karakter
    if len(password) >= 8:
        skor += 1

    # Ada huruf besar
    if any(c.isupper() for c in password):
        skor += 1

    # Ada huruf kecil
    if any(c.islower() for c in password):
        skor += 1

    # Ada angka
    if any(c.isdigit() for c in password):
        skor += 1

    # Ada karakter spesial
    karakter_spesial = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
    if any(c in karakter_spesial for c in password):
        skor += 1

    # b.2 level: SANGAT KUAT (5), KUAT (4), SEDANG (3), LEMAH (1–2), SANGAT LEMAH (0)
    if skor == 5:
        level = "SANGAT KUAT"
    elif skor == 4:
        level = "KUAT"
    elif skor == 3:
        level = "SEDANG"
    elif skor in [1, 2]:
        level = "LEMAH"
    else:
        level = "SANGAT LEMAH"

    # b.3 aman (boolean): True jika skor ≥ 4
    aman = skor >= 4

    return skor, level, aman

# c. laporan_keamanan(ip, password, username) — fungsi uDDtama yang:
def laporan_keamanan(ip: str, password: str, username: str = "") -> str:
    # c.1 Memanggil validasi_ip() dan analisis_password()
    is_ip_valid = validasi_ip(ip)
    skor_pwd, level_pwd, is_pwd_aman = analisis_password(password, username)

    # c.3 Mengembalikan status akhir: "LOGIN DIIZINKAN" jika IP valid dan password aman, atau "LOGIN DITOLAK"
    if is_ip_valid and is_pwd_aman:
        status_akhir = "LOGIN DIIZINKAN"
    else:
        status_akhir = "LOGIN DITOLAK"

    # c.2 Menampilkan laporan lengkap
    print("=" * 50)
    print("HASIL LAPORAN")
    print("=" * 50)
    if username:
        print(f"Username         : {username}")
        print(f"Alamat IP        : {ip} -> Status IP: {'VALID' if is_ip_valid else 'TIDAK VALID'}")
        print(f"Password         : {'*' * len(password)}")
        print(f"Skor Password    : {skor_pwd}/5")
        print(f"Level Password   : {level_pwd}")
        print(f"Keamanan Password: {'AMAN' if is_pwd_aman else 'TIDAK AMAN'}")
        print("-" * 50)
        print(f"STATUS AKHIR     : {status_akhir}")
        print("=" * 50)

    return status_akhir


if __name__ == "__main__":
    # Percobaan
    laporan_keamanan("192.168.1.1", "Admin321!", "fachri")
    laporan_keamanan("256.100.0.1", "12345", "user1")

    # Menampilkan total berapa kali fungsi analisis_password() dipanggil via global variable
    print(
        f"\n[INFO] Fungsi analisis_password() telah dipanggil sebanyak: {counter_analisis_password} kali."
    )