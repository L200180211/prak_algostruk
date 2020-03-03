
def jumlahHurufVokal(hruf):
    vokal= "AIUEOaiueo"
    a=0
    hasil=0
    for i in hruf:
        if i in vokal:
            a += len(i)
        else:
            a += 0
    hasil = len (hruf),a
    return hasil
