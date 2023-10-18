# BOJ 17396 백도어
import heapq
import sys
input = sys.stdin.readline
# 분기점의 수와 분기점을 잇는 길의 수
# 가중치 양의 가중치만 존재하는 그래프 탐색에서의 최소비용 탐색 문제는
# 다익스트라 알고리즘을 사용하여 해결
def dijkstra(start):
    pq = []
    heapq.heappush(pq,(0, start))
    distance[start] = 0
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next_node, next_cost in graph[now]:
            if (distance[next_node] > dist + next_cost) and not node[next_node]:
                distance[next_node] = distance[now] + next_cost
                heapq.heappush(pq, (distance[next_node], next_node))

N, M = map(int, input().split())
INF = sys.maxsize
node = list(map(int, input().split()))
graph = [[] for _ in range(N)]
distance = [INF] * N
node[-1] = 0

for _ in range(M):
    start, end, acc = map(int ,input().split())
    graph[start].append((end, acc))
    graph[end].append((start, acc))


dijkstra(0)
if distance[N-1] == INF:
    print(-1)
else:
    print(distance[N-1])
