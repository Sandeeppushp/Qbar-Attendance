import base64
f=open('attendence.txt','r')
lines = f.read().split("\n")
maindata=[]
for i in range(0,len(lines)):
    maindata.append(base64.b64decode(lines[i]))

print(maindata)

fob=open('att.txt','w+')
for i in range(0,len(maindata)):
    fob.write(maindata[i]+'\n')
fob.close()
