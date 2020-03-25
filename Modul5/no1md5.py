#NOMER 1

class MhsTIF(object) :
    def __init__(self, nama, nim, asal, uangsaku) :
        self.nama = nama
        self.nim = nim
        self.asal = asal
        self.uangsaku = uangsaku

def urutnim(nimku) :
    for nimmhs in range(len(nimku)-1,0,-1) :
        for i in range(nimmhs) :
            if nimku[i] > nimku[i+1] :
                elmt = nimku[i]
                nimku[i] = nimku [i+1]
                nimku[i+1] = elmt

m0 = MhsTIF('Baity', 9, 'Klaten', 300000)
m1 = MhsTIF('Lutfi', 10, 'Semarang', 320000)
m2 = MhsTIF('Mifta', 23, 'Kartasura', 350000)
m3 = MhsTIF('Falah', 45, 'Solo', 290000)
m4 = MhsTIF('Dewi', 27, 'Karanganyar', 310000)
m5 = MhsTIF('Lia', 56, 'Wonogiri', 380000)
m6 = MhsTIF('Bagus', 2, 'Boyolali', 280000)
m7 = MhsTIF('Wahyu', 8, 'Sragen', 330000)
m8 = MhsTIF('Laila', 34, 'Purwodadi', 340000)
m9 = MhsTIF('Alfina', 60, 'Sleman', 390000)
m10 = MhsTIF('Wafiq', 51, 'Magelang', 370000)

urut =[m0.nim, m1.nim, m2.nim, m3.nim, m4.nim, m5.nim, m6.nim, m7.nim, m8.nim, m9.nim, m10.nim]
urutnim(urut)
print(urut)
