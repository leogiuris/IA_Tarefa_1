import pygame

BLACK = (  0,   0,   0)
BLUE  = (  0,   0, 255)
BROWN = (150,  75,   0)
GREY  = (200, 200, 200)
GREEN = (  0, 255,   0)
PINK  = (255,   0, 220)
RED   = (255,   0,   0)
WHITE = (255, 255, 255)

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 1200
WINDOW_DIMENSIONS = (WINDOW_HEIGHT, WINDOW_WIDTH)

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

def drawGrid():
    blockSize = 4
    mapChar = GetMap()
    for y in range(0, len(mapChar)): 
       for x in range(0, len(mapChar[y])):
            rect = pygame.Rect(x*blockSize, y*blockSize*2, blockSize, blockSize*2)
            if mapChar[y][x] == 'M':
                pygame.Surface.fill(display, BROWN, rect)
            elif mapChar[y][x] == 'F':
                pygame.Surface.fill(display, GREEN, rect) 
            elif mapChar[y][x] == '.':
                pygame.Surface.fill(display, WHITE, rect)
            elif mapChar[y][x] == 'A':
                pygame.Surface.fill(display, BLUE, rect)
            elif mapChar[y][x] == 'R':
                pygame.Surface.fill(display, BLACK, rect)
            else:
                pygame.Surface.fill(display, RED, rect)

def drawPath(path):
    blockSize = 4

    for etapa in path:
        for node in etapa:
            print(node)
            rect = pygame.Rect(node[1]*blockSize, node[0]*blockSize*2, blockSize, blockSize*2)
            pygame.Surface.fill(display, PINK, rect)
            pygame.display.update()
    
def RunView(path):
    global display
    drawn = False
    pygame.init()
    display = pygame.display.set_mode(WINDOW_DIMENSIONS)
    display.fill(BLACK)
    open =True
    while open:
        if not drawn:
            drawGrid()
            drawPath(path)
            drawn = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                open=False
                pygame.quit()
                quit()
        pygame.display.update()