# 산책(small) # 231004 # 틀림! 고쳐보자!
# S에서 출발 > E 찍고 > S 다시 돌아오기
# 이미 갔던 정점 안가
# 가장 짧은 거리 선택, 같은 거리라면 사전순으로 먼저 오는것 선택
# 전체 경로 거리 구하기

import sys
sys.setrecursionlimit(10000)

from collections import deque


# bfs하면 작은 순서대로
# def bfs(s, e):
#     q = deque()
#     q.append(s, 0)
#     while q:
#         now, cnt = q.popleft()
#         for child in tree[now]:
#             visited[child] = cnt+1
#             q.append((child, cnt+1))

# 경로를 저장해야하지 않을까?
# def dfs(s, e):
#     stack = [(s,1)]
#     visited[s] = 1
#     path = [s]
#     while stack:
#         now, cnt = stack.pop()
#         for child in tree[now]:
#             if child == e:
#                 return cnt+1
#             if not visited[child] or visited[child]>cnt+1:
#                 visited[child] = cnt+1
#                 stack.append((child, cnt+1))


def dfs(now, e, arr):
    global path, ans
    print(now, arr, visited)
    if now == e:
        if ans==0 or visited[now] <= ans:
            if path==[] or arr < path:
                path = arr[:]
            ans = visited[now]
        return

    cnt = visited[now]
    for child in tree[now]:
        if not visited[child] or visited[child]>cnt+1:
            visited[child] = cnt+1
            dfs(child, e, arr+[child])

N, M = map(int, input().split())
# 1~N
tree = [[] for _ in range(N+1)]
visited = [0]*(N+1)
path = []
ans = 0

for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
S, E = map(int, input().split())

# 우선순위큐로 넣어도 될듯..?
# 작은순서대로 bfs탐색하면 됨
for i in range(1, N+1):
    tree[i].sort()

print(tree)


dfs(S, E, [S])

print(ans, path)