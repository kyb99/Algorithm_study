import sys
input = sys.stdin.readline
def backtracking(depth, idx):
    global res
    if depth == N:
        res += 1
        return
    for i in range(idx, M+1):
        if i == M:
            backtracking(depth+1, 0)
        else:
            if visited[depth-1][i] == 0 or visited[depth-1][i-1] == 0 or visited[depth][i-1] == 0:
                visited[depth][i] = True
                backtracking(depth, i+1)
                visited[depth][i] = False
N, M = map(int, input().split())
visited = [[False] * M for _ in range(N)]
res = 0
backtracking(0,0)
print(res)