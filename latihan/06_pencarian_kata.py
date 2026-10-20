
# Latihan 6: Pencarian Kata

teks = "Python untuk data. Python untuk pendidikan."
teks = teks.lower()
kata = "python"

print("Kata ditemukan:", kata in teks)
print("Jumlah kemunculan:", teks.count(kata))
print("Posisi pertama:", teks.find(kata))
