import matte
b=0
for o in range(1,1000):
    if matte.delbar(o,3)or matte.delbar(o,5):
        b+=o
print(b)
        
