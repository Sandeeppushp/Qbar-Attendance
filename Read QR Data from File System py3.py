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
    #you can change bmp to any other extension i.e jpg png etc.
    if not 'bmp' in f[i]:
        break
    getvalues=decode(Image.open(f[i]))
    getvalues=getvalues[0].data
    getvalues=str(getvalues,'utf-8')

    #remove below line if you dont have its encoding    
    getvalues=str(base64.b64decode(getvalues).decode())
    data.append(getvalues)
    #time.sleep(0.1)

print(len(data))
print(*data, sep = "\n") 
#print(data)
fob=open('savedata.txt','w+')
for i in range(0,len(data)):
    fob.write(data[i]+'\n')
fob.close()
