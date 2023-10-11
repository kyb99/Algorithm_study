# LCA # 231011
# N개의 정점으로 이루어진 트리
# 정점: 1~N번, 루트=1번
# 두 노드의 가장 가까운 공통조상 출력
# 어렵군.. 다른방식으로 접근해보자

from collections import deque

def find(a, b):
    ans = 1
    return ans

# # 돌면서 조상을 메모하기? 노드수가 많으니까?
# def DFS():
#     visited = [0]*(N+1)
#     stack = [1]
#     while stack:
#         now = stack.pop()
#         visited[now] = 1
#         print(now, end=' ')
#         for node in tree[now]:
#             if visited[node] == 0:
#                 stack.append(node)

def BFS():
    q = deque()
    q.append((1, 1))
    visited = [0]*(N+1)
    depth = [[] for _ in range(N+1)]
    depth[1].append(1)
    visited[1] = 1
    while q:
        now, lv = q.popleft()
        for node in tree[now]:
            if visited[node]==0:
                visited[node] = lv+1
                depth[lv+1].append(node)
    # print(visited)
    # print(depth)
    return visited, depth

N = int(input())
tree = [[] for _ in range(N+1)]

# 트리 입력받기
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
# print(tree)

# DFS()
visited, depth = BFS()

# 알고싶은 쌍
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    # 조상찾기
    # print(find(a,b))