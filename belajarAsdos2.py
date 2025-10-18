# nama = "Dhaffa fatir"
# matkul = "Matematika"
# nilai = 70
# nama = input ("Masukan nama mahasiswa: ")
# matkul = input ("Masukan mata kuliah: ")
# nilai = int(input("Masukan nilai: "))

# # menentukan grade nilainya
# if nilai > 85 and nilai <= 100:
#     grade = "A"
# elif nilai >= 75 and nilai < 85:
#     grade = "B"
# elif nilai >= 60 and nilai < 75:
#     grade = "C"
# elif nilai >= 30 and nilai < 60:
#     grade = "D"
# else:
#     grade = "E"

# print ("nama :", nama
#        ,"\nmatkul :", matkul
#        ,"\nnilai :", nilai
#        ,"\ngrade :", grade)



# Latihan Asdos
# nama = input ("Masukan nama mahasiswa: ")
# tinggiBadan = int(input("Masukan Tinggi Badannya: "))
# beratBadan = int(input("Masukan Berat Badannya: "))
# BMI = int(input("Masukan BM internal: "))
# kategori = "kelebihan berat badan"


# # menentukan Rentang BMI & Kategori
# if BMI > 30.0 and BMI <= 30.0:
#     kategori = "Obesitas"
# elif BMI >= 25.0 and BMI < 24.9:
#     kategori = "Kelebihan Berat Badan"
# elif BMI >= 18.5 and BMI < 24.9:
#     kategori = "Ideal"
# elif BMI >= 18.5:
#     kategori = "Kurus"
# else:
#     kategori = "Meninggal"

# print ("nama :", nama
#        ,"\nTinggiBadan :", tinggiBadan
#        ,"\nBeratBadan :", beratBadan
#        ,"\nBMI :", BMI
#        ,"\nKategori :", kategori)

nama = input("Masukan nama mahasiswa: ")
tinggiBadan = int(input("Masukan Tinggi Badannya (cm): "))
beratBadan = int(input("Masukan Berat Badannya (kg): "))

# hitung BMI
BMI = beratBadan / ((tinggiBadan / 100) ** 2)

# menentukan Rentang BMI & Kategori
if BMI > 30.0:
    kategori = "Obesitas"
elif BMI >= 25.0 and BMI <= 30.0:
    kategori = "Kelebihan Berat Badan"
elif BMI >= 18.5 and BMI < 25.0:
    kategori = "Ideal"
elif BMI < 18.5:
    kategori = "Kurus"
else:
    kategori = "Data tidak valid"

print("Nama :", nama,
      "\nTinggi Badan :", tinggiBadan, "cm",
      "\nBerat Badan :", beratBadan, "kg",
      "\nBMI :", round(BMI, 2),
      "\nKategori :", kategori)
