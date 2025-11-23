print("-------Program Evaluasi Nilai Mahasiswa---------")

# input datanya
nama = input("Masukkan nama mahasiswa : ")
tugas = float(input("Masukkan nilai tugas : "))
uts = float(input("Masukkan nilai UTS   : "))
uas = float(input("Masukkan nilai UAS   : "))

# bobot nilainya (tuple)
bobot = (0.30, 0.30, 0.40)

# perhitungan dari nilai akhir
nilai_akhir = (tugas * bobot[0]) + (uts * bobot[1]) + (uas * bobot[2])

# menentukan gradenya
if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 75:
    grade = "B"
elif nilai_akhir >= 65:
    grade = "C"
elif nilai_akhir >= 50:
    grade = "D"
else:
    grade = "E"

# output
print("\n____Hasil Evaluasi____")
print(f"Nama Mahasiswa : {nama}")
print(f"Nilai Akhir    : {nilai_akhir:.2f}")
print(f"Grade          : {grade}")
