# 벽 부수고 이동하기
# N*M 행렬, 0은 이동할 수 있는곳
# 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면,
# 벽을 한 개 까지 부수고 이동하여도 된다.
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸
#  N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)

# 최단경로니까 BFS, 벽 한개 부수는거 표시 해줘야함
# bfs하면서, 벽을 안부쉈다면 부수는 경우도 넣어주기
# 벽 한번 부쉈는데 못가면 리턴, 반환 -1
# dfs가 낫지않을까?

from collections import deque

from copy import deepcopy

def bfs(is_break, v): # 이거 싹 지우고 다시 풀어봐라
    while q:
        i, j, cnt = q.popleft()
        cnt += 1
        print(v)
        for k in range(3):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:
                print(ni, nj)
                if i==N-1 and j == M-1:
                    answer.append(cnt)
                    return
                if v[ni][nj] == -1:
                    if arr[ni][nj] == 0:
                        v[ni][nj] = cnt
                        q.append((ni, nj, cnt))
                        print('aa')
                        bfs(is_break, deepcopy(v))
                elif v[ni][nj] > cnt: # 이러면 안되네...어렵다..
                    if arr[ni][nj] == 0:
                        q.append((ni, nj, cnt))
                        v[ni][nj] = cnt
                        print('bb')
                        bfs(is_break, deepcopy(v))
                elif is_break == False:
                    q.append((ni, nj, cnt))
                    print('cc')
                    bfs(True, deepcopy(v))
            print('ff')

# 이건 딥카피 안해서 틀림, 시간초과인지는 안해봄
# def dfs(cnt, is_break):
#     if not stack:
#         return
#     else:
#         i, j = stack.pop()
#         visited[i][j] = cnt
#         if i==N-1 and j == M-1:
#             answer.append(cnt)
#             return
#         # print(i, j, cnt)
#         for k in range(3):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0<=ni<N and 0<=nj<M and visited[ni][nj] == -1:
#                 if arr[ni][nj] == 0:
#                     stack.append((ni, nj))
#                     dfs(cnt+1, is_break)
#                 elif is_break == False:
#                     stack.append((ni, nj))
#                     dfs(cnt+1, True)

# 시간초과 > 이건 아닌듯..?
def dfs(cnt, is_break, v):
    global max_v
    while stack:
        i, j = stack.pop()
        v[i][j] = cnt
        
        # print(i, j, cnt)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if i==N-1 and j == M-1:
            # answer.append(cnt)
                if cnt < max_v:
                    max_v = cnt
                return
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == -1:
                if arr[ni][nj] == 0:
                    stack.append((ni, nj))
                    dfs(cnt+1, is_break, deepcopy(v))
                elif is_break == False:
                    stack.append((ni, nj))
                    dfs(cnt+1, True, deepcopy(v))

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
is_break = False
cnt = 1
# delta D L R
di = [1, 0, 0, -1]
dj = [0, -1, 1, 0]

answer = []
stack = deque([(0, 0)])
visited[0][0] = 1
max_v = 1_000_001
# dfs(cnt, is_break, visited)

q = deque([(0, 0, 1)])
bfs(is_break, visited)

# while stack:
#     i, j = stack.pop()
#     cnt += 1
#     print(i, j, cnt)
#     for k in range(3):
#         ni = i + di[k]
#         nj = j + dj[k]
#         if 0<=ni<N and 0<=nj<M and visited[ni][nj] == -1:
#             if arr[ni][nj] == 0:
#                 visited[ni][nj] = cnt
#                 stack.append((ni, nj))
#             elif is_break == False:
#                 visited[ni][nj] = cnt
#                 stack.append((ni, nj))
#                 # 진행가능한지 확인하고
#                 for kk in range(3):
#                     nni = ni + di[kk]
#                     nnj = nj + dj[kk]
#                     if 0<=nni<N and 0<=nnj<M and visited[nni][nnj] == -1:
#                         if arr[nni][nnj] == 0:
#                             visited[nni][nnj] = cnt
#                             stack.append((nni, nnj))
#                             is_break = True
#                         else: # for kk
#                             break
    # print(stack)


# if answer:
#     print(min(answer))
# else:
#     print(-1)

if max_v == 1_000_001:
    print(-1)
else:
    print(max_v)