import sys
'''
input example
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
'''

n, m = map(int, sys.stdin.readline().split())
balls = list(map(int, sys.stdin.readline().split()))
count_table = [0] * 11

for ball in balls:
    count_table[ball] += 1

total = n
ans = 0
for val in count_table:
    total -= val
    ans += total * val
print(ans)
