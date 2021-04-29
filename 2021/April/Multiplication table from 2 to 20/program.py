for i in range(2,21):
    for j in range(1,11):
        f=open(f"Multiplication table of {i}.txt","a")
        f.write(f"{i}  * {j} = {i * j}\n")
        f.close()