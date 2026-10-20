
# Tugas 4: Normalisasi Data Mahasiswa
# Input: Nama lengkap dan kode kelas
# Proses: Membersihkan serta menormalkan teks
# Output: Nama bersih, kode kelas, jumlah kata, dan inisial


def normalisasi_nama(nama):
    """Membersihkan spasi dan mengubah nama menjadi title case."""
    return " ".join(nama.strip().split()).title()


def buat_inisial(nama):
    """Membuat inisial dari huruf pertama setiap kata."""
    kata = normalisasi_nama(nama).split()
    return "".join(k[0] for k in kata)


def normalisasi_kode(kode):
    """Mengubah kode kelas menjadi huruf besar dengan pemisah '-'. """
    kata = kode.strip().upper().split()
    return "-".join(kata)


# Input data mahasiswa
nama = input("Nama: ")
kode = input("Kode kelas: ")

# Proses normalisasi
nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama)

# Output
print("\n=== HASIL NORMALISASI DATA MAHASISWA ===")
print("Nama bersih :", nama_bersih)
print("Kode kelas  :", kode_bersih)
print("Jumlah kata :", jumlah_kata)
print("Inisial     :", inisial)
