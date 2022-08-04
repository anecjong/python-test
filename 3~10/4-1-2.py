import sys

n = int(sys.stdin.readline())

if n < 3:
    print((n+1)*15*105)
elif n < 13:
    print((n)*15*105 + 3600)
elif n < 23:
    print((n-1)*15*105 + 3600*2)
else:
    print((n-2)*15*105 + 3600*3)
