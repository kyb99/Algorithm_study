from collections import deque
from itertools import combinations

def search(virus):
    dq = deque()
    visited = [[False] * N for _ in range(N)]
    time = 0
    fill_cnt = 0
    for v in virus:
        dq.append(v)
    while True:
        length = len(dq)
        if length == 0 or fill_cnt == blank_cnt:
            if fill_cnt == blank_cnt:
                return time
            else:
                return 987654321
        time += 1
        for i in range(length):
            x, y = dq.popleft()
            visited[x][y] = True
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if lab[nx][ny] == 2: # 바이러스
                        dq.append((nx,ny))
                        visited[nx][ny] = True
                    elif lab[nx][ny] == 0:  # 빈칸
                        dq.append((nx,ny))
                        visited[nx][ny] = True
                        fill_cnt += 1


N,M = map(int ,input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
candidates = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
blank_cnt = 0
res = 987654321
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            candidates.append((i,j))
        if lab[i][j] == 0:
            blank_cnt += 1

for virus in combinations(candidates,M):
    res = min(res, search(virus))

if res == 987654321:
    print(-1)
else:
    print(res)