from turtle import position

class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def _eq_(self, other):
        return self.position == other.position

    def __repr__(self):
        return "("+str(self.position)+")"

def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(parent=None, position=start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    counter2 = 0

    while len(open_list) > 0:
        counter2=counter2+1
        if(counter2 >5):
            break
        # Get the current node
        print("open: ", open_list)
        print("closed: ", closed_list)
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        
        # Found the goal
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

            # # Make sure walkable terrain
            # if maze[node_position[0]][node_position[1]] != 0:
            #     continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            close = 0 
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    close = 1 
                    break
            if close == 0:
            # Create the f, g, and h values
                child.g = current_node.g + 1
                # Manhattan Distance
                child.h = (child.position[0] - end_node.position[0]) + (child.position[1] - end_node.position[1])
                child.f = child.g + child.h

            # Child is already in the open list
                aberto = 0
                for open_node in open_list:
                    if child == open_node:
                        aberto = 1
                        if child.f < open_node.f:
                            open_node.f = child.f
                            open_node.g = child.g
                            open_node.h = child.h
                            open_node.parent = child.parent
                        break
                if aberto == 0:
                    # Add the child to the open list
                    open_list.append(child)