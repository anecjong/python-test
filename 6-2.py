import sys

n = int(sys.stdin.readline())
arr_ = [0] * n
for idx in range(n):
    arr_[idx] = int(sys.stdin.readline())

arr_.sort(key=lambda x: -x)
print(*arr_)
