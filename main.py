from algo import *
from jogo import *

def main():

    maze = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    map = GetMap()
    check_etapas = ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                    'B', 'C', 'D', 'E', 'G',
                    'H', 'I', 'J', 'K', 'L',
                    'N', 'O', 'P', 'Q', 'S', 
                    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    n = len(check_etapas)
    check_points = positions_etapas(map, check_etapas, n)
    for i in range(n-1):
        path = astar(map, check_points[i], check_points[i+1])
        print('caminho', i)
        print(path)

    print(TIME)

if __name__ == '__main__':
    main()

