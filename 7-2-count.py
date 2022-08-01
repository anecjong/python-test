import sys

n = int(sys.stdin.readline())
item_ = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
req_ = list(map(int, sys.stdin.readline().split()))

max_item_ = max(item_)
count_item_ = [0] * (max_item_ + 1)
for i in item_:
    count_item_[i] += 1

ans = []
for r in req_:
    if count_item_[r] != 0:
        ans.append("yes")
    else:
        ans.append("no")
print(*ans)
