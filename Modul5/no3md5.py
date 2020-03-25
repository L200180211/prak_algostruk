from time import time as detak
from random import shuffle as kocok

def bubbleSort(X) :
    n = len (X)
    for i in range(n-1) :
        for j in range(n-i-1) :
            if X[j] > X[j+i] :
                swap (X, j, j+1)

def selectionSort(X) :
    n = len (X)
    for i in range(n-1) :
        indeksKecil = mencariYangPalingKecil(X, i, n)
        if indeksKecil != i :
            swap (X, i, indeksKecil)

def insertSort(X) :
    n = len (X)
    for i in range (1, n) :
        nilai = X[i]
        abc = i
        while abc > 0 and nilai < X[abc-1] :
            X[abc] = X[abc-1]
            abc = abc-1
        X[abc] = nilai

def swap (X, a, b) :
    klm = X[a]
    X[a] = X[b]
    X[b] = klm

def mencariYangPalingKecil(X, awal, pilihanberhenti) :
    palingKecil = awal
    for i in range (awal+1, pilihanberhenti) :
        if X[i] < X[palingKecil] :
            palingKecil = i
    return palingKecil

k = []
for i in range(1, 6001) :
    k.append(i)

kocok(k)

u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak () ; bubbleSort (u_bub) ; ak = detak() ; print('bubble : % g detik' % (ak - aw)) ;
aw = detak () ; selectionSort (u_sel) ; ak = detak() ; print('selection : % g detik' % (ak - aw)) ;
aw = detak () ; insertSort (u_ins) ; ak = detak() ; print('insert : % g detik' % (ak - aw)) ;
