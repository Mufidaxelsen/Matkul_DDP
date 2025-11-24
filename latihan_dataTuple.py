tup1 = ('PKI 1', 'PKI 2', 1948, 1965)
tup2 = (1, 2, 3, 4, 5, 6 )
tup3 = ("Kucing","Ikan Cupang","Kelinci","Burung")
print("G30S/PKI tahun", tup1[3])
print("Bilangan Index Antara 1 dan 5 adalah", tup2[1:5])
print("Binatang Kesayanganku adalah", tup3[0])


#tuple index/keynya dimulai dari 0
ar_buah =('Pepaya','Mangga','Pisang','Jambu','Belimbing')
ar_buah = ('Manggis','Markisa') + ar_buah
#cetak
print('Buah index 2:',ar_buah[2])
print('Buah index 4:',ar_buah[4])
#len = jumlah elemen
print('Jumlah Buah :',len(ar_buah))
print('-----cetak all buah------')
for buah in ar_buah:
    print('Buah',buah)
#memotong list
print('Memotong tuple 1 - 4', ar_buah[1:4])