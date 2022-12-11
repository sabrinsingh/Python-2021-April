words=['sabrin','sabrin singh','sls']
data= True
i=0
f=open("sample.txt","r")
while data:
    content=f.readline().lower()
    i+=1
    for word in words:
        if(word in content):
            print(f"{word} is present in line {i}")
    if content=="":
        data = False

f.close()


