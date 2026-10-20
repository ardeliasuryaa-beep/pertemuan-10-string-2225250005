
# Latihan 4: Membersihkan Teks

teks = " belajar    python  untuk           pendidikan       "

# Menghapus spasi di awal dan akhir serta merapikan
# spasi berlebih di antara kata
teks = " ".join(teks.split())

print(teks.capitalize())
