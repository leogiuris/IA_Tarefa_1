from algo import *
from map import *


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #map = GetMap()
    start = (0,0)
    end = (3,7)


    #print("len ",len(map))
    #print(map)
    #print('\n')
    #print(map[1])
    print('len', len(maze))

    #start = GetStart()
    #end = GetCheckpoints()

    #end = (7, 6)
    print (start, end)


    path = astar(maze, start, end)

    print('caminho', path)


if __name__ == '__main__':
    main()

