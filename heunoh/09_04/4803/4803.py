import sys
sys.stdin = open('input.txt')
tc = 1
input = sys.stdin.readline
# 정점 하나도 트리로 치는듯 함
# 순회 하는것을 표현하는 방법을 찾아야 함
def bfs(start):
    global cnt
    stk = []
    stk.append(start)
    if visited[start] == True:
        return
    visited[start] = True
    if not stk:
        return
    while stk:
        idx = stk.pop(0)
        for nxt in arr[idx]:
            if not visited[nxt]:
                visited[nxt] = True
                stk.append(nxt)
            elif visited[nxt]:
                return
    cnt += 1

while True:
    cnt = 0
    N, M = map(int, input().split())
    if N + M == 0:
        break
    arr = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for i in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    if N == 1:
        cnt += 1
    #트리를 순회하고 count 를 세어야함
    for i in arr:
        print(i)
    for i in range(1, N+1):
        bfs(i)

    if cnt == 0:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')
    tc += 1
