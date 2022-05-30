from turtle import position
import numpy as np
class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.t = 0 # tempo de percurso
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return str(self.position)

def time(char):
    if char == '.':
        return 1
    elif char == 'R':
        return 5
    elif char == 'V':
        return 10
    elif char == 'A':
        return 15
    elif char == 'M':
        return 200
    return 0

def positions_etapas(maze, lista, n):
    v = np.zeros(n, dtype=object) #python sets for anything for array that way
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            for index, elem in enumerate(lista):
                if maze[x][y] == elem:
                    v[index] = (x, y)
    return v

def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(parent=None, position=start)
    start_node.g = start_node.h = start_node.t =start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.t = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    # counter2 = 0

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        
        # print("closed: ", closed_list)

        # Found the goal
        # print('current', current_node)
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        # Adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue
            
            # Create new node
        
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if child not in closed_list:
            # Create the f, g, and h values
                child.g = current_node.g + 1
                
                child.t = current_node.t + time(maze[child.position[0]][child.position[1]])
                # Manhattan Distance
                child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
                child.f = child.g + child.h + child.t
                

            # Child is already in the open list
                aberto = 0
                for open_node in open_list:
                    if child == open_node:

                        aberto = 1
                        if child.f < open_node.f:
                            open_node.f = child.f
                            open_node.g = child.g
                            open_node.h = child.h
                            open_node.t = child.t
                            open_node.parent = child.parent
                        break
                if aberto == 0:
                    # Add the child to the open list
                    open_list.append(child)