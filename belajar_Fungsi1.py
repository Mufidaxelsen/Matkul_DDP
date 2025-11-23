def hitungUmur(tahun_ini):
    nama = input('Nama Siswa : ')
    tahun = int(input('Tahun Lahir :'))
    umur = tahun_ini - tahun
    print("Siswa dengan nama %s yg lahir pada tahun %i berumur %.2f" %(nama,tahun,umur))

# memanggil fungsi
print('==Data Diri==')
hitungUmur(2025)

# print('Data diri anda')
# hitungUmur(2025)

def infoDerajat():
    lokasi = input('Masukkan Lokasi\t:')
    derajat = int(input('Masukkan Derajat\t:'))
    # ----------Buat Fungsi status Suhu--------
    def status():
        if(derajat <= 0 ):
            kondisi = 'Beku'
        elif(derajat >0 and derajat <= 16):
            kondisi = 'Dingin'
        elif(derajat >16 and derajat <= 20):
            kondisi = 'Sejuk'
        elif(derajat >20 and derajat <= 30):
            kondisi = 'Biasa'
        else:
            kondisi = 'Panas'

        return kondisi
    
    # -----------Cetak Populasi Data----------
    print('\n\n------INFORMASI DERAJAT--------'
    '\nLokasi\t:', lokasi,
    '\nDerajat\t:', derajat,
    '\nKondisi\t:', status())

# jalankan Programnya
print('\n\n--------INFORMASI DERAJAT DI SUATU DAERAH--------')
infoDerajat()