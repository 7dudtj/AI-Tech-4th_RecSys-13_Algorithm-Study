import sys
import heapq

n = int(input())
data = []
for i in range(n) :
    time, cup = list(map(int, sys.stdin.readline().rstrip().split()))
    data.append([time, cup])
data.sort()

q = []
for time, cup in data :
    heapq.heappush(q, cup)
    if len(q) > time :
        heapq.heappop(q)

print(sum(q))
