#Nomer3
class Manusia(object):
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaaaam, Namaku ", self.nama)
    def makan(self, s):
        print ("Saya baru saja makan ", s)
        self.keadaan = "kenyang"
    def olahraga(self, k):
        print ("Saya baru saja latihan ", k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self,n):
        return n*2


class Mahasiswa (Manusia):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__ (self):
        s = self.nama + ", NIM " +str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uang saku Rp " + str(self.uangSaku) \
            + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = "kenyang"

    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal=ubah
    def tambahUangSaku(self, tambah):
        self.uangSaku += tambah
        
print("Masukkan Data mahasiswa Di Sini : ")
a=raw_input("Nama      : ")
b=raw_input("NIM       : ")
c=raw_input("Asal      : ")
d=raw_input("Uang Saku : ")
maha=Mahasiswa(a,b,c,d)
"""silahkan ketik 'maha.instruksi' untuk menjalankan
program yang kalian inginkan"""
