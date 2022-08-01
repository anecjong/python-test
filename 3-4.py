import sys

n, k = map(int, sys.stdin.readline().split())
ans = 0
while n >= k:
    while n % k != 0:
        n -= 1
        ans += 1
    n //= k
    ans += 1

print(ans + (n-1))
