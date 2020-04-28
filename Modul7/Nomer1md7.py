# NOMER 1

import re

o = open("Indonesia.txt", 'r', encoding='latin1')

artikel = o.read()
o.close()
o = r'me\w+'
hasil = re.findall(o,artikel)

print ('Nomer 1\n')
print (hasil)

