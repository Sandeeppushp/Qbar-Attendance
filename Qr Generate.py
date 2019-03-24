from MyQR import myqr
import os
import base64

#create a text file and fill the information line by line
f=open('codebreakers.txt','r')
lines = f.read().split("\n")
print (lines)


for i in range(0,len(lines)):
    data=lines[i].encode()
    name=base64.b64encode(data)
    
    version, level, qr_name = myqr.run(
    str(name),
    version = 1,
    level = 'H',
    
    #you can use any picture in the background including gif
    picture = 'a.jpg',
    colorized = True,
    contrast = 1.0,
    brightness = 1.0,
    save_name = str(lines[i]+'.bmp'),
    save_dir = os.getcwd()
    )

