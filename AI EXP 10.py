
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

h = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 1, 'F': 0}

def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return

        for neighbor, cost in graph[node]:
            new_g = g + cost
            open_list.append((new_g + h[neighbor], new_g,
                              neighbor, path + [neighbor]))

astar('A', 'F')
