import sys

n = int(sys.stdin.readline())
arr_ = [[] for _ in range(n)]
for idx in range(n):
    arr_[idx] = sys.stdin.readline().split()
    arr_[idx][1] = int(arr_[idx][1])
arr_.sort(key=lambda x: x[1])
for idx in range(n):
    print(arr_[idx][0], end=' ')
