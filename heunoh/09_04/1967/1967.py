# 응애 ㅠ
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
graph = [[] for _ in range(N+1)]


def dfs(start, weight):
    for i in graph[start]:
        a, b = i
        if distance[a] == -1:
            distance[a] = weight + b
            dfs(a, weight + b)


for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

distance = [-1] * (N+1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (N+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))