import bisect
t = int(input())
n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
b_list = list(map(int, input().split()))

answer = 0
sub_a = []
for i in range(n):
    for j in range(i, n):
        sub_a.append(sum(a_list[i:j+1]))
sub_b = []
for i in range(m):
    for j in range(i, m):
        sub_b.append(sum(b_list[i:j+1]))
        
sub_a.sort()
sub_b.sort()

for i in sub_a:
    l = bisect.bisect_left(sub_b,t-i)
    r = bisect.bisect_right(sub_b,t-i)
    answer+=r-l

print(answer)
