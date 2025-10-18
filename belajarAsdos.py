pelanggan = "Alfaris Bachtiar"
totalBelanja = 150000

# if totalBelanja >= 100000:
#     print("Selamat anda mendapat hadiah ")
# else:
#     print("Maaf, silahkan belanja lagi")
if totalBelanja > 100000:
    print ("diatas 100 rebu")
elif totalBelanja < 100000:
    print ("dibawah 100 rebu")
else:
    print ("sama dengan 100 rebu")

# statement if dengan ternary
print("diatas 100 ribu") if totalBelanja > 100000 else print("dibawah 100 rebu")  if totalBelanja < 100000 else print("sama dengan 100 rebu")

