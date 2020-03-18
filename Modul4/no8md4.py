Dalam kasus ini menggunakan konsep Big-O. Yang mana rumus yang dipakai adalah rumus O(log n)
dengan rincian 1 = 1, 2 = 2, 4 = 3, 10 = 4, 100 = 7, 1000=10.
Yang nantinya log itu berasal dari pangkat log berbasis 2. Sehingga dapat mengetahui jumlah
maksimal tebakan.
Untuk pola adalah sebagai berikut:
        apabila ingin menebak angka 80
        
        a = nilai tebakan pertama // 2
        tebakan selanjutnya = nilai tebakan "lebih dari" + a
        *jika hasil tebakan selanjutnya "kurang dari", maka nilai yang dipakai
        tetap nilai lebih dari sebelumnya*
        a = a // 2
        
    Untuk simulasinya adalah sebagai berikut 
        tebakan ke 1: 50 (mengambil nilai tengah) jawaban= "itu terlalu kecil"
        tebakan ke 2: 90 (dari 50 + 25) jawaban = "itu terlalu besar"
        tebakan ke 3: 70 (dari 50 + 12) jawaban = "itu terlalu kecil"
        tebakan ke 4: 78 (dari 72 + 6) jawaban = "itu terlalu besar"
        tebakan ke 5: 81 (dari 78 + 3) jawaban = "itu terlalu besar"
        tebakan ke 6: 79 (dari 78 + 1) jawaban = "itu terlalu kecil"
        tebakan ke 7: antara 81 dan 79 hanya ada 1 angka yaitu 80
        jadi angka yang harus ditebak pada tebakan ketujuh adalah angka 80

