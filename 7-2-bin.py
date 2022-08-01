import sys

n = int(sys.stdin.readline())
item_ = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
req_ = list(map(int, sys.stdin.readline().split()))


def bin_search(r, item_):
    lo, hi = 0, n-1
    while lo <= hi:
        mid = (lo+hi)//2
        if item_[mid] == r:
            return True
            break
        if item_[mid] > r:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


ans = []
for r in req_:
    if bin_search(r, item_):
        ans.append("yes")
    else:
        ans.append("no")
print(*ans)
