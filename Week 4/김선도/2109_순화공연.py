n = int(input())
pay_list = [list(map(int, input().split())) for _ in range(n)]
pay_list = sorted(pay_list, key=lambda x:x[1])

import heapq
cal = []
for pay in pay_list:
    heapq.heappush(cal, pay[0])
    if(len(cal)>pay[1]):
        heapq.heappop(cal)
print(sum(cal))
