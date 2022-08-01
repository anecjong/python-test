import sys

n = int(sys.stdin.readline())
repo = [int(x) for x in sys.stdin.readline().split()]

dp = [0] * n
dp[0] = repo[0]
for idx in range(1, n):
    dp[idx] = max(dp[idx-1], dp[idx-2] + repo[idx])
print(dp[-1])
