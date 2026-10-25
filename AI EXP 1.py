from heapq import heappush, heappop

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(state):
    return sum(state[i] != goal[i] and state[i] != 0
               for i in range(9))

pq = [(h(start), 0, start, [])]
visited = set()

while pq:
    f, g, state, path = heappop(pq)

    if state == goal:
        for s in path + [state]:
            print(s[:3], s[3:6], s[6:])
        break

    if state in visited:
        continue
    visited.add(state)

    z = state.index(0)
    for n in (z-3, z+3, z-1, z+1):
        if 0 <= n < 9 and abs(z % 3 - n % 3) + abs(z // 3 - n // 3) == 1:
            new = list(state)
            new[z], new[n] = new[n], new[z]
            new = tuple(new)
            if new not in visited:
                heappush(pq, (g + 1 + h(new), g + 1,
                              new, path + [state]))
else:
    print("No solution")
