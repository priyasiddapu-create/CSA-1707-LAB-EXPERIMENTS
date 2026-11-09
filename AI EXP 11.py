
colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

color_map = {}

def solve(region):
    if region == len(graph):
        return True

    place = list(graph.keys())[region]

    for color in colors:
        if all(color_map.get(n) != color for n in graph[place]):
            color_map[place] = color

            if solve(region + 1):
                return True

            del color_map[place]

    return False

if solve(0):
    print("Map Coloring Solution:")
    print(color_map)
else:
    print("No Solution")
