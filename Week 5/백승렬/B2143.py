def first_occ(arr, target):
    lo = 0; hi = len(arr) - 1; ans = -1
    while lo <= hi:
        mid = lo + (hi - lo)//2
        if arr[mid] == target:
            ans = mid
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

def last_occ(arr, target):
    lo = 0; hi = len(arr) - 1; ans = -1
    while lo <= hi:
        mid = lo + (hi - lo)//2
        if arr[mid] == target:
            ans = mid
            lo = mid + 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

import sys
T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A_boo = A[:]
B_boo = B[:]

for i in range(n):
    num = A[i]
    for j in range(i+1,n):
        num += A[j]
        A_boo.append(num)

for i in range(m):
    num = B[i]
    for j in range(i+1,m):
        num += B[j]
        B_boo.append(num)

B_boo.sort()

count = 0
for a in A_boo:
    first = first_occ(B_boo, T-a)
    if first != -1:
        last = last_occ(B_boo, T-a)
        count += (last - first + 1)

print(count)
