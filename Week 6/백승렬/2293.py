import sys
N,K = map(int, sys.stdin.readline().split())

C = []
for _ in range(N):
  x = int(sys.stdin.readline())
  if x <= K:
    C.append(x)
C.sort(reverse=True)
dp = [0]*(K+1)
dp[0] = 1
for v in C:
  for j in range(v, K+1):
    dp[j] += dp[j-v]

print(dp[K])
