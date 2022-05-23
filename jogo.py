import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
mapChar = []
def GetMap():
    f = open('MAPA_LENDA-AANG.txt','r')
    lines = f.readlines()
    for line in lines:
        lista = []
        for char in line:
            lista.append(char)
        mapChar.append(lista)

      


def drawGrid():
    #blockSizex = 5 #Set the size of the grid block
    blockSize = 1
    GetMap()
    for y in range(0, 82, blockSize): 
       for x in range(0, 301, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            if mapChar[y][x] == 'M':
                pygame.Surface.fill(display, (255,248,220), rect, 1)
            elif mapChar[y][x] == 'F':
                pygame.Surface.fill(display, (0,10,0), rect, 1) 
            elif mapChar[y][x] == '.':
                pygame.Surface.fill(display, (1,1,1), rect, 1)
            elif mapChar[y][x] == 'A':
                pygame.Surface.fill(display, (0,0,1), rect, 1)
            else:
                pygame.Surface.fill(display, (0,0,0), rect, 1)


def main():
    global display
    pygame.init()
    display = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    display.fill((200,200,200))
    open =True
    while open:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                open=False
                pygame.quit()
                quit()
        pygame.display.update()

main()