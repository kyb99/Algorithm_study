# 불! # 230925 # 틀림! 테스트케이스 찾아보자
# 지훈이가 불에 타기전에 탈출할 수 있는지 여부
# 얼마나 빨리 탈출할 수 있는지 결정
# 불/지훈이가 매 분마다 한칸씩 이동
# 불은 네 방향으로 확산
# 지훈이는 가장자리에서 탈출가능
# 벽은 통과못함
# 동시에 움직인다!

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
fire = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            # 좌표와 시간 저장
            q.append((i, j, 1))
            arr[i][j] = 1

        elif arr[i][j] == 'F':
            fire.append((i, j))
            arr[i][j] = 'F'


while q:
    # 불이 먼저 움직여야하나?
    # 불이 두개이상인 경우?
    fire_cnt = len(fire)
    for mv in range(fire_cnt):
        f_i, f_j = fire.popleft()
        # 네 방향 탐색
        for k in range(4):
            f_ni = f_i + di[k]
            f_nj = f_j + dj[k]

            # 범위를 벗어나지 않고
            if 0<=f_ni<R and 0<=f_nj<C:
                # 불이 번질 수 있는 경우
                if arr[f_ni][f_nj] == '.':
                    arr[f_ni][f_nj] = 'F'
                    fire.append((f_ni, f_nj))
    
    # 지훈이가 움직이기
    i, j, cnt = q.popleft()

    if i==0 or j ==0 or i == R-1 or j == C-1:
                    min_t = cnt
                    # print(ni, nj, min_t)
                    break # for k

    # 네 방향 탐색
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        # 범위를 벗어나지 않고
        if 0<=ni<R and 0<=nj<C:
            # 방문가능한 경우
            if arr[ni][nj] == '.':
                # 가장자리에 도착한 경우
                if ni==0 or nj ==0 or ni == R-1 or nj == C-1:
                    min_t = cnt+1
                    # print(ni, nj, min_t)
                    break # for k
                else:
                    # 표시하고 추가
                    arr[ni][nj] = cnt+1
                    q.append((ni, nj, cnt+1))

    if min_t:
        break # while
# test
for row in arr:
    print(row)

if min_t:
    print(min_t)
else:
    print('IMPOSSIBLE')

# 지훈이가 갈 수 있는지 확인
# 가장자리에 도착했으면 그거 출력
# 더이상 갈 수 있는 곳이 없으면 IMPOSSIBLE 출력
# 불이 확산 되는곳 적기