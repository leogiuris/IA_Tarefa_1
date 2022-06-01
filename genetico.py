from random import randint, random
from urllib.parse import _NetlocResultMixinBytes
import numpy as np
#cria linhas da matriz
from copy import deepcopy

NUM_LINES = 31
NUM_COLUMNS = 7

etapa_dif = []
for i in range(1,32):
    etapa_dif.append(10*i)
personagem_agilidade = [1.8, 1.6, 1.6, 1.6, 1.4, 0.9, 0.7]
k = 8

#new cria matrix
def cria_matriz():
    m=np.zero(NUM_LINES, NUM_COLUMNS)
    final=randint(0, NUM_COLUMNS) #definir momo
    n=8
    for i in range(NUM_COLUMNS):
        if i==final:
            n=7
        for num in range(n):
            l=randint(0, NUM_LINES) 
            m[l,i]=1
    if checa_vazio(*m)!=-1:#checa se pelo menos um membro percorreu o percurso
        return cria_matriz(NUM_LINES, NUM_COLUMNS)
    else:
        return m

def cria_novo_line():
    ltot = 0
    line = np.zeros(NUM_COLUMNS)
    while ltot < k:
        n = randint(0, NUM_COLUMNS - 1)
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

def cria_novo_matrix(k):
    m=np.zeros((NUM_LINES, NUM_COLUMNS))
    for i in range(NUM_COLUMNS):
      ltot = 0
      while ltot < k:
         n = randint(0, NUM_LINES - 1)
         if m[n][i] != 1:
               m[n][i] = 1
               ltot += 1
    index = checa_vazio(*m)
    while index != -1:
        n = randint(0, NUM_COLUMNS - 1)
        m[index][n] = 1
        s = -1
        ## atualizar matrix pois agora tem mais de k 1's na coluna
        k = randint(0, NUM_LINES - 1)
        while m[k][n]== 0:
            k = randint(0, NUM_LINES - 1)
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

def bits(n):
    bits = [] 
    while n > 0:
        r = n%2
        n = n//2
        bits.append(r)
    return bits

# assume que soma resultado vai a no maximo n '1s
def soma_bits(a,b, n ):
    r = a+b
    for i in range(n-1):
        if r[i] == 2:
            r[i] = 0
            r[i+1] +=1
    return r

def reproduce1(x,y, n): 
    tuplas = []
    for line in range(NUM_LINES):
        for col in range(NUM_COLUMNS):
            if x[line][col] != y[line][col]:
                tuplas.append((line, col))

    casas_sorteadas = []
    for i in range(n):
        num = randint(0, len(tuplas)-1)
        casas_sorteadas.append(tuplas[num])
        tuplas.pop(i)
	
def reproduce_versaox(*mae,*pai):
    m = np.zeros(NUM_LINES, NUM_COLUMNS)
    for i in range (NUM_COLUMNS):
        if randint(0,1):
           m[:i]=mae[:i]
        else:
            m[:i]=pai[:i]
    if checa_vazio(*m) != -1:
        return reproduce(*mae,*pai)
    else:
        return m
    
    ## np.array
    childs = [x, y]
    bits = np.array([1,0,0,0])
    m = deepcopy(x)
    n = pow(2,n)
    for i in range(n-1): ## criancas podem ser x e y
        matrix = deepcopy(m)
        for j in range(n):
            # percorrer bits
            if bits[j] == 1:
                a = casas_sorteadas[j][0]
                b = casas_sorteadas[j][1]
                matrix[a][b] = y[a][b]
        um = np.array([1,0,0,0])
        bits = soma_bits(bits, um, n)
        if checa_k(*matrix) == -1 and checa_vazio(*matrix) == -1:
            childs.append(matrix)
    return childs

# def reproduce(x,y):
#     ## CUT THE COLUMNS

#     m = np.zeros((NUM_LINES, NUM_COLUMNS))
#     m[:, 0:3] = x[:, 0:3]
#     m[:, 3:8] = y[:, 3:8]
#     n = np.zeros((NUM_LINES, NUM_COLUMNS))
#     n[:, 0:3] = x[:, 0:3]
#     n[:, 3:8] = y[:, 3:8]
#     if checa_vazio(m) == -1:
#         if checa_vazio(n) == -1:
#             a = custo_tempo(etapa_dif, personagem_agilidade, m)
#             b = custo_tempo(etapa_dif, personagem_agilidade, n)
#             if a < b:
#                 return m
#             else:
#                 return n
#         else:
#             return m
#     else:
#         if checa_vazio(n) == -1:
#             return n
#         else:
#             # no child available
#             # conserta?
#             # send parents?
#             # a = custo_tempo(etapa_dif, personagem_agilidade, x)
#             # b = custo_tempo(etapa_dif, personagem_agilidade, y)
#             # if (a < b):
#             #     return x
#             # return y
            # return -1
    

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
        # while len(population) < 1000: ## tamanho pop
        # ideia tirar caras ruins
            new_population = []
            # evaluate best individual...
            for i in range(len(population)):
                x = random_selection(population)
                y = random_selection(population)
                childs = reproduce1(x,y)
                for child in childs:
                    new_population.append(child)
                # p = random()
                # if (p < 0.01):
                #     child = mutate(child)
            print('new pop', len(new_population))
            population = new_population
            time, ind = best_individual(population)
            if time < best_time:
                best_time = time
                fit_ind = ind
                print('time', time)
                print('best_time', best_time)
    return fit_ind

# def cria_linha():
#     l=[]
#     i=0
#     t=0
#     while i < NUM_COLUMNS:
#         n=randint(0,1) # mudar probabilidade!!!!!!!! assim nao funciona
#         l.append(n)
#         t+=n
#         i+=1
#     if t: # checa se pelo menos um membro percorreu o percurso
#         return l
#     else:
#         return cria_linha(NUM_COLUMNS)
   
# #cria matriz [30][7]
# def cria_matriz_velho():
#     i=0
#     m=[]
#     while i < NUM_LINES:
#        m.append(cria_linha())
#        i+=1
#     return m