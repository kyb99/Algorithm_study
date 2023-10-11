# 연구소3
# 0은 빈칸, 1은 벽, 2는 바이러스위 위치
# N칸의 연구소, M개의 바이러스를 골라서 활성화
from collections import deque
from copy import deepcopy
from itertools import combinations
N, M = map(int ,input().split())
laboratory = [list(map(int, input().split())) for  _ in range(N)]
visited = [[False] * N for _ in range(N)]
candidate = []
to_check = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 987654321

for i in range(N):
    for j in range(N):
        if laboratory[i][j] == 2:
            candidate.append((i,j))
        elif laboratory[i][j] == 1:
            visited[i][j] = True


def is_valid(x,y):
    return 0 <= x < N and 0 <= y < N

def comb(depth, idx):
    if depth == M:
        search(to_check)
        return
    else:
        for next in range(idx,M):
            to_check.append(candidate[next])
            comb(depth+1, next+1)
            to_check.pop()

def search(candi):
    global time
    dq = deque()
    for i,j in candi:
        dq.append((i,j,0))
    now_visited = deepcopy(visited)
    now_laboratory = deepcopy(laboratory)
    while dq:
        cur_x, cur_y, tmp = dq.popleft()
        now_visited[cur_x][cur_y] = True
        now_laboratory[cur_x][cur_y] = -1
        for k in range(4):
            nx = cur_x + dx[k]
            ny = cur_y + dy[k]
            if is_valid(nx,ny) and now_laboratory[nx][ny] != 1 and not now_visited[nx][ny]:
                now_visited[nx][ny] = True
                if now_laboratory[nx][ny] == -1: # 바이러스가 있으니 넘어가자
                    continue
                if now_laboratory[nx][ny] == 2:  #
                    dq.append((nx,ny,tmp))
                    now_laboratory[nx][ny] = -1
                    continue
                now_laboratory[nx][ny] = -1
                dq.append((nx,ny,tmp+1))
    #print(tmp)
    for i in range(N):
        for j in range(N):
            if now_laboratory[i][j] == 0:
                return
    time = min(time, tmp)

comb(0,0)
if time != 987654321:
    print(time)
else:
    print(-1)




