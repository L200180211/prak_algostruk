class Mhs(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

h0 = Mhs("Baity", 211, "Klaten", 240000)
h1 = Mhs("Janna", 228, "Sragen", 230000)
h2 = Mhs("Tika", 222, "Semarang", 250000)
h3 = Mhs("Muahmmad", 232, "Kartasura", 235000)
h4 = Mhs("Azzam", 121, "Boyolali", 240000)
h5 = Mhs("Muzakky", 231, "Kranganyar", 250000)
h6 = Mhs("Addina", 223, "Sukoharjo", 245000)
h7 = Mhs("Hanu", 225, "Sukoharjo", 245000)
h8 = Mhs("Rafa", 233, "Klaten", 245000)
h9 = Mhs("Farida", 234, "Karanganyar", 270000)
h10 = Mhs("Hakim", 229, "Salatiga", 265000)

Daftar = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]

def cariUangSakuTerkecilObject(list):
    temp = [list[0]]
    for i in list[1:]:
        if i.uangSaku < temp[0].uangSaku:
            temp = [i]
        elif i.uangSaku == temp[0].uangSaku:
            temp.append(i)
    return temp

a = cariUangSakuTerkecilObject(Daftar)
print(a)
