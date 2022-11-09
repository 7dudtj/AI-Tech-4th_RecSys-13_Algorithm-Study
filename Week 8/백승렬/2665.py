import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited[0][0] = 1

dir = [(1,0),(-1,0),(0,1),(0,-1)]

q = [(0,0,0)]

while q:
    num_room, x, y = heappop(q)
    
    if x==(N-1) and y==(N-1):
        print(num_room)
        break

    for dx, dy in dir:
        a = x+dx; b = y+dy
        if 0<=a<N and 0<=b<N and not visited[a][b]:
            if board[a][b] == '1':
                heappush(q, (num_room, a, b))
            else:
                heappush(q, (num_room+1, a, b))
            visited[a][b] = 1
            
