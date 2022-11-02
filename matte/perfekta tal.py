
def perfekt(b):
    perf=0
    for p in range (1,b):
        if b%p==0:
            perf+=p
            
     
    
    if b==perf:
        print(b)
  
     
        




for r in range(1,1000000000000000000000):
    perfekt(r)
