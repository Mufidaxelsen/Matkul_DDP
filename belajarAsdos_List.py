# 
data1 = [1,2,3,4,5,6,7,8,9,10]
print(data1)

# skeumpulan data Numbers
data_numbers = [1,2,3]
print(data_numbers)

# sekumpulan data String
data_string = ["ucup","ujang","karbu"]
print(data_string)

# sekumpulan data Boolean
data_numbers = [True,False,True,False]
print(data_numbers)

# sekumpulan data Campuran
data_numbers = ["Ramdhan",4,"Fathir",5]
print(data_numbers)

# list MultiDimensi
list_makanan = [
    ["Bakwan","Cakwe","Donat"],
    ["Jasjus","Nutrisari","ale-ale"],
    ["Nadi uduk","Nasi goreng","Nasi lemak"]
]

print("=====Cetak Peritem======")
print(list_makanan[0][0])
print(list_makanan[1][2])
print(list_makanan[2][2])

print("=====Mencetak semuanya dengan NestedLoop======")
for menu in list_makanan:
    for makanan in menu:
        print(makanan)