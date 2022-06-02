from algo import positions_etapas, astar, TIME
from jogo import GetMap, RunView

def main():
    totalPath = []
    map = GetMap()
    
    check_etapas = ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                    'B', 'C', 'D', 'E', 'G', 'H', 'I', 'J', 'K', 
                    'L', 'N', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 
                    'W', 'X', 'Y', 'Z']
    num_etapas = len(check_etapas)
    check_points = positions_etapas(map, check_etapas, num_etapas)

    for i in range(num_etapas - 1):
        path = astar(map, check_points[i], check_points[i+1])
        totalPath.append(path)
        print('caminho', i)
        print(path)

    print(TIME)
    print(totalPath)
    RunView(totalPath)

if __name__ == '__main__':
    main()