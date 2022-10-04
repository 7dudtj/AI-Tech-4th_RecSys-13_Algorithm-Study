import sys
from collections import deque

A,B = map(int, sys.stdin.readline().split())
N,M = map(int, sys.stdin.readline().split())

graph = [[0]*A for _ in range(B)]

robot_coord = [(-1,-1)]
robot_dir = ['empty']

for i in range(1,N+1):
    a,b,d  = sys.stdin.readline().split()
    a,b = int(a)-1, B-int(b)
    graph[b][a] = i
    robot_dir.append(d)
    robot_coord.append((b,a))


def forward(a,b,c):
    dir = {'N':[-1,0],'E':[0,1],'S':[1,0],'W':[0,-1]}
    robot_num = graph[b][a]
    y, x = dir[robot_dir[robot_num]]
    graph[b][a] = 0
    for _ in range(c):
        b += y; a+= x
        if not 0<=a<A or not 0<=b<B:
            return f"Robot {robot_num} crashes into the wall"
        if graph[b][a]:
            return f"Robot {robot_num} crashes into robot {graph[b][a]}"
    graph[b][a] = robot_num
    robot_coord[robot_num] = (b,a)
    return None 


def rotate(a,b,c):
    q = deque(['N','E','S','W'])
    while q[0] != robot_dir[graph[b][a]]:
        q.rotate(-1)
    q.rotate(c % 4)
    return q[0]

def op(M):
    for _ in range(M):
        r,o,c = sys.stdin.readline().split()
        r, c = int(r), int(c)
        b,a = robot_coord[r]

        if o == 'F':
            message = forward(a,b,c)
            if message:
                return message
            
        elif o == 'L':
            robot_dir[r] = rotate(a,b,c)
           
        else:
            robot_dir[r] = rotate(a,b,-c)
            
    return 'OK'

print(op(M))
