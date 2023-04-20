lines = []
with open('./inputB.txt') as f:
    for line in f:
        lines.append(line.strip())

personas = lines[0][0]
# favores = lines[0][2]

# Precondition
if(personas>favores):
    print("No")
    exit()

lines.pop(0)

edges = []
for l in lines:
    edges.append((l[0],l[2]))

visited = []
for e in edges:
    if e[1] not in visited:
        visited.append(e)

if(int(personas)<len(visited)):
    print("Yes")
else:
    print("No")