import sys

n, m = map(int, sys.stdin.readline().split())
ans = 0
for idx in range(n):
    ans = max(ans, min(list(map(int, sys.stdin.readline().split()))))
print(ans)
