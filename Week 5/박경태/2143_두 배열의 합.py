import sys

input = sys.stdin.readline

t = int(input())
n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
b = [int(i) for i in input().split()]

a_sum = {}
for i in range(n) :
    temp_sum = a[i]
    if temp_sum not in a_sum :
        a_sum[temp_sum] = 1
    else :
        a_sum[temp_sum] += 1
    for j in range(i+1, n) :
        temp_sum += a[j]
        if temp_sum not in a_sum :
            a_sum[temp_sum] = 1
        else :
            a_sum[temp_sum] += 1
        
b_sum = {}
for i in range(m) :
    temp_sum = b[i]
    if temp_sum not in b_sum :
        b_sum[temp_sum] = 1
    else :
        b_sum[temp_sum] += 1
    for j in range(i+1, m) :
        temp_sum += b[j]
        if temp_sum not in b_sum :
            b_sum[temp_sum] = 1
        else :
            b_sum[temp_sum] += 1

answer = 0
for i in a_sum :
    if t-i in b_sum :
        answer += a_sum[i] * b_sum[t-i]

print(answer)