import sys

n, m = map(int, sys.stdin.readline().split())
coins = [0] * n
for idx in range(len(coins)):
    coins[idx] = int(sys.stdin.readline())

dp = [float('inf')] * (m+1)
dp[0] = 0
for idx in range(min(coins), m+1):
    for coin in coins:
        if idx - coin >= 0:
            dp[idx] = min(dp[idx], dp[idx - coin] + 1)
if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])
