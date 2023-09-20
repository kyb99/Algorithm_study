# 트리의 지름
# 트리에 존재하는 모든 경로들 중 가장 긴것의 길이
# 루트가 있는 트리를 가중치가 있는 간선들로 줌
# 최대값 출력
# 루트는 1

# 해인언니가 말해준대로
# 답은 나오는데, recursion error 발생
def dfs(now, cnt):
    global max_v
    global max_idx

    visited[now] = 1

    if cnt > max_v:
            max_v = cnt
            max_idx = now

    for ch, w in tree[now]:
        if visited[ch] == 0:
            dfs(ch, cnt+w)
    return


N = int(input()) # 노드 개수
tree = [[] for _ in range(N+1)] # [자식, 가중치] 넣을 리스트
visited = [0] * (N+1)
max_v = 0
max_idx = 0
value = []
for _ in range(N-1):
    par, *child = map(int, input().split())
    tree[par].append(child)
    tree[child[0]].append([par, child[1]])
# print(tree)
dfs(1, 0)
# max_v = 0
visited = [0] * (N+1)
dfs(max_idx, 0)
print(max_v)



# 끝에서부터 dp로 올라가도 될듯?
# 부모 값은 자식들을 합친거
# 최대값..

# 쭉 올라가면서 노드에 가중치 저장
# 다음 리프에서 올라가면서, 
# 자식이 두개면 더하기, 자식이 한개면 비교해서 큰값 저장
# def dp(now):
#     if now == 1: # root
#         return
#     else:
#         print('before',now, visited)
#         for par, w in parent[now]:
#             w = w+visited[now]
#             if num_child[par] == 2:
#                 visited[par] += w
#             else:
#                 if visited[par] < w:
#                     visited[par] = w
#             print('after', par, visited)
#             dp(par)


# N = int(input()) # 노드 개수
# parent = [[] for _ in range(N+1)] # [자식, 가중치] 넣을 리스트
# visited = [0] * (N+1)
# num_child = [0] * (N+1)
# max_v = 0
# for _ in range(N-1):
#     par, child, weight = map(int, input().split())
#     parent[child].append([par, weight])
#     num_child[par] += 1
# print(parent)
# print(num_child)
# for i in range(1, N+1):
#     if num_child[i] == 0:
#         dp(i)

# print(visited)



# 일단은 정석대로 해보자 > 이렇게 하면 루트에서부터 제일 가중치 큰게 나옴
# def dfs(now, cnt):
#     global max_v
#     visited[now] = 1

#     if not tree[now]:
#         if cnt > max_v:
#             max_v = cnt
#         return
#     else:
#         for ch, w in tree[now]:
#             if visited[ch] == 0:
#                 dfs(ch, cnt+w)
#     return


# N = int(input()) # 노드 개수
# tree = [[] for _ in range(N+1)] # [자식, 가중치] 넣을 리스트
# visited = [0] * (N+1)
# max_v = 0
# value = []
# for _ in range(N-1):
#     par, *child = map(int, input().split())
#     tree[par].append(child)
# print(tree)
# dfs(1, 0)

# print(max_v)