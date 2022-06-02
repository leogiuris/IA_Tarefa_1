

import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (0, 0, 255)
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 1200

def GetMap():
    mapChar = []
    f = open('MAPA_LENDA-AANG.txt','r')
    lines = f.read().splitlines()
    for line in lines:
        lista = []
        for char in line:
            lista.append(char)
        mapChar.append(lista)
    return mapChar

def pontos_get_map(map):
    lista = []
    soma = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            count  = 0
            for i in ['M', 'F', '.', 'A', 'R']:
                if (map[y][x] == i):
                    count = 1
            if count == 0:
                lista.append(map[y][x])
            if map[y][x] == '\n':
                soma +=1
    print('soma ', soma)
    return lista

def drawGrid():
    #blockSizex = 5 #Set the size of the grid block
    blockSize = 4
    mapChar = GetMap()
    for y in range(0, len(mapChar), 1): 
       for x in range(0, len(mapChar[y]), 1):
            rect = pygame.Rect(x*blockSize, y*blockSize*2, blockSize, blockSize*2)
            if mapChar[y][x] == 'M':
                pygame.Surface.fill(display, (255,248,220), rect, 1)
            elif mapChar[y][x] == 'F':
                pygame.Surface.fill(display, (0,10,0), rect, 1) 
            elif mapChar[y][x] == '.':
                pygame.Surface.fill(display, (1,1,1), rect, 1)
            elif mapChar[y][x] == 'A':
                pygame.Surface.fill(display, (0,0,1), rect, 1)
            elif mapChar[y][x] == 'R':
                pygame.Surface.fill(display, (0,0,0), rect, 1)
            else:
                pygame.Surface.fill(display, (1,0,0), rect, 1)


def drawPath(path):
    blockSize = 4

    for block in path:
        rect = pygame.Rect(block[0]*blockSize, block[1]*blockSize*2, blockSize, blockSize*2)
        pygame.Surface.fill(display, (255, 0, 220), rect, 1)
    


def RunView(path):
    global display
    pygame.init()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    display.fill(BLACK)
    open =True
    while open:
        drawGrid()
        drawPath(path)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                open=False
                pygame.quit()
                quit()
        pygame.display.update()

