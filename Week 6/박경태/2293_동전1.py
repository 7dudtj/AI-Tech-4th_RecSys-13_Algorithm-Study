n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
counts = [0 for _ in range(k+1)]
counts[0] = 1
for coin in coins :
    for i in range(coin, k+1) :
        counts[i] += counts[i-coin]
print(counts[-1])