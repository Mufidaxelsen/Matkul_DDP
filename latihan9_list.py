ar_buah = ['Pepaya'
,'Mangga','Pisang',
'Jambu', 'Belimbing']
#cetak sebuah element array dgn panggil key/index
ar_buah[2] = 'Apel' #ganti element list
print("buah index 2 =", ar_buah[2])
del ar_buah[4] #hapus element list
print("buah index 4 =", ar_buah[4])

buah2an = ['Stroberi','Pisang','Mangga','Apel','Sorry','Ngga','Level']

print("Buah index 2 :", buah2an[2])

#mengubah buah
buah2an[2] = 'Apel'
print("buah index ke 2 :", buah2an[2])
print("buah index ke 4 :", buah2an[4])

# print
print("-----cetak semua-----")
buah2an.insert(3,'Naga')
buah2an.append("Jeruk")
for buah in buah2an:
    print("Buah", buah)

    