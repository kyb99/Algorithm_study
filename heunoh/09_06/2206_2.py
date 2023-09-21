# 벽뿌셔 다뿌셔
import sys
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
can_break = True
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < M


result = []
stk = [(0, 0, 0)]


def backtracking(start, possibility):
    if not stk:
        return
    start_i, start_j, move_count = start.pop(0)
    if start_i == N-1 and start_j == M-1:
        return result.append(move_count)
    if not possibility and arr[start_i][start_j] == 1:
        return
    if result and move_count > min(result):
        return
    for k in range(4):
        ni = int(start_i) + di[k]
        nj = int(start_j) + dj[k]
        if is_valid(ni, nj) and arr[ni][nj] == '1' and not visited[ni][nj] and possibility:
            visited[ni][nj] = True
            possibility = False
            arr[ni][nj] = '0'
            stk.append((ni, nj, move_count+1))
            backtracking(stk, possibility)
            possibility = True
            visited[ni][nj] = False
            arr[ni][nj] = '1'
        elif is_valid(ni, nj) and arr[ni][nj] == '0' and not visited[ni][nj]:
            visited[ni][nj] = True
            stk.append((ni, nj, move_count+1))
            backtracking(stk, possibility)
            visited[ni][nj] = False


backtracking(stk, can_break)
if result:
    print(min(result)+1)
else:
    print('-1')