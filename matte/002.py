import matte
def fib(a,b):
    return a+b


låg=1
hög=2
summa=2
while hög<4000000:
    ny=fib(låg,hög)
    låg=hög
    hög=ny
    if matte.delbar(ny,2):
        summa+=ny
print(summa)
