from random import randint

#cria linhas da matriz
def cria_linha(): 
    l=[]
    i=0
    t=0
    while i<7:
        n=randint(0,1) # mudar probabilidade!!!!!!!! assim nao funciona
        l.append(n)
        t+=n
        i+=1
    if t:#checa se pelo menos um membro percorreu o percurso
        return l
    else:
        return cria_linha()
   
#cria matriz [30][7]
def cria_matriz():
    i=0
    m=[]
    while i<30:
       m.append(cria_linha())
       i+=1
    return m

#checa se alguem foi usado mais que 8 vezes
def checa_8(*m):
    i=0
    j=0
    while i<7:
        t=0
        while j<30:
            t+=m[j][i]
            j+=1
        if t>8:
            return i #retorna indice do que apareceu mais de 8 vezes
        i+=1
    return -1

#escolhe um trajeto ao acaso para tirar o personagem 
def conserta_8(i,*m):
    j=randint(0,29)
    m[j][i]=0
    return m #necessario checar novamente

#junta as duas funcoes auxiliares e deixa a matriz dentro os parametros esperados
def conserta_verifica_8(*m):
    n=checa_8(*m)
    while n>-1:
        m=conserta_8(n,*m)
        n=checa_8(*m)
    return m



