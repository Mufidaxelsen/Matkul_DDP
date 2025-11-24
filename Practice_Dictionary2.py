data_nilai = {
    'Franco': 90,
    'Ilham': 60,
    'Valir': 70,
    'Argus': 80,
    'Usman': 50
}

for nama, nilai in data_nilai.items():
    ket = "Lulus" if nilai >= 60 else "Gagal"
    print(
        f"Daftar Siswa: {nama} | Nilai: {nilai} | Status: {ket}"
    )   # Diatas adalah [F String]

print()  

for nama in data_nilai.keys():
    print("Daftar Siswa:", nama)
