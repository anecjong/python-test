import sys

n = int(sys.stdin.readline())
dp = [0] * (n+1)
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    dp[1] = 1
    dp[2] = 3
    for idx in range(3, n+1):
        dp[idx] = dp[idx-1] + 2 * dp[idx-2]
    print(dp[-1] % 796796)
