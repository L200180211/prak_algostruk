#NOMOR 2
def urutnim(nimku) :
    for nimmhs in range(len(nimku)-1,0,-1) :
        for i in range(nimmhs) :
            if nimku[i] > nimku[i+1] :
                elmt = nimku[i]
                nimku[i] = nimku [i+1]
                nimku[i+1] = elmt

angka = [12,34,45,24,78,90,65,58,2,10]
urutnim(angka)
x = angka

angka1 = [12,34,45,24,78,90,65,58,2,10]
urutnim(angka1)
y = angka1

angka2 = (x+y)
z = angka2
print (z)
