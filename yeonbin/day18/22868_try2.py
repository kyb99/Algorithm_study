# 산책(small) # 231004 # pass
# S에서 출발 > E 찍고 > S 다시 돌아오기
# 이미 갔던 정점 안가
# 가장 짧은 거리 선택, 같은 거리라면 사전순으로 먼저 오는것 선택
# 전체 경로 거리 구하기

# import sys
# sys.setrecursionlimit(10000)

from collections import deque


# bfs하면 작은 순서대로
# 경로를 저장해야하지 않을까?
def bfs(s, e):
    q = deque()
    q.append((s, 0, [s]))
    visited[s] = 1
    path = []
    while q:
        now, cnt, arr = q.popleft()
        for child in tree[now]:
            # 1)
            # if not visited[child] or visited[child] > cnt+1:
            # 먼저 적어놓은게 숫자가 작음
            if not visited[child]:
                visited[child] = cnt+1
                if child == e:
                    path = arr[:]
                    # 1) 이렇게하니까 틀렸음!
                    # continue # for child
                    # 이게 제일 빠른거니까 리턴 바로 해도됨
                    return path
                else:
                    q.append((child, cnt+1, arr+[child]))
    return path

# def bfs2(s, e):
#     q = deque()
#     q.append((s, 0, [s]))
#     visited[s] = 1
#     path = []
#     while q:
#         now, cnt, arr = q.popleft()
#         for child in tree[now]:
#             if child in path:
#                 continue
#             if not visited[child] or visited[child] > cnt+1:
#                 visited[child] = cnt+1
#                 if child == e:
#                     path = arr[:]
#                     continue # for child
#                 else:
#                     q.append((child, cnt+1, arr+[child]))
#     return path

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

# print(tree)

# 출발지 > 도착지
path = bfs(S, E)
ans = visited[E]
# print(ans, path, visited)

# 선택한 곳 빼고 초기화
for i in range(1, N+1):
    if i==S or i not in path:
        visited[i] = 0
# print(visited)

# 도착지 > 출발지
path = bfs(E, S)

# print(ans+visited[S], path, visited)
print(ans+visited[S])