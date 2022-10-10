import string
import sys
w, h = map(int, input().split())
num_robots, num_move = map(int, input().split())
robots = [list(map(lambda x: int(x) if x in string.digits else x, sys.stdin.readline().split().rstrip("\n"))) for _ in range(num_robots)]
moves = [list(map(lambda x: int(x) if x in string.digits else x, sys.stdin.readline().split().rstrip("\n"))) for _ in range(num_move)]

directions = {"N":[0,-1], "W":[-1,0], "S":[0,1], "E":[1,0]}
positions = [[0 for _ in range(h)] for _ in range(w)]
for i, x in enumerate(robots):
    positions[x[0]-1][x[1]-1] = i+1
is_crash = False
for r, a, i in moves:
    for _ in range(i):
        if(a=="F"):
            positions[robots[r-1][0]-1][robots[r-1][1]-1] = 0
            robots[r-1][0] += directions[robots[r-1][2]][0]
            robots[r-1][1] += directions[robots[r-1][2]][1]
            if(robots[r-1][0] > w or robots[r-1][0]<1 or robots[r-1][1]> h or robots[r-1][1] < 1):
                print("Robot {} crashes into the wall".format(r))
                is_crash = True
                break
            elif(positions[robots[r-1][0]-1][robots[r-1][1]-1] != 0):
                print("Robot {} crashes into robot {}".format(r, positions[robots[r-1][0]-1][robots[r-1][1]-1]))
                is_crash = True
                break
            positions[robots[r-1][0]-1][robots[r-1][1]-1] = r
        elif(a=="L"):robots[r-1][2] = list(directions.keys())[list(directions.keys()).index(robots[r-1][2])+1 if robots[r-1][2] != "E" else 0]
        elif(a=="R"):robots[r-1][2] = list(directions.keys())[list(directions.keys()).index(robots[r-1][2])-1 if robots[r-1][2] != "N" else 3]
        
    if(is_crash):break
if(not is_crash): print("OK")
