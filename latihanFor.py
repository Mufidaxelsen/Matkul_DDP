# Cetak angka 1 sd 10
angka = 10
for no in range (angka):
    # no = no + 1
    no += 1
    print("Bilangan", no)

print ("----------Cetak bilangan genap-----------")
bil = 20
for bil in range (bil):
    # no = no + 1
    bil += 1
    if (bil % 2 == 0):
        print("Bilangan genap", bil)

print ("----------Cetak bilangan ganjil-----------")
no = 10
for no in range (no):
    # no = no + 1
    no += 1
    if (no % 2 == 1):
        print("Bilangan genap", no)
