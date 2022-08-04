import sys

x = int(sys.stdin.readline())

dp = [0] * (x + 1)
for idx in range(2, x+1):
    dp[idx] = dp[idx-1] + 1
    if idx % 2 == 0:
        dp[idx] = min(dp[idx], dp[idx//2] + 1)
    if idx % 3 == 0:
        dp[idx] = min(dp[idx], dp[idx//3] + 1)
    if idx % 5 == 0:
        dp[idx] = min(dp[idx], dp[idx//5] + 1)
print(dp[x])
