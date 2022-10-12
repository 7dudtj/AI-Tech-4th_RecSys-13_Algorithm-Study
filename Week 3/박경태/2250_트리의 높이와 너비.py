n = int(input())
data = {}
parents = {}
for i in range(n) :
    node, l, r = map(int, input().split())
    data[node] = [l, r]
    parents[l] = node

start = list(parents.keys())[0]        
while True :
    if start not in parents :
        root = start
        break
    start = parents[start]

width = []
depth = []
path = [root]
d = 1
while len(width) < len(data) :
    node = path.pop()
    if node == -1 :
        d -= 1
        continue
    l, r = data[node]
    if l != -1 :
        if l not in width :
            d += 1
            path.extend([node, l])
            continue
    depth.append(d)
    width.append(node)
    if r != -1 :
        d += 1
        path.extend([-1, r])
    else :
        d -= 1

max_depth = {}
for index, d in enumerate(depth) :
    if d not in max_depth :
        max_depth[d] = 0
    else :
        max_depth[d] = index - depth.index(d) + 1

max_width = 0
min_level = len(width)
for key, value in max_depth.items() :
    if value > max_width :
        max_width = value
        min_level = key
    elif value == max_width and key < min_level :
        max_width = value
        min_level = key
        
print(min_level, max_width)
