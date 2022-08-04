import sys

lookdir = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
n, m = map(int, sys.stdin.readline().split())
x_, y_, lookat = map(int, sys.stdin.readline(). split())
map_ = [[] for _ in range(n)]
for idx in range(n):
    map_[idx] = list(map(int, sys.stdin.readline().split()))
map_[x_][y_] = 3

rot_idx = 0
ans = 1
while True:
    lookat = (lookat + 1) if lookat != 3 else 0
    x_new, y_new = x_ + lookdir[lookat][0], y_ + lookdir[lookat][1]
    if map_[x_new][y_new] == 0:
        x_, y_ = x_new, y_new
        map_[x_][y_] = 3
        rot_idx = 0
        ans += 1
    elif rot_idx == 4:
        x_new, y_new = x_ - lookdir[lookat][0], y_ - lookdir[lookat][1]
        if map_[x_new][y_new] == 1:
            break
        else:
            x_, y_ = x_new, y_new
            rot_idx = 0
    else:
        rot_idx += 1
print(ans)
