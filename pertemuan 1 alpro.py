# (a) Variable
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
jam = ["8:00 - 9:30", "10:00 - 11:30", "13:00 - 14:30", "15:00 - 16:30"]
matkul = {
    "Senin": ["kepemimpinanan ", "sistem data"],
    "Selasa": ["probabilitas ", "bahasa inggris"],
    "Rabu": ["dasar keuangan ", "Statistika"],
    "Kamis": ["algoritman ", "matriks "],
    "Jumat": ["algoritman", "Soft Skills"],
}

# (b) Tipe Data
nama = input("Masukkan nama Anda: ")
nim = input("Masukkan NIM Anda: ")

# (c) Operator
print("-" * 40)
print(f"Jadwal Matakuliah {nama} ({nim})")
print("-" * 40)

# (f) Fungsi
def pilih_hari():
    while True:
        hari_pilih = input("Masukkan hari (Senin-Jumat): ")
        if hari_pilih in hari:
            return hari_pilih
        else:
            print("Hari tidak valid.")

# (d) Percabangan
while True:
    # (e) Perulangan
    hari_pilih = pilih_hari()
    print(f"\nAnda memilih hari {hari_pilih}.")

    # Menampilkan detail matakuliah di hari yang dipilih
    for matkul_hari in matkul[hari_pilih]:
        print(f"{matkul_hari}")

    # Menanyakan apakah ingin melihat jadwal hari lain
    lagi = input("\nApakah ingin melihat jadwal hari lain? (y/n): ").lower()
    if lagi == "n":
        break

print("\nTerima kasih telah menggunakan program ini!")

