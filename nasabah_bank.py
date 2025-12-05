from Bank import *

    # buat Object
siti = Bank('001','Siti',5000000)
dewi = Bank('002','Dewi',6000000)
andi = Bank('003','Andi',7000000)
budi = Bank('004','Budi',8000000)

# Konsumsi class
siti.nabung(1500000)
dewi.nabung(2500000)
andi.nabung(3500000)
budi.nabung(4500000)

siti.tarik(450000)
budi.tarik(750000)
andi.tarik(950000)
dewi.tarik(650000)
print(Bank.BANK,
"\n==========================")

siti.cetak()
budi.cetak()
andi.cetak()
dewi.cetak()
print("Jumlah Nasabah: %i orang" %Bank.jmlNasabah)