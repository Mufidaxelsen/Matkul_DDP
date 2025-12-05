class Gempa:
    # Artibut Class
    lokasi = ""
    skala = 0

    # Method Konstruktor
    def __init__(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala

    # Method 2 Menghitung dampak
    def dampak(self):
        if self.skala < 2:
            ket = "Tidak terasa"
        elif self.skala >=2 and self.skala <4:
            ket = "Bangunan retak-retak"
        elif self.skala >=4 and self.skala < 6:
            ket = "Bangunan pada roboh"
        else:
            ket = "Berpotensi Tsunami"
        print(f'telah terjadi Gempa di {self.lokasi} dengan skala {self.skala} Ritcher, berdampak {ket} ')
        