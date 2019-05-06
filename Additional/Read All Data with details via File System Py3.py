from pyzbar.pyzbar import decode
from PIL import Image
from os import walk
import base64
import time

f = []
for (dirpath, dirnames, filenames) in walk("."):
    f.extend(filenames)
    break
#print(f)
print(*f, sep = "\n")
print('\n\n\n')

data=[]

for i in range(0,len(f)):
    if not 'bmp' in f[i]:
        break
    try:            
        getvalues=decode(Image.open(f[i]))
        getvalues=getvalues[0].data
        getvalues=str(getvalues,'utf-8')
        getvalues=str(base64.b64decode(getvalues).decode())
        data.append(getvalues)
        #time.sleep(0.1)
    except(IndexError):
        pass

print(len(data))
print(*data, sep = "\n") 
#print(data)
fob=open('savedata.txt','w+')
for i in range(0,len(data)):
    fob.write(data[i]+'\n')
fob.close()

input('\n\n\nAll Data is Saved in a text File savedata.txt')
