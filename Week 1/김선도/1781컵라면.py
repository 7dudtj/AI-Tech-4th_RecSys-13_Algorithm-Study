import heapq
import sys

num_problems = int(sys.stdin.readline().rstrip("\n"))
problems_list = []
for i in range(int(num_problems)):
    problems_list.append(list(map(int, sys.stdin.readline().rstrip("\n").split())))
problems_list.sort()
solve_heapq = []
for problem in problems_list:
    if problem[0]>len(solve_heapq): heapq.heappush(solve_heapq, problem[1])
    else : heapq.heappushpop(solve_heapq, problem[1])
print(sum(solve_heapq))
