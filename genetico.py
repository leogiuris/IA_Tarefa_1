from random import randint
import numpy as np
#cria linhas da matriz
def cria_linha(ncols): #ncols = 7
    l=[]
    i=0
    t=0
    while i<ncols:
        n=randint(0,1) # mudar probabilidade!!!!!!!! assim nao funciona
        l.append(n)
        t+=n
        i+=1
    if t:#checa se pelo menos um membro percorreu o percurso
        return l
    else:
        return cria_linha(ncols)
   
#cria matriz [30][7]
def cria_matriz(nlines, ncols): # nlines=30, ncols = 8
    i=0
    m=[]
    while i<nlines:
       m.append(cria_linha(ncols))
       i+=1
    return m

#checa se alguem foi usado mais que k vezes
def checa_k(*m, k):
    i=0
    j=0
    for i in range(len(m[0])):
        t=0
        for j in range(len(m)):
            t+=m[j][i]
            # j+=1
        if t>k:
            return i #retorna indice do que apareceu mais de k vezes
        # i+=1
    return -1

#escolhe um trajeto ao acaso para tirar o personagem 
def conserta_k(i,*m):
    j=randint(0,len(m))
    while (m[j][i] == 0):
        j=randint(0,len(m)) # de fato altera o caminho
    m[j][i]=0
    return m 

#junta as duas funcoes auxiliares e deixa a matriz dentro os parametros esperados
#verifica se algum trajeto está vazio
def conserta_vazio(*m):
    sum = 0
    cols = len(m[0])
    lista = np.zeros(cols, dtype=int)
    for j in range(cols):
        for i in range(len(m)):
            lista[j] += m[i][j]
    
    for i in range(len(m)):
        for j in range(cols):
            sum += m[i][j]
        if sum == 0:
            k = np.argmin(lista) ## menor indice
            lista[k] += 1
            m[i][k] = 1
    return m

def conserta_verifica_k(*m, k):
    n=checa_k(*m, k)
    while n>-1:
        m=conserta_k(n,*m)
        n=checa_k(*m, k)
    return m #necessario checar novamente se nenhum trajeto ficou sem personagens

def conserta_geral(*m, k):
    m = conserta_verifica_k(*m, k)
    m = conserta_vazio(*m)
    return m

# custo do tempo a cada etapa: dificuldade/ agilidade na etapa
def custo_tempo(etapa_dif, personagem_agilidade, matrix_genetica):
    matrix = np.divide(etapa_dif, np.matmul(matrix_genetica, personagem_agilidade))
    return np.sum(matrix)

def mutation(parents, num_offspring):
    
    return
