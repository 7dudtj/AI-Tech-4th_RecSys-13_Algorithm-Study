import heapq

count = int(input())
data = []
for i in range(count) :
    m, d = map(int, input().split())
    data.append([d, m])
data.sort()

q = []
for d, m in data :
    heapq.heappush(q, m)
    if len(q) > d :
        heapq.heappop(q)
print(sum(q))
