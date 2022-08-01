import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph_ = [[] for _ in range(n)]
for idx in range(n):
    graph_[idx] = list(map(int, sys.stdin.readline().rstrip()))

deq = deque([[0, 0]])
mov_dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while deq:
    x_, y_ = deq.popleft()
    for mov in mov_dir:
        x_new = x_ + mov[0]
        y_new = y_ + mov[1]
        if 0 <= x_new < n and 0 <= y_new < m:
            if x_new == 0 and y_new == 0:
                pass
            elif graph_[x_new][y_new] == 1:
                deq.append([x_new, y_new])
                graph_[x_new][y_new] = graph_[x_][y_] + 1
    if graph_[n-1][m-1] != 1:
        break
print(graph_)
print(graph_[-1][-1])
