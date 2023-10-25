# try3 다익스트라로 풀어보잔
# 231019 다시 도전! > 시간초과

import sys
sys.stdin = open('input.txt')

import heapq


def dijk(n):
    # 해보자!
    # 현재 위치에서 갈 수 있는 가장 짧은 경로 찾기
    # 다음 갈 곳 + 거리 꺼내는데, 못가면/더 길면 넘어가
    pq = []
    heapq.heappush(pq, (0, n))
    distance[n] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        # 이미 저장되어있는게 더 짧으면 넘어가
        if distance[now] < dist:
            continue
        for cost, next in graph[now]:
            if next != N-1 and point[next] == 1:
                continue
            new_cost = dist + cost
            if distance[next] <= new_cost:
                continue
            distance[next] = new_cost
            heapq.heappush(pq, (new_cost, next))


# 분기점 수 , 길의 수
N, M = map(int, input().split())
# 분기점
point = list(map(int, input().split()))
# 길 저장 - 그래프
graph = [[] for _ in range(N)]

INF = 10e9
# 거리가 짧으면 저장, 길면 그냥 넘어갈거라서
distance = [INF]*N

# 시작, 끝, 시간
for _ in range(M):
    a, b, t = map(int, input().split())

    graph[a].append((t, b))
    graph[b].append((t, a))

# for p in graph:
#     p = heapq.heapify(p)

# print(graph)

dijk(0)

if distance[N-1] == INF:
    print(-1)
else:
    print(distance[N-1])