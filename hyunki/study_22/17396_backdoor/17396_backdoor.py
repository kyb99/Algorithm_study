import heapq
import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline
INF = sys.maxsize   # 처음에 int(1e9)를 썻지만 이 값보다 큰 값이 나올수 있으므로 sys.maxsize 를 사용한다.

# 시야를 피해 넥서스 까지 백도를 갈 수 있는 최소 시간
# 넥서스에 가지 못하면 -1 출력
# 넥서스에 도착하면 최소시간 출력

N, M = map(int, input().split())    # N:분기점 수, M:분기점을 잇는 길의 수
ward = list(map(int, input().split()))  # ward: 분기점에 시야 있는지 확인(0:시야없음, 1:시야있음), 마지막은 넥서스(무조건 1)
ward[-1] = 0

# a: 출발, b:도착, t:시간
graph = [[] for _ in range(N)]

# 양방향으로 입력 받기
for i in range(M):
    a, b, t = map(int, input().split())
    graph[a].append([b, t])
    graph[b].append([a, t])

visited = [INF] * N


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if visited[node] < dist:
            continue

        for next_node, next_cost in graph[node]:
            # 다음 방문 장소가 지금 까지의 거리를 더한 값보다 크거나 와드가 있으면 지나갈 수 없다
            if visited[next_node] > visited[node] + next_cost and not ward[next_node]:
                visited[next_node] = visited[node] + next_cost
                heapq.heappush(q, (visited[next_node], next_node))


# 다익스트라 가동
dijkstra(0)
# visited = [0, 6, 2, 4, 5]

# 넥서스 빼고 나머지 더해서 출력
result = visited[(N - 1)]

if result == INF:
    print("-1")
else:
    print(result)
