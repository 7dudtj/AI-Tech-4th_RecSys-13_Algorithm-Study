import sys
import heapq

N = int(sys.stdin.readline())
arr = [list(map(int, (sys.stdin.readline().split()))) for _ in range(N)]
arr.sort(key=lambda x: x[1])
curr = []

for price, date in arr:
    heapq.heappush(curr, price)
    if len(curr) > date:
        heapq.heappop(curr)

print(sum(curr))
