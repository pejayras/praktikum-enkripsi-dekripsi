from cryptography.fernet import Fernet


# ==========================================
# MEMBUAT KEY
# ==========================================

key = Fernet.generate_key()
cipher = Fernet(key)

print("=" * 50)
print("PROGRAM PENGUJIAN ENKRIPSI DAN DEKRIPSI")
print("=" * 50)

print("\nKEY:")
print(key.decode())


# ==========================================
# PENGUJIAN 1
# ==========================================

print("\n--- PENGUJIAN 1 ---")

data1 = "Nilai mahasiswa: 90"

print("Data asli      :", data1)

encrypted1 = cipher.encrypt(data1.encode())

print("Hasil enkripsi :", encrypted1.decode())

decrypted1 = cipher.decrypt(encrypted1)

print("Hasil dekripsi :", decrypted1.decode())


# ==========================================
# PENGUJIAN 2
# ==========================================

print("\n--- PENGUJIAN 2 ---")

data2 = """Nama: Budi
NIM: 231001"""

print("Data asli:")
print(data2)

encrypted2 = cipher.encrypt(data2.encode())

print("\nHasil enkripsi:")
print(encrypted2.decode())

decrypted2 = cipher.decrypt(encrypted2)

print("\nHasil dekripsi:")
print(decrypted2.decode())


# ==========================================
# PENGUJIAN 3
# KEY BERBEDA
# ==========================================

print("\n--- PENGUJIAN 3 ---")

key_baru = Fernet.generate_key()
cipher_baru = Fernet(key_baru)

print("Key asli :", key.decode())
print("Key baru :", key_baru.decode())

print("\nMencoba dekripsi menggunakan key berbeda...")

try:
    decrypted_salah = cipher_baru.decrypt(encrypted1)

    print("Hasil dekripsi:", decrypted_salah.decode())

except Exception:
    print("GAGAL DEKRIPSI!")
    print("Key yang digunakan tidak sesuai.")
