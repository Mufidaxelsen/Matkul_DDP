# 1 - Buat data dictionary
menu = {
    "ayam bakar": 20,
    "ayam goreng": 18,
    "ayam geprek": 22,
    "ayam penyet": 25,
    "ayam panggang": 23,
    "jus jeruk": 8,
    "es teh manis": 5,
    "es teh tawar": 4
}

# 2 - Variabel keranjang dan total
cart = []
total = 0

# 3 - Daftar menu
print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:15} : {value}K")

# 4 - Pesanan menu
while True:
    pesanan = input("Pilih Makanan (q untuk keluar): ").lower()

    if pesanan == "q":
        break
    elif pesanan in menu:
        cart.append(pesanan)
        print(f"➜ {pesanan} ditambahkan ke keranjang.\n")
    else:
        print("❌ Menu tidak ditemukan, coba lagi.\n")

print("-------------------------")

# 5 - Loop pesanan dan total
print("--------- PESANAN ---------")
for item in cart:
    harga = menu[item]
    total += harga
    print(f"{item:15} : {harga}K")

print("\nTotal bayar:", total, "K")
print("---------------------------")
