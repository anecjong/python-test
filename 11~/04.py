import sys

'''
input example
5
3 2 1 1 9
'''
n = int(sys.stdin.readline())
coins = sorted([int(x) for x in sys.stdin.readline().rstrip()])

target = 1
for coin in coins:
    if target < coin:
        break
    target += coin
print(target)
