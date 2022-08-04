import sys
from collections import deque
from itertools import product

n, m = map(int, sys.stdin.readline().split())
graph_ = [[] for _ in range(n)]
for idx in range(n):
    graph_[idx] = [int(x) for x in sys.stdin.readline().rstrip()]

adj_idx = [[-1, 0], [1, 0], [0, 1], [0, -1]]

ans = 0
for i, j in product(range(n), range(m)):
    if graph_[i][j] == 0:
        deq = deque([(i, j)])
        graph_[i][j] = ans+2
        while deq:
            v = deq.popleft()
            for dir in adj_idx:
                i_new = v[0] + dir[0]
                j_new = v[1] + dir[1]
                if 0 <= i_new < n and 0 <= j_new < m:
                    if graph_[i_new][j_new] == 0:
                        deq.append((i_new, j_new))
                        graph_[i_new][j_new] = ans+2
        ans += 1
print(graph_)
print(ans)
