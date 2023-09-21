# 특정한 최단 경로 # 230913
# 1초, 256mb
# 1번 정점에서 N번 정점으로 이동
# 주어진 두 정점을 반드시 거치면서 최단 경로로 이동
# 갔던 곳 또 갈 수 있음
# 경로가 없으면 -1 출력 

# 그래프..
# 어떻게 탐색해야할까?
# 다익스트라! 최단거리 갱신? > bfs

from collections import deque

def dj(start, end):
    q = deque([start])
    # 언제 그만둬? 안돌아가도 되는지 어떻게 알아?
    # 다음 갈 곳보다 내꺼+거리 크기가 크면 안넣을래

    while q:
        # print(q)
        now = q.popleft()
        # print(now)
        for next in tree[now]:
            # print(next)
            child, weight = next
            # print(child, weight)
            tmp = weight + distance[now]
            if tmp < distance[child]:
                distance[child] = tmp
                if child != end:
                    q.append(child)


N, E = map(int, input().split())
tree = [[] for _ in range(N+1)] # [자식,가중치]를 해당 리스트에 넣어줄거임
# 방문했는지 표시 - 방문해야하는 노드 방문했는지 알아보려고
distance = [999_999_999_999] * (N+1)

# 그래프 저장
for i in range(E):
    a, b, c = map(int, input().split()) # a, b노드, c 가중치
    tree[a].append([b,c])
    tree[b].append([a,c])
# 반드시 방문해야하는 점
a, b = map(int, input().split())

# 1 - a - b- N
distance[1] = 0
dj(1, a)

tmp = distance[a]
distance = [999_999_999_999] * (N+1)
distance[a] = tmp
dj(a, b)

tmp = distance[b]
distance = [999_999_999_999] * (N+1)
distance[b] = tmp
dj(b, N)

min_v = (distance[N])

# 1 - b - a - N
distance = [999_999_999_999] * (N+1)
distance[1] = 0
dj(1, b)

tmp = distance[b]
distance = [999_999_999_999] * (N+1)
distance[b] = tmp
dj(b, a)

tmp = distance[a]
distance = [999_999_999_999] * (N+1)
distance[a] = tmp
dj(a, N)

if distance[N] < min_v:
    min_v = distance[N]

if min_v == 999_999_999_999:
    print(-1)
else:
    print(min_v)