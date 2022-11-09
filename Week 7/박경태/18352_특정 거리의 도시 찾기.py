import sys
import heapq
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
cities = {i:[] for i in range(1, n+1)}
for i in range(m) :
    s, e = map(int,input().split())
    cities[s].append(e)

city = x
visited = {i:300000 for i in range(1, n+1)}
visited_city = {city:0}
visited[city] = 0
q = []
while True :
    for c in cities[city] :
        heapq.heappush(q, (visited[city]+1, c))
    cities[city] = []
    while len(q) >= 1 and city in visited_city :
        dis, city = heapq.heappop(q)

    if dis > k :
        break

    visited[city] = min(visited[city], dis)
    visited_city[city] = dis
    if len(q) == 0 and len(cities[city]) == 0 :
        break

c_list = []
for key, value in visited.items() :
    if value == k :
        c_list.append(key)
if len(c_list) == 0 :
    print(-1)
else :
    for c in sorted(c_list) :
        print(c)