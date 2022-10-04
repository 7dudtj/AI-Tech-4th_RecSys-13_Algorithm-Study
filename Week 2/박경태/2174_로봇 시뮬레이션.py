a, b = map(int, input().split())
n, m = map(int, input().split())
direction = {'N':[-1, 0], 'E':[0, 1], 'S':[1, 0], 'W':[0, -1]}
d_keys = ['N', 'E', 'S', 'W']
robots = []
maps = [[0 for i in range(a)] for j in range(b)]
for i in range(n) :
    x, y, d = input().split()
    x, y = int(x)-1, b-int(y)
    robots.append([x, y, d])
    maps[y][x] = i + 1
    
for i in range(m) :
    r, order, count = input().split()
    r, count = int(r), int(count)
    robot = robots[r-1]
    x, y, d = robot
    d_key = d_keys.index(d)
    if order == 'L' :
        d_key -= count
        robots[r-1] = [x, y, d_keys[d_key % 4]]
        continue
    elif order == 'R' :
        d_key += count
        robots[r-1] = [x, y, d_keys[d_key % 4]]
        continue
    way = direction[d_keys[d_key]]
    maps[y][x] = 0
    for j in range(count) :
        y += way[0]
        x += way[1]
        if x < 0 or x >= a or y < 0 or y >= b :
            print(f"Robot {r} crashes into the wall")
            break
        elif maps[y][x] != 0 :
            print(f"Robot {r} crashes into robot {maps[y][x]}")
            break
    else :
        maps[y][x] = r
        robots[r-1] = [x, y, d_keys[d_key]]
        continue
    
    break

else :
    print("OK")
