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

def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan)-1
    while low <= high:
        mid = (high+low)//2
        if kumpulan[mid] == target:
            return mid
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
print(binSe(kumpulan, 5))
