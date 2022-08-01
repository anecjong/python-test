import sys

x = int(sys.stdin.readline())

if x <= 3:
    print(1)
elif x == 4:
    print(2)
elif x == 5:
    print(1)
else:
    dp = [0] * (x + 1)
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 1
    for idx in range(6, x+1):
        dp[idx] = dp[idx-1] + 1
        if idx % 2 == 0:
            dp[idx] = min(dp[idx], dp[idx//2] + 1)
        if idx % 3 == 0:
            dp[idx] = min(dp[idx], dp[idx//3] + 1)
        if idx % 5 == 0:
            dp[idx] = min(dp[idx], dp[idx//5] + 1)
print(dp[x])
