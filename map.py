
mapChar = []
mapCost = []


def GetStart():
    for i,line in enumerate(mapChar):
        for j,el in enumerate(line):
            if el == '0':
                return (i,j)


# a ideia é pegar todos os checkpoints e passar uma lista de tuplas
def GetCheckpoints():
    for i,line in enumerate(mapChar):
        for j,el in enumerate(line):
            if el == '1':
                return (i,j)


def SetCost(val):
    if(val == 'A'):
        return 1
    else:
        return 0


def GetMap():
    f = open('MAPA_MENOR.txt','r')
    lines = f.read()
    for el in lines.split('\n'):
        if len(el) < 2:
            continue
        mapChar.append(el)
        difs = []
        for ch in el:
            difs.append(int(SetCost(ch)))
        mapCost.append(difs)

    #print(*mapChar, sep = '\n')
    return mapCost
    
