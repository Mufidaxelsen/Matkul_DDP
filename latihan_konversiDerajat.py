
#Latihan sederhana konversi suhu
print("=== KONVERSI SUHU ===")

celcius = float(input("Masukan data dalam celcius ="))
print("Suhu adalah:",celcius,"Celcius")

#konversi ke fahrenheit
fahrenheit = (9/5) * celcius + 32
print("Suhu dalam fahrenheit adalah:",fahrenheit,"Fahrenheit")

#konversi ke reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah:",reamur,"Reamur")

#konversi ke kelvin
kelvin = celcius + 273.15 
print("Suhu dalam kelvin adalah:",kelvin,"Kelvin")
