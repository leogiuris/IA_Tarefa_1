import numpy as np
from random import random, randint, randrange, choices
from copy import deepcopy
NUM_LINES = 31
NUM_COLUMNS = 7
ENERGY = 8
MAX_POPULATION = 1500 ## 2000 roudou
etapa_dif = [] #1823.960333872418 em 11 min 34
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

def checa_vivo(m):
    n = deepcopy(m)
    n = n.T
    for i in range(len(n)):
        if n[i].sum() > ENERGY:
            return i
    if n.sum() < NUM_COLUMNS*ENERGY:
        return -1
    return 0

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
        index = checa_vazio(m)
    return m 

def custo_tempo(matrix_genetica):
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

def random_selection_pair(population):
    times = [float(population[i][1]) for i in range(len(population))]
    times = np.divide(1, times) 
    return choices(population, weights=times, k=2)

def best_individual(population):
    print(population[0][0])
    population.sort(key=lambda y: y[1]) #sort by time
    best_time = population[0][1]
    best_person = population[0][0]
    return (best_time, best_person)

def cria_prob(lista):
    probs = np.divide(lista, np.sum(lista)) ## normaliza 
    lista_probs = []
    psum = 0
    for i in range(len(probs)):
        psum += probs[i]
        lista_probs.append(psum)
    return lista_probs

def die(population, max):
    tam = len(population)
    excess = tam - max
    # tupla (child, time)
    population.sort(key=lambda y: y[1]) ## ordena
    times = [float(population[i][1]) for i in range(len(population))]
    for i in range(1,excess+1):
        lista_probs = cria_prob(times)
        p = random()
        j = busca(p, lista_probs)
        while j < 10: # nao mata 10 primeiros
            p = random()
            j = busca(p, lista_probs)
        population.pop(j)
        times.pop(j)
    # return population

def die_optimal(population, max, BEST):
    tam = len(population)
    excess = tam - max
    # tupla (child, time)
    population.sort(key=lambda y: y[1]) ## ordena
    times = [float(population[i][1]) for i in range(len(population))]
    deaths = choices(population[BEST:], weights = times[BEST:], k = excess)
    deaths_index = list()
    for index, individual in enumerate(population):
        for dead in deaths:
            if np.array_equal(individual[0], dead[0]):
                deaths_index.append(index)
    count_remove = 0  
    for i in len(deaths_index):
        index = deaths_index[i] - count_remove
        population.pop(index)
        count_remove += 1
    return population

def mutation(person, probability = 0.3):
    if random() < probability:
        kshift = randrange(NUM_LINES)
        person = np.roll(person, NUM_COLUMNS*kshift)
    return person

def swap(person):
    new_person = deepcopy(person)
    p1 = randrange(NUM_COLUMNS)
    p2 = p1
    while p2 == p1:
        p2 = randrange(NUM_COLUMNS)

    for s1 in range(NUM_LINES):
        for s2 in range(s1, NUM_LINES):
            swaped = deepcopy(new_person[0])
            swaped[s1][p1] = new_person[0][s1][p2]
            swaped[s1][p2] = new_person[0][s1][p1]
            swaped[s2][p2] = new_person[0][s2][p1]
            swaped[s2][p1] = new_person[0][s2][p2]
            if checa_vazio(swaped) == -1 and checa_vivo(swaped)==-1:
                swaped = garante_vivo(swaped)
                tempo_swaped = custo_tempo(swaped)
                if tempo_swaped < new_person[1]:
                    new_person = (swaped, tempo_swaped)
    return new_person
     
def repetition(population, potential_child):
    for child in population:
        if np.array_equal(child[0], potential_child[0]):
            return 1
    return 0

# mae  = matrix
def reproduce(parent1, parent2):
    childs = []
    child1 = np.zeros((NUM_LINES, NUM_COLUMNS))
    child2 = np.zeros((NUM_LINES, NUM_COLUMNS))
    for i in range (NUM_COLUMNS):
        if randint(0,1):
           child1[:, i] = parent1[:, i]
           child2[:, i] = parent2[:, i]
        else:
            child1[:, i] = parent2[:, i]
            child2[:, i] = parent1[:, i]
    if checa_vazio(child1) == -1:
        child1 = garante_vivo(child1)
        childs.append(child1)
        if checa_vazio(child2) == -1:
            child2 = garante_vivo(child2)
            childs.append(child2)
    elif checa_vazio(child2) == -1:
        child2 = garante_vivo(child2)
        childs.append(child2)
    else:
        return reproduce(parent1,parent2)
    return childs


def genetic_algorithm(population, BEST): ## population: (persosn, time)
    count_stop = 0
    iter = 0
    while count_stop < 50:
        population.sort(key=lambda person: person[1]) #sort by time
        best_time = population[0][1]
        best_individual = population[0][0]

        
        print('iter', iter)
        print('count_stop', count_stop)
        new_population = population[0:500] #mantém melhores 500 habitantes ## chegou a 1923 em 4 min
        #new_population = population
        for i in range(len(population)//2):
            parents = random_selection_pair(population) # [(person1, time1), (person2, time2)]
            
            childs = reproduce(parents[0][0], parents[1][0])
            for child in childs:
                child = mutation(child)        
                if repetition(new_population, child) == 0:
                    tempo_child = custo_tempo(child)
                    new_population.append((child, tempo_child))


        population = new_population
        print('new pop', len(population))
        if len(population) > MAX_POPULATION:
            die_optimal(population, MAX_POPULATION)
            print('new pop after massive deaths', len(population))
        
        population.sort(key=lambda person: person[1])
        for i, genome in enumerate(population[0:BEST]): # Realiza o swap nas BEST melhores soluções
            swaped = swap(genome) 
            population[i] = swaped
        population.sort(key=lambda person: person[1])
        time = population[0][1]
        individual = population[0][1]
        if time < best_time:
            best_time = time
            best_individual = individual
            count_stop = 0
        
        else:
            count_stop += 1
        print('time', time)
        print('best_time', best_time)
        iter += 1    
    return best_individual
def initial_population(n):
    population = list()
    count = 0
    while count < n:
        potential_person = cria_novo_matrix()
        if repetition(population, potential_person) == 0:
            tempo = custo_tempo(potential_person)
            population.append((potential_person, tempo))
            count +=1
    return population