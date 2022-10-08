import sys
import heapq

R, C = map(int, sys.stdin.readline().split())

graph = [sys.stdin.readline() for _ in range(R)]

water = []

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            start = (i,j)
        elif graph[i][j] == 'D':
            end = (i,j)
        elif graph[i][j] == '*':
            water.append((i,j))

dir = [(-1,0),(1,0),(0,-1),(0,1)]
visited = [[R*C]*C for _ in range(R)]

if water:
    w_q = []
    for i,j in water:
        w_q.append((0,i,j))
        visited[i][j] = 0

    heapq.heapify(w_q)
    while w_q:
        c, na, nb = heapq.heappop(w_q)
        for a,b in dir:
            x = na + a; y = nb + b
            if 0<=x<R and 0<=y<C and visited[x][y] == R*C:
                if graph[x][y] == '.':
                    visited[x][y] = c+1
                    heapq.heappush(w_q,(c+1,x,y))     

visited[start[0]][start[1]] = -1

d_q = [(0,*start)]
ans = 0

while d_q:
    c, na, nb= heapq.heappop(d_q)
    if graph[na][nb] == 'D':
        ans = c
        break
    for a,b in dir:
        x = na + a; y = nb + b
        if 0<=x<R and 0<=y<C and visited[x][y] != -1 and visited[x][y] > c+1:
            if graph[x][y] == '.' or graph[x][y] == 'D':
                visited[x][y] = -1
                heapq.heappush(d_q,(c+1,x,y))
                
print(ans if ans else 'KAKTUS')
