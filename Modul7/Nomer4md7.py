#NOMER 4
import re

f = open ('KEI.html', 'r', encoding='latin1')

teks = f.read()
f.close()

search = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>', teks)

list = []
for i in search:
    x = (i[0],float(i[4]))
    list.append(x)
    
print ('Nomer 4')    
print(list)


