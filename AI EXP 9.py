
from itertools import permutations

d = [[0, 10, 15, 20],
     [10, 0, 35, 25],
     [15, 35, 0, 30],
     [20, 25, 30, 0]]

n = len(d)
best = float('inf')

for p in permutations(range(1, n)):
    path = (0,) + p + (0,)
    cost = sum(d[path[i]][path[i+1]] for i in range(n))
    if cost < best:
        best = cost
        route = path

print("Best Path:", route)
print("Minimum Cost:", best)
