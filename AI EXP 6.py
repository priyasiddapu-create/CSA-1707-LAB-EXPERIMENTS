room = {'A': 1, 'B': 1}
pos = 'A'

while 1 in room.values():
    if room[pos] == 1:
        print("Clean", pos)
        room[pos] = 0
    else:
        pos = 'B' if pos == 'A' else 'A'
        print("Move to", pos)

print("Both rooms are clean!")
