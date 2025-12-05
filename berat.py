class BeratIdeal:
    # Atribut
    tinggi = 0
    berat = 0

    def __init__(self, tinggi, berat):
        self.tinggi = tinggi
        self.berat = berat
        
                                        # PEMANGGILAN berat.py dan gempa.py DIJALANKAN DI mainGempa.py
    def perhitungan(self):
        bmi = self.berat / (self.tinggi * self.tinggi)
        if bmi <18.5:
            ket = "Kurus"
        elif bmi >= 18.5 and bmi < 24.9:
            ket = "Ideal"
        elif bmi >= 25 and bmi <= 29.9:
            ket = "gemuk"
        else:
            ket = "Obesitas"
        print(f"Hasil perhitungan BMI dengan\n"
              f"Berat: {self.berat}\n"
              f"Tinggi: {self.tinggi}\n"
              f"Keterangan: {ket}")
        
        # PANGGIL OBJEKNYA
        # Contoh input manual
        # obj = BeratIdeal(1.70, 60)  # tinggi dalam meter, berat dalam kg
        # obj.perhitungan()

   