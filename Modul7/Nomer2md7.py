#NOMER 2

import re

o = open("Indonesia.txt", 'r', encoding='latin1')

artikel = o.read()
o.close()
o = r'di\w+'
hasil = re.findall(o,artikel)

print ('Nomer 2')
print(hasil)

