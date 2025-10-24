# manipulasi list

# index 0(-4) 1(-3) 2(-2) 3(-1)
data = ['Ramdhan','Fathir','Raffan','Danish','Mupied']

# mengambil data dari list ini
data_0 = data[-1]
print(data_0)
data_0 = data[1]
print(data_0)

# mengambil info panjang list
jumlah_data = len(data)
print(jumlah_data)

# manipulasi list
# menambahkan item kedalam list
# print('\n data sebelum ditambahkan:=\n')
data.insert(1, 'bagas')
print('\n data setelah ditambahkan =\n')

# menambahkan item diakhir
data.insert('hilmi')
print('\n data setelah ditambahkan =\n')

# menambahkan list dengan list
data.insert('faris','kaysan','dirga')
print('\n kelompok gabungan =\n', data)

# merubah item list
# kita akan mengubah jul menjadi KDM
data[3] = "KDM"
print('data yg udah diubah =\n', data)

# menghapus item listt
# kita akan kick hilmi dari kampusss
data.remove('hilmi')
print('data hapus =\n', data)
del data[3]
print('data hapus =\n', data)

# menghapus item list dari belakang
data.pop()
print('data akhir =\n', data)