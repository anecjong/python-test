import sys

'''
input example
02984

567
'''
input_ = [int(x) for x in sys.stdin.readline().rstrip()]
ans = 0
for x in input_:
    if ans == 0 or x == 0:
        ans += x
    else:
        ans *= x
print(ans)
