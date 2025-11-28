
print("--------Input Nilai Siswa-----------")
nama = input("Nama\t\t: ")
matpel = str(input("Mata Pelajaran\t: "))
nilai = float(input("Nilai\t\t: "))
#tuple & list
ket = ("Gagal","Lulus")[nilai >= 60]
print("--------Data Nilai Siswa-----------"
    "\nNama\t\t: %s"
    "\nMata Pelajaran\t: %s"
    "\nNilai\t\t: %.2f"
    "\nKeterangan\t: %s"
    %(nama,matpel,nilai,ket)
    )
