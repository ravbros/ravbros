def delbar(stor,liten):
    return (stor%liten)==0

    
def Primtal(b):
    for p in range (2,b):
        if delbar(b,p):
            return False
    return True
