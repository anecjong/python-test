import sys

n, k = map(int, sys.stdin.readline().split())
A = sorted([int(x) for x in sys.stdin.readline().split()])
B = sorted([int(x) for x in sys.stdin.readline().split()], reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i] = B[i]
print(A)
print(sum(A))
