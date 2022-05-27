from random import randint

def cria_linha():
    l=[]
    i=0
    t=0
    while i<7:
        n=randint(0,1)
        l.append(n)
        t+=n
        i+=1
    if t:
        return l
    else:
        return cria_linha()
    
def cria_matriz():
    i=0
    m=[]
    while i<30:
       m.append(cria_linha())
       i+=1
    return m
