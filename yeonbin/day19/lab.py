# 연구소3  # 231009
# 바이러스 M개를 활성상태로 변경
# N*N 정사각형, 활성바이러스가 비활성칸으로 가면 활성으로 변함
# 0은 빈칸, 1은 벽, 2는 바이러스
# 바이러스 퍼뜨리는 최소시간 구하기

# BFS + delta
# 비활성 바이러스 어떻게 처리할건지? 마지막이 비활성이면 cnt-1해야함

# 방문표시할 배열, 바이러스를 다 퍼뜨렸는지확인

# 마지막에 틀림..왜?

import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
sys.stdin = open('input.txt')


def BFS(q):
    q = deque(q)
    # print(q)
    # print('----')
    # visited = [[0]*N for _ in range(N)]

    mini_visited = deepcopy(visited)
    # print(mini_visited)

    while q:
        i, j, cnt = q.popleft()
        mini_visited[i][j] = cnt+1
        # print(i, j, cnt)
        if cnt >= min_v:
            return min_v
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1:
                if mini_visited[ni][nj]==0:
                    q.append((ni, nj, cnt+1))
                    # visited
                    mini_visited[ni][nj] = 1
        # print('1', q)
        else: # 더이상 갈 곳이 없는데, 그 위치가 비활성바이러스
            if (i, j, 0) in virus:
                cnt -= 1
    # test
    for row in mini_visited:
        for col in row:
            print(col, end=' ')
        print()
    print('cnt', cnt)
    # 못 간곳이 있는지 확인
    if is_done(mini_visited):
        return cnt
    else:
        return -1

# 다 돌았는지 검사하는 함수
def is_done(v):
    for row in v:
        if row.count(0):
            # 0이 있으면 실패
            return False
    return True

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
virus = [] # 바이러스 위치, 이 중 에서 M개를 골라서 해야함

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# q = deque()
min_v = 2501

for row in range(N):
    for col in range(N):
        if arr[row][col]==2:
            virus.append((row, col, 0))
        elif arr[row][col]==1:
            visited[row][col] = '-'
# M개를 어떻게 고르지?! 조합?

if is_done(arr):
    print(0)

else:
    active = list(combinations(virus, M))
    # print(active)

    for qq in active:
        tmp = BFS(qq)
        if tmp != -1:
            min_v = tmp
            ans = tmp
        elif tmp==-1 and min_v==2501:
            ans = -1

    print(ans)

    # print(arr.count(0))
