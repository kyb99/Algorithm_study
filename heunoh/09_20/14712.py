# 넴모넴모모모

def check(i,j):
    pass


def backtracking(depth, number, idx):
    print('--------------------')
    for i in visited:
        print(i)
    print('--------------------')

    for i in range(idx, M):
        if not visited[depth][i]:
            visited[depth][i] = True
            if number and (number % (M-1))==0 and depth < N-1:
                backtracking(depth+1, number+1, 0)
                backtracking(depth, number+1, 0)
            else:
                backtracking(depth,number+1, idx + 1)
            visited[depth][i] = False

N, M = map(int, input().split())
arr = [[False] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
print(arr)
backtracking(0,0,0)