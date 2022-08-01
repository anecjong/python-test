import sys

n = int(sys.stdin.readline())
order_list = sys.stdin.readline().split()

x, y = 1, 1
dict_ = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
for order in order_list:
    x += dict_[order][0]
    y += dict_[order][1]
    if x > n:
        x = n
    elif y > n:
        y = n
    elif x < 1:
        x = 1
    elif y < 1:
        y = 1
print(x, y)
