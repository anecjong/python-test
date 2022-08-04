import sys
import heapq

'''
input example
3 2 1
1 2 4
1 3 2
'''

INF = int(1e9)
n, m, c = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distances = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((z, y))


def dijkstra(start):
    q = []
    q.append((0, start))
    distances[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distances[now]:
            continue
        else:
            for i in graph[now]:
                cost = dist + i[0]
                if cost < distances[i[1]]:
                    distances[i[1]] = cost
                    heapq.heappush(q, (cost, i[1]))


dijkstra(c)
fine_list = [x for x in distances if x != INF and x != 0]
print(len(fine_list), max(fine_list))
