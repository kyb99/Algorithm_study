# try2 다익스트라로 풀어보잔

import sys
sys.stdin = open('input.txt')

import heapq

# def dijk(n):
#     # 다익스트라..어케하더라?
#     # 현재 위치에서 갈 수 있는 최단거리 pop
#     # 그 다음위치로 옮겨가서 pop
#     # 마지막에 도착하면 끝내기?
#     now = n
#     visited[now] = 0
#     while True:
#         next_t, next = heapq.heappop(graph[now])
#         if next == N-1:
#             return visited[now] + next_t
#         # 방문 안한 곳
#         if visited[next] == -1:
#             visited[next] = visited[now] + next_t
#             now = next
#         if graph[now] == []:
#             break
    
#     return -1


def dijk(n):
    pass
    # 어떻게 하더라?
    # 못하겠다..까먹었다..복습해야겠다..



# 분기점 수 , 길의 수
N, M = map(int, input().split())
# 분기점
point = list(map(int, input().split()))
# 길 저장 - 그래프
graph = [[] for _ in range(N)]
visited = [-1]*N

# 시작, 끝, 시간
for _ in range(M):
    a, b, t = map(int, input().split())
    # 애초에 넣을때 못가는 곳은 안넣는다면?
    if a != N-1 and point[a] == 1:
        continue
    elif b != N-1 and point[b] == 1:
        continue
    graph[a].append((t, b))
    graph[b].append((t, a))

for p in graph:
    p = heapq.heapify(p)

print(graph)

dijk(0)

print(visited[N-1])