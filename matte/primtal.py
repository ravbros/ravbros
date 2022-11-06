def primtal(b):
    prim=True
    for p in range (2,sqrt(b)):
        if b%p==0:
            prim=False
            break
        #print(b,p,div== round(div))
    if prim:
        print(b)
  
     
        




for r in range(1,1000000000000):
    primtal(r)
