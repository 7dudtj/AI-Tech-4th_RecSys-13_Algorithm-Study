import sys

N,M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

if M == 1:
  print(arr[-1] - arr[0])
else:
  split_points = [(v-arr[i-1], i) for i,v in enumerate(arr[1:],1)]  
  split_points.sort(reverse=True)
  split_at = [split_points[j][1] for j in range(M-1)]
  split_at.sort()

  start = 0
  ans = arr[-1] - arr[split_at[-1]]
  
  for n in split_at:
    ans += arr[n-1] - arr[start]
    start = n
  
  print(ans)
