import sys
import heapq

N = int(sys.stdin.readline())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort()
q = []

for dl, ramen in arr:
    if len(q) < dl:
        heapq.heappush(q, ramen)
    else:
        heapq.heappushpop(q, ramen)

print(sum(q))
