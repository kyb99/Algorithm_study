# 백도어 # 231018
# N개의 분기점에 위치가능, 0번째가 현재, N-1번째가 상대편
# 적챔피언, 적와드...등 상대의 시야에 걸리는 곳은 지나칠 수 없음
# 지나칠 수 있는지 여부와 각 분기점에서 다른 분기점으로 가는데 걸리는 시간이 주어짐
# 최소 시간을 구하라

# 0이면 안보인다, 1이면 보인다, N-1번째는 1이지만 갈 수있다
# 연결은 양방향, 간선은 최대 1개
# 갈 수없으면 -1 출력

# (1 ≤ N ≤ 100,000, 1 ≤ M ≤ 300,000)

# BFS쓰면 되지 않을까? > 시간초과 나려나? > 시간초과
# 아니면 다익스트라?

import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(n):
    q = deque()
    visited[n] = 1
    q.append((n, 0)) # 뭘 넣지?
    while q:
        now, acc = q.pop()
        for next, next_t in graph[now]:
            # 도착점
            if next == N-1:
                if visited[next] == -1 or acc+next_t < visited[next]:
                    visited[next] = acc + next_t
            elif point[next] == 1:
                continue
            # 처음가거나, 갈 수 있는 거리가 더 짧은 경우
            if visited[next]==-1 or (acc+next_t) < visited[next]:
                visited[next] = acc + next_t
                q.append((next, acc+next_t))



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
    # 애초에 넣을때 못가는 곳은 안넣는다면? 그래도 시간초과일세
    # if a != N-1 and point[a] == 1:
    #     continue
    # elif b != N-1 and point[b] == 1:
    #     continue
    graph[a].append((b, t))
    graph[b].append((a, t))

BFS(0)

print(visited[N-1])


