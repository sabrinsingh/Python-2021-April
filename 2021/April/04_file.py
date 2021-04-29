
score=122
f=open("highscore.txt")
data=f.read()
if(data==""):
    data=0
if(int(data)<score):
    f=open("highscore.txt","w")
    f.write(str(score))
f.close()

with open("highscore.txt") as f:
    print(f.read())