import sys

n, m, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

max1 = max(nums)
nums.remove(max1)
max2 = max(nums)

print(m//(k+1) * (k*max1 + max2) + m % (k+1) * max1)
