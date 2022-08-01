import sys

n, m = map(int, sys.stdin.readline().split())
rice_cakes = sorted([int(x) for x in sys.stdin.readline().split()])

lo, hi = 0, rice_cakes[-1]
ans = None
while lo <= hi:
    mid = (lo + hi) // 2
    remain_ = 0
    for idx in range(n):
        remain_ += max(0, rice_cakes[idx] - mid)
    if remain_ >= m:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)
