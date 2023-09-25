# 좀 더 가다가 틀림

import sys
sys.stdin = open('4179_input.txt')

from collections import deque

R, C = map(int, input().split()) # 행, 열
arr = [list(input()) for _ in range(R)]

min_t = 0

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# bfs로 해보자
q = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            # 좌표와 시간 저장
            # 이미 가장자리에 있는 경우 탈출
            # 근데 이거 쓰니까 인덱스에러뜸
            # if i==0 or i==R-1 or j==0 or j==C-1:
            #     min_t = 1
            #     break # for j

            q.append((i, j, 1))
            arr[i][j] = 1

        elif arr[i][j] == 'F':
            q.append((i, j, -1))
            arr[i][j] = -1
    if min_t:
        break

while q:
    print(q)
    i, j, cnt = q.popleft()
        # 네 방향 탐색
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        # 범위를 벗어나지 않고
        if 0<=ni<R and 0<=nj<C:
            # 방문가능한 경우
            if arr[ni][nj] != '#':
                if cnt != -1 and arr[ni][nj]=='.':
                    # 가장자리에 도착한 경우
                    if ni==0 or nj ==0 or ni == R-1 or nj == C-1:
                        min_t = cnt+1
                        # print(ni, nj, min_t)
                        break # for k
                    else:
                        # 표시하고 추가
                        arr[ni][nj] = cnt+1
                        q.append((ni, nj, cnt+1))
                # 불인 경우
                elif cnt==-1 and arr[ni][nj]!=-1:
                    arr[ni][nj] = -1
                    q.append((ni, nj, -1))
    if min_t:
        break # while
# test
for row in arr:
    print(row)

if min_t:
    print(min_t)
else:
    print('IMPOSSIBLE')