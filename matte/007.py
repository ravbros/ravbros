import matte
p=0
num=2
while p<=10001:
    if matte.Primtal(num):
        p+=1
        print(num,p)
    num+=1
