from random import randint, random
from urllib.parse import _NetlocResultMixinBytes
import numpy as np
#cria linhas da matriz


etapa_dif = []
for i in range(1,32):
    etapa_dif.append(10*i)
personagem_agilidade = [1.8, 1.6, 1.6, 1.6, 1.4, 0.9, 0.7]
nlines = 31
ncols = 7
k = 8

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

#new cria matrix

def cria_novo_line(ncols, k):
    ltot = 0
    line = np.zeros(ncols)
    while ltot < k:
        n = randint(0,ncols-1)
        if line[n] != 1:
            line[n] = 1
            ltot += 1
    return line
        
# cada linha com k 1's
# cria matrix
def checa_vazio(*m):    
    for i in range(len(m)):
        sum = m[i].sum()
        if sum == 0:
            return i
    return -1

def cria_novo_matrix(nlines, ncols, k):
    m=np.zeros((nlines, ncols))
    for i in range(ncols):
      ltot = 0
      while ltot < k:
         n = randint(0,nlines-1)
         if m[n][i] != 1:
               m[n][i] = 1
               ltot += 1
    index = checa_vazio(*m)
    while index != -1:
        n = randint(0,ncols-1)
        m[index][n] = 1
        s = -1
        ## atualizar matrix pois agora tem mais de k 1's na coluna
        k = randint(0, nlines-1)
        while m[k][n]== 0:
            k = randint(0, nlines-1)
        m[k][n] = 0
        index = checa_vazio(*m)
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
# MELHORAR 
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
    
    #### ERRO - E SE TODOS FORAM USADOS 8 VEZES E ALGUM PATH ESTÁ VAZIO
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

### ERRO POIS ERRO EM CONSERTA_VAZIO
def conserta_geral(*m, k):
    m = conserta_verifica_k(*m, k)
    m = conserta_vazio(*m)
    return m


# custo do tempo a cada etapa: dificuldade/ agilidade na etapa
def custo_tempo(etapa_dif, personagem_agilidade, matrix_genetica):
    matrix = np.divide(etapa_dif, np.matmul(matrix_genetica, personagem_agilidade))
    return np.sum(matrix)



def busca(p, lista): # returna indice i em que lista[i-1] < p < lista[i]
	low = 0
	high = len(lista) - 1
	while low <= high:
		middle = low + (high - low) // 2
		if lista[middle] >= p and lista[middle-1] < p: # lista[middle-1] < p <= lista[middle]
			return middle
		elif lista[middle] <= p:
			low = middle + 1 
		else:
			high = middle - 1
	return 0

def random_selection(population):
    times = [custo_tempo(etapa_dif, personagem_agilidade, person) for person in population]
    times = np.divide(1, times) 
    probs = np.divide(times, np.sum(times)) ## mais provavel, menor tempos
    lista = []
    psum = 0
    n= len(probs)
    for i in range(n):
        psum += probs[i]
        lista.append(psum)
    p = random()
    j = busca(p, lista)
    return population[j] 


def reproduce(x,y):
    ## CUT THE COLUMNS

    m = np.zeros((nlines, ncols))
    m[:, 0:3] = x[:, 0:3]
    m[:, 3:8] = y[:, 3:8]
    n = np.zeros((nlines, ncols))
    n[:, 0:3] = x[:, 0:3]
    n[:, 3:8] = y[:, 3:8]
    if checa_vazio(m) == -1:
        if checa_vazio(n) == -1:
            a = custo_tempo(etapa_dif, personagem_agilidade, m)
            b = custo_tempo(etapa_dif, personagem_agilidade, n)
            if a < b:
                return m
            else:
                return n
        else:
            return m
    else:
        if checa_vazio(n) == -1:
            return n
        else:
            # no child available
            # conserta?
            # send parents?
            # a = custo_tempo(etapa_dif, personagem_agilidade, x)
            # b = custo_tempo(etapa_dif, personagem_agilidade, y)
            # if (a < b):
            #     return x
            # return y
            return -1
    

def best_individual(population):
    times = [custo_tempo(etapa_dif, personagem_agilidade, person) for person in population]    
    best_time = times[0]
    index = 0
    for i in range(1, len(times)):
        if times[i] < best_time:
            best_time = times[i]
            index = i
    return best_time, population[index]
        
def genetic_algorithm(population,n): ## population list of matrices
    best_time, fit_ind = best_individual(population)
    print('best_time', best_time)
    for j in range(n):
        new_population = []
        # evaluate best individual...
        for i in range(len(population)):
            x = random_selection(population)
            y = random_selection(population)
            child = reproduce(x,y)
            # p = random()
            # if (p < 0.01):
            #     child = mutate(child)
            if isinstance(child, int):
                new_population.append(child)
        print('new pop', len(new_population))
        population = new_population
        time, ind = best_individual(population)
        if time < best_time:
            best_time = time
            fit_ind = ind
            print('time', time)
            print('best_time', best_time)
    return fit_ind