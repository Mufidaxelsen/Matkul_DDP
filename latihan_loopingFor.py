print("----------cetak 1 s/d 20------------")
angka = 20
for no in range(angka):
    no += 1 # no = no + 1
print("Angka",no)
print("----------cetak bilangan ganjil 1 s/d 20------------")
bil = 20
for no in range(bil):
    no += 1 # no = no + 1
    if(no % 2 == 1):
       print("Bilangan Ganjil",no)