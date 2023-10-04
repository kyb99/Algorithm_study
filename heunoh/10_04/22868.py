# 정점의 개수 N 두 정점 사이를 잇는 도로의 개수 M
# 방문처리를 어떻게 해야하는가..
# 時發男娥

from collections import deque
def search(start, end):
    dq = deque()
    dq.append((start,[start]))
    visited[start] = True
    while dq:
        current, path = dq.popleft()
        if current == end:
            return path
        for next in graph[current]:
            if visited[next]:
                continue
            visited[next] = True
            dq.append((next, path + [next]))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
res = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

S, E = map(int,input().split())

go = search(S,E)

visited = [0] *(N+1)

for i in go:
    if i == E or i == S:
        continue
    visited[i] = True
back = search(E,S)
#print(go)
#print(back)
print(len(go) + len(back) - 2)