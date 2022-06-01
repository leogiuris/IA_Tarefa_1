import numpy as np
from random import random, randint

NUM_LINES = 31
NUM_COLUMNS = 7
ENERGY = 8
etapa_dif = []
for i in range(1,32):
    etapa_dif.append(10*i)
personagem_agilidade = [1.8, 1.6, 1.6, 1.6, 1.4, 0.9, 0.7]

def checa_vazio(m):    
    for i in range(len(m)):
        sum = m[i].sum()
        if sum == 0:
            return i
    return -1

def garante_vivo(m):
    if m.sum() < NUM_COLUMNS*ENERGY:
        return m
    # muda uma vida pois máximo possivel por construção é NUM_COLUMNS*ENERGY
    i = randint(0, NUM_LINES - 1)
    while m[i].sum() < 2:
        i = randint(0, NUM_LINES - 1)
    j = randint(0, NUM_COLUMNS - 1)
    while m[i][j] == 0:
        j = randint(0, NUM_COLUMNS - 1)
    m[i][j] = 0
    return m

# talvez usar garante_vivo
def cria_novo_matrix():
    m=np.zeros((NUM_LINES, NUM_COLUMNS))
    vivo = randint(0, NUM_COLUMNS-1)
    for i in range(NUM_COLUMNS):
      ltot = 0
      if i == vivo:
          ltot = 1 ## i irá sobreviver
      while ltot < ENERGY:
         n = randint(0, NUM_LINES - 1)
         if m[n][i] != 1:
               m[n][i] = 1
               ltot += 1
    index = checa_vazio(m)
    while index != -1:
        n = randint(0, NUM_COLUMNS - 1)
        m[index][n] = 1
        ## atualizar matrix pois agora tem mais de k 1's na coluna
        k = randint(0, NUM_LINES - 1)
        while m[k][n]== 0:
            k = randint(0, NUM_LINES - 1)
        m[k][n] = 0
        index = checa_vazio(*m)
    return m 

def custo_tempo(etapa_dif, personagem_agilidade, matrix_genetica):
    matrix = np.divide(etapa_dif, np.matmul(matrix_genetica, personagem_agilidade))
    return np.sum(matrix) # returna tempo total de todas etapas

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
    times = list()
    for person in population:
        times.append(person[1])
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
    return population[j] # (person, time)

def best_individual(population):
    population.sort(key=lambda y: y[1]) #sort by time
    best_time = population[0][1]
    best_person = population[0][0]
    return best_time, best_person

def die(population, max):
    tam = len(population)
    excess = tam - max
    # tupla (child, time)
    population.sort(key=lambda y: y[1])
    for i in range(1,excess+1):
        population.pop(tam-i)
    # return population

def repetition(population, potential_child):
    for child in population:
        if np.array_equal(child[0], potential_child[0]):
            return 1
    return 0

# mae  = matrix
def reproduce(mae, pai):
    m = np.zeros((NUM_LINES, NUM_COLUMNS))
    for i in range (NUM_COLUMNS):
        if randint(0,1):
           m[:, i]=mae[:, i]
        else:
            m[:, i]=pai[:, i]
    if checa_vazio(m) != -1: 
        return reproduce(mae,pai)
    m = garante_vivo(m)
    return m


def genetic_algorithm(population): ## population list of matrices
    best_time, fit_ind = best_individual(population)
    print('best_time', best_time)
    count_change = 0
    while count_change < 50:
        new_population = []
        # evaluate best individual...
        for i in range(100):
            x = random_selection(population) # (person, time)
            y = random_selection(population)
            while np.array_equal(x[0],y[0]):
                y = random_selection(population)
            child = reproduce(x[0],y[0])
            tempo_child = custo_tempo(etapa_dif, personagem_agilidade, child)
            if repetition(new_population, child) == 0:
                new_population.append((child, tempo_child))
            # p = random()
            # if (p < 0.01):
            #     child = mutate(child)
        for person in population:
            new_population.append(person)
        population = new_population
        print('new pop', len(population))
        if len(population) > 2000:
            die(population, 2000)
            print('new pop after massive deaths', len(population))
        time, ind = best_individual(population)
        if time < best_time:
            best_time = time
            fit_ind = ind
            print('time', time)
            print('best_time', best_time)
        else:
            count_change += 1
            
    return fit_ind
