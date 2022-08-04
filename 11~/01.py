import sys

'''
input example
5
2 3 1 2 2
'''
n = int(sys.stdin.readline())
fear = sorted([int(x) for x in sys.stdin.readline().split()])

ans = 0
count = 0
for idx in range(n):
    count += 1
    if fear[idx] <= count:
        ans += 1
        count = 0
print(ans)
