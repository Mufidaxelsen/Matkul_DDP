# def hitungPendapatan():
#     # -----------INPUT DATA---------
#     nama = input('Masukkan nama \t\t:')
#     jabatan = input('Masukkan Jabatan \t:')
#     kepercayaanRohani = input('Masukkan Agamanya \t\t:')
#     jumlah = int(input('Masukkan Jumlah Anak \t:'))
#     # ---------TENTUKAN GAJI POKOK--------
#     def gajiPokok(jabatan):
#         return{
#             "General Manager":20000000,
#             "Manager":10000000,
#             "Staff":5000000
#         }[jabatan]

# # ---------TUNJANGAN ANAK---------
#     persentase = 0.01
#     if(jumlah > 0 and jumlah < 4):
#         tunjanganAnak = gajiPokok(jabatan) * persentase * jumlah
#     elif(jumlah > 3):
#         tunjanganAnak = gajiPokok(jabatan) * persentase * (jumlah-(jumlah-3))
#     else:
#         tunjanganAnak = 0

#     #__________ZAKAT PROFESI__________
#     gajiKotor = gajiPokok(jabatan) * tunjanganAnak
#     zakat = (0.025 * gajiKotor) if gajiKotor >= 10000000 and kepercayaanRohani == "Islam" else 0

#     gajiBersih = (gajiPokok(jabatan) + tunjanganAnak) - zakat


# # .........CETAK POPULASI DATA............
# print('\n\n--------DATA PEGAWAI--------'
#     '\nNama Pegawai\t\t:', nama,
#     '\nJabatan\t\t\t:', jabatan,
#     '\nAgama\t\t\t:', kepercayaanRohani,
#     '\nJumlah Anak\t\t:', jumlah,
#     '\nGaji Pokok\t\t:', gajiPokok(jabatan),
#     '\nTunjangan Keluarga\t:', tunjanganAnak,
#     '\nZakat Profesi\t\t:', zakat,
#     '\nTake Home Pay\t\t:', gajiBersih,
#     )
# # Jalankan Program
# print('\n\n___________INPUT DATA PEGAWAI_________')
# hitungGaji()

#                                                               Dibawah VERSI PEMBENARAN 
#                                                               --SCOPE VARIABEL
#                                                               --Nama Fungsi
#                                                               --Logika Zakat
#                                                               --gajiKotor (kamu salah: harusnya gaji pokok 
#                                                                + tunjangan, bukan gaji pokok × tunjangan)
#                                                               --Typo Variabel
#                                                               --Posisi Print di dalam fungsi

def hitungPendapatan():
    # -----------INPUT DATA---------
    nama = input('Masukkan nama \t\t: ')
    jabatan = input('Masukkan Jabatan \t: ')
    agama = input('Masukkan Agamanya \t: ')
    jumlah = int(input('Masukkan Jumlah Anak \t: '))

    # ---------TENTUKAN GAJI POKOK--------
    def gajiPokok(jabatan):
        return {
            "General Manager": 20000000,
            "Manager": 10000000,
            "Staff": 5000000
        }[jabatan]

    # ---------TUNJANGAN ANAK---------
    persentase = 0.01
    if jumlah > 0 and jumlah < 4:
        tunjanganAnak = gajiPokok(jabatan) * persentase * jumlah
    elif jumlah >= 4:
        tunjanganAnak = gajiPokok(jabatan) * persentase * 3
    else:
        tunjanganAnak = 0

    # ---------ZAKAT PROFESI---------
    gajiKotor = gajiPokok(jabatan) + tunjanganAnak
    zakat = 0.025 * gajiKotor if gajiKotor >= 10000000 and agama == "Islam" else 0

    # ---------GAJI BERSIH---------
    gajiBersih = gajiKotor - zakat

    # ---------CETAK DATA---------
    print('\n\n--------DATA PEGAWAI--------')
    print('Nama Pegawai\t\t:', nama)
    print('Jabatan\t\t\t:', jabatan)
    print('Agama\t\t\t:', agama)
    print('Jumlah Anak\t\t:', jumlah)
    print('Gaji Pokok\t\t:', gajiPokok(jabatan))
    print('Tunjangan Keluarga\t:', tunjanganAnak)
    print('Zakat Profesi\t\t:', zakat)
    print('Take Home Pay\t\t:', gajiBersih)


# Jalankan Program
print('\n\n___________INPUT DATA PEGAWAI_________')
hitungPendapatan()
