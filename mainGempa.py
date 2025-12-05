from gempa import *
from berat import *

b1 = BeratIdeal(1.7, 99)
g1 = Gempa('Aceh',4)
g2 = Gempa('Bandung',2)
g3 = Gempa('Tokyo',4.4)
g4 = Gempa('Sydney',3.3)
g5 = Gempa('Texas',4.0)

b1.perhitungan()
g1.dampak()
g2.dampak()
g3.dampak()
g4.dampak()
g5.dampak()
